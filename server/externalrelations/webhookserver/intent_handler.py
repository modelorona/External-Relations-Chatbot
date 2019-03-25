import datetime

from dateutil.relativedelta import *

from .models import ShortCourse


def handle(data):
    if data['intent'] == 'Available Courses':
        return all_course_titles()
    elif data['intent'] == 'Subject Areas':
        return all_subjects()
    elif data['intent'] == 'Subject area -> Title':
        return specific_subject_courses(data['parameters']['Subject_area'])
    elif data['intent'] == 'FindTitle':
        return find_title(data['parameters'])
    elif data['intent'] == 'FindClassCode':
        return find_id(data['parameters'])
    elif data['intent'] == 'FindCost':
        return find_cost(data['parameters'])
    elif data['intent'] == 'FindCredits':
        return find_credits(data['parameters'])
    elif data['intent'] == 'FindDescription':
        return find_description(data['parameters'])
    elif data['intent'] == 'FindDuration':
        return find_duration(data['parameters'])
    elif data['intent'] == 'FindEndDate':
        return find_end_date(data['parameters'])
    elif data['intent'] == 'FindLecturer':
        return find_lecturer(data['parameters'])
    elif data['intent'] == 'FindStartDate':
        return find_start_date(data['parameters'])
    elif data['intent'] == 'FindSubjectArea':
        return find_subject_area(data['parameters'])
    elif data['intent'] == 'FindVenue':
        return find_venue(data['parameters'])


def all_course_titles():
    data = ShortCourse.all_course_titles()
    resp = 'All courses that are available to take are as follows: '
    return '{}{}'.format(resp, ', '.join([row.Title for row in data]))


def all_subjects():
    data = ShortCourse.all_subjects()
    resp = 'All subjects that are available are as follows: '
    return '{}{}'.format(resp, ', '.join([row.get('Subject_area') for row in data]))


def specific_subject_courses(subject):
    data = ShortCourse.specific_subject_courses(subject)
    resp = 'All courses that belong to {} are as follows: '.format(subject)
    return '{}{}'.format(resp, ', '.join([row.Title for row in data]))


# ------------------------------------------Many to One questions ------------------------------------
# ----------------------------------------------------------------------------------------------------


# figure out if number is ID or credits
def class_code_or_credits(number, number1, credits, class_code):
    if isinstance(number, (list,)):
        number = number[0]
    if credits and class_code:
        if number > number1:
            number = 'Class_code'
            number1 = 'Credits_attached'
        else:
            number = 'Credits_attached'
            number1 = 'Class_code'
    elif credits:
        number = 'Credits_attached'
        number1 = 'UNNECESSARY'
    elif class_code or number:
        number = 'Class_code'
        number1 = 'UNNECESSARY'
    return number, number1


def start_or_end(param_date, param_date1, start, end):
    if isinstance(param_date, (list,)):
        param_date = param_date[0]
    if param_date and param_date1:
        date = datetime.datetime.strptime(param_date[0:10], '%Y-%m-%d').date()
        if date > datetime.date(2019, 9, 1):
            date = date + relativedelta(years=-1)
        param_date = date
        date1 = datetime.datetime.strptime(param_date1[0:10], '%Y-%m-%d').date()
        if date1 > datetime.date(2019, 9, 1):
            date1 = date1 + relativedelta(years=-1)
        param_date1 = date1
        if date > date1:
            date_return = 'End_date'
            date1_return = 'Start_date'
        elif date < date1:
            date1_return = 'End_date'
            date_return = 'Start_date'
        else:
            date1_return = 'End_date'
            date_return = 'Start_date'
    elif start or (param_date and not end):
        date = datetime.datetime.strptime(param_date[0:10], '%Y-%m-%d').date()
        if date > datetime.date(2019, 9, 1):
            date = date + relativedelta(years=-1)
        param_date = date
        param_date1 = None
        date_return = 'Start_date'
        date1_return = 'UNNECESSARY'
    elif end:
        date = datetime.datetime.strptime(param_date[0:10], '%Y-%m-%d').date()
        if date > datetime.date(2019, 9, 1):
            date = date + relativedelta(years=-1)
        param_date = date
        param_date1 = None
        date_return = 'End_date'
        date1_return = 'UNNECESSARY'
    else:
        date_return = 'UNNECESSARY'
        date1_return = 'UNNECESSARY'
    return param_date, param_date1, date_return, date1_return


# ------------------------------------------------------------------------------------------------------


def find_title(parameters):
    print(parameters)
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY'}

    # figure out if number is ID or credits
    dialog_to_db['number'], dialog_to_db['number1'] = class_code_or_credits(parameters['number'], parameters['number1'], parameters['Credits'], parameters['Class_code'])
    # figure out which date is start and/or end
    parameters['date'], parameters['date1'], dialog_to_db['date'], dialog_to_db['date1'] = start_or_end(parameters['date'], parameters['date1'], parameters['Date_start'], parameters['Date_end'])

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    if 'UNNECESSARY' in given_parameters:
        del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Cost':
            given_parameters[k] = v['amount']
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Title', given_parameters)
    print(title)
    resp = 'The title of a course matching that description is '
    return "{}{}".format(resp, title.get('Title'))


# ------------           ----------               -----------------            ----------

def find_id(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'number': 'Credits_attached', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY',
                    'Description': 'UNNECESSARY'}

    # figure out which date is start and/or end
    parameters['date'], parameters['date1'], dialog_to_db['date'], dialog_to_db['date1'] = start_or_end(parameters['date'], parameters['date1'], parameters['Date_start'], parameters['Date_end'])

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    if 'UNNECESSARY' in given_parameters:
        del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Cost':
            given_parameters[k] = v['amount']
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Class_code', given_parameters)
    resp = 'The id of a course matching that description is '
    return "{}{}".format(resp, title.get('Class_code'))


# ------------           ----------               -----------------            ----------

def find_cost(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY'}

    # figure out if number is ID or credits
    dialog_to_db['number'], dialog_to_db['number1'] = class_code_or_credits(parameters['number'], parameters['number1'], parameters['Credits'], parameters['Class_code'])
    # figure out which date is start and/or end
    parameters['date'], parameters['date1'], dialog_to_db['date'], dialog_to_db['date1'] = start_or_end(parameters['date'], parameters['date1'], parameters['Date_start'], parameters['Date_end'])

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    if 'UNNECESSARY' in given_parameters:
        del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Cost', given_parameters)
    resp = 'This course costs '
    pounds = ' pounds'
    return "{}{}{}".format(resp, title.get('Cost'), pounds)


# ------------           ----------               -----------------            ----------

def find_credits(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'Class_code', 'Credits1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY'}

    # figure out which date is start and/or end
    parameters['date'], parameters['date1'], dialog_to_db['date'], dialog_to_db['date1'] = start_or_end(parameters['date'], parameters['date1'], parameters['Date_start'], parameters['Date_end'])

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    if 'UNNECESSARY' in given_parameters:
        del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Cost':
            given_parameters[k] = v['amount']
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Credits_attached', given_parameters)
    resp = 'The number of credits given by that course is '
    return "{}{}".format(resp, title.get('Credits_attached'))


# ------------           ----------               -----------------            ----------

def find_description(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY',
                    'Description': 'UNNECESSARY'}

    # figure out if number is ID or credits
    dialog_to_db['number'], dialog_to_db['number1'] = class_code_or_credits(parameters['number'], parameters['number1'], parameters['Credits'], parameters['Class_code'])
    # figure out which date is start and/or end
    parameters['date'], parameters['date1'], dialog_to_db['date'], dialog_to_db['date1'] = start_or_end(parameters['date'], parameters['date1'], parameters['Date_start'], parameters['Date_end'])

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    if 'UNNECESSARY' in given_parameters:
        del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Description', given_parameters)
    resp = 'The description of a course matching those parameters is '
    return "{}{}".format(resp, title.get('Description'))


# ------------           ----------               -----------------            ----------

def find_duration(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY',
                    'desription': 'Description'}

    # figure out if number is ID or credits
    dialog_to_db['number'], dialog_to_db['number1'] = class_code_or_credits(parameters['number'], parameters['number1'], parameters['Credits'], parameters['Class_code'])
    # figure out which date is start and/or end
    parameters['date'], parameters['date1'], dialog_to_db['date'], dialog_to_db['date1'] = start_or_end(parameters['date'], parameters['date1'], parameters['Date_start'], parameters['Date_end'])

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    if 'UNNECESSARY' in given_parameters:
        del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
    title = ShortCourse.find_with_filters('Duration', given_parameters)
    resp = 'The duration of a course matching that description is '
    days = ' days'
    return "{}{}{}".format(resp, title.get('Duration'), days)


# ------------           ----------               -----------------            ----------

def find_end_date(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'Start_date', 'desription': 'Description',
                    'Date_end': 'UNNECESSARY'}

    if parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d').date()
        if date > datetime.date(2019, 9, 1):
            date = date + relativedelta(years=-1)
        parameters['date'] = date

    # figure out if number is ID or credits
    dialog_to_db['number'], dialog_to_db['number1'] = class_code_or_credits(parameters['number'], parameters['number1'], parameters['Credits'], parameters['Class_code'])

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    if 'UNNECESSARY' in given_parameters:
        del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('End_date', given_parameters)
    hour = ShortCourse.find_with_filters('End_time', given_parameters)
    resp = 'The end date of a course matching that description is '
    time = ' at '
    return "{}{}{}{}".format(resp, title.get('End_date'), time, hour.get('End_time'))


# ------------           ----------               -----------------            ----------

def find_start_date(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'End_date', 'desription': 'Description',
                    'Date_end': 'UNNECESSARY'}

    if parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d').date()
        if date > datetime.date(2019, 9, 1):
            date = date + relativedelta(years=-1)
        parameters['date'] = date

        # figure out if number is ID or credits
    dialog_to_db['number'], dialog_to_db['number1'] = class_code_or_credits(parameters['number'], parameters['number1'], parameters['Credits'], parameters['Class_code'])

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    if 'UNNECESSARY' in given_parameters:
        del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    print(given_parameters)
    title = ShortCourse.find_with_filters('Start_date', given_parameters)
    hour = ShortCourse.find_with_filters('Start_time', given_parameters)
    resp = 'The start date of a course matching that description is '
    time = ' at '
    return "{}{}{}{}".format(resp, title.get('Start_date'), time, hour.get('Start_time'))


# ------------           ----------               -----------------            ----------

def find_lecturer(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY',
                    'desription': 'Description'}

    # figure out if number is ID or credits
    dialog_to_db['number'], dialog_to_db['number1'] = class_code_or_credits(parameters['number'], parameters['number1'], parameters['Credits'], parameters['Class_code'])
    # figure out which date is start and/or end
    parameters['date'], parameters['date1'], dialog_to_db['date'], dialog_to_db['date1'] = start_or_end(parameters['date'], parameters['date1'], parameters['Date_start'], parameters['Date_end'])

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    if 'UNNECESSARY' in given_parameters:
        del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Tutor', given_parameters)
    resp = 'The lecturer of a course matching that description is '
    return "{}{}".format(resp, title.get('Tutor'))


# ------------           ----------               -----------------            ----------        

def find_subject_area(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY', 'desription': 'Description'}

    # figure out if number is ID or credits
    dialog_to_db['number'], dialog_to_db['number1'] = class_code_or_credits(parameters['number'], parameters['number1'], parameters['Credits'], parameters['Class_code'])
    # figure out which date is start and/or end
    parameters['date'], parameters['date1'], dialog_to_db['date'], dialog_to_db['date1'] = start_or_end(parameters['date'], parameters['date1'], parameters['Date_start'], parameters['Date_end'])

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    if 'UNNECESSARY' in given_parameters:
        del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Subject_area', given_parameters)
    resp = 'The subject area of a course matching that description is '
    return "{}{}".format(resp, title.get('Subject_area'))


# ------------           ----------               -----------------            ----------

def find_venue(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY',
                    'desription': 'Description'}

    # figure out if number is ID or credits
    dialog_to_db['number'], dialog_to_db['number1'] = class_code_or_credits(parameters['number'], parameters['number1'], parameters['Credits'], parameters['Class_code'])
    # figure out which date is start and/or end
    parameters['date'], parameters['date1'], dialog_to_db['date'], dialog_to_db['date1'] = start_or_end(parameters['date'], parameters['date1'], parameters['Date_start'], parameters['Date_end'])

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    if 'UNNECESSARY' in given_parameters:
        del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Venue', given_parameters)
    if 'will be listed' in title.get('Venue'):
        return 'The venue for this course has not been confirmed yet. Room number will be listed at reception on the day/evening of the class'
    resp = 'The venue for a course matching that description is '
    return "{}{}".format(resp, title.get('Venue'))
