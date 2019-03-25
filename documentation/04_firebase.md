# Firebase

There is not much going on here. We use only the function offering by Firebase, and it's one
function at that.

The function takes user input from the frontend and sends it to DialogFlow to do its magic, and then returns
the response to the user.

It checks for some specific intents, listed below.

- Good bye, good night - checks this to see if the user is ending the chat and show the feedback form
- anything that starts with smalltalk - this is a dialogflow feature to simulate "real flowing conversation"
- text to speech on/off - these are two separate intents to see if the user wants to the speech to be read aloud or not
- send email to client - this is to see if the client should show the form for the user to fill out to send the email

The status codes are just for the client to be able to conveniently check how the response should be handled. They have absolutely
no correlation or relation with actual HTTP codes.
