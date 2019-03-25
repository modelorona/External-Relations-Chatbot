# from django.shortcuts import render
from json import loads
from smtplib import SMTPException
from os import getenv

from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .intent_handler import handle
from .utils import deep_get


@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        return HttpResponse("Hello World, from webhook!", content_type='text/html')
    else:
        data = loads(request.body)
        user_intent = deep_get(data, 'queryResult.intent.displayName')

        if user_intent is None:
            if deep_get(data, 'type') == 'email':
                try:
                    name = deep_get(data, 'name')
                    query = deep_get(data, 'query')
                    email = deep_get(data, 'email')
                    send_mail(
                        subject='{} has a query that Gilbert could not answer'.format(name),
                        message='Their query was {} \n\nTheir email is {}.'.format(query, email),
                        from_email=getenv('FROM_EMAIL'),
                        recipient_list=[getenv('CLIENT_EMAIL')],
                        fail_silently=False
                    )
                    return JsonResponse({'fulfillmentText': 'Email sent'})
                except SMTPException as e:
                    print(e)
                    return JsonResponse({'fulfillmentText': 'Email not sent'})

            return JsonResponse({
                'fulfillmentText': 'Something happened on our end.'
            })

        elif user_intent == 'Test':
            return JsonResponse({
                'fulfillmentText': 'Test Passed'
            })

        parameters = deep_get(data, 'queryResult.parameters')
        return_data = handle({'intent': user_intent, 'parameters': parameters})

        return JsonResponse({
            'fulfillmentText': return_data
        })
