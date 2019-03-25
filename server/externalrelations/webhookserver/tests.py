from json import dumps

from django.test import TestCase, Client
from .models import ShortCourse
from .intent_handler import *
import datetime


class AppGetTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.response = cls.client.get('/')

    def test_get_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_get_content_length(self):
        self.assertGreater(len(str(self.response.content)), 0)

    def test_get_charset_type(self):
        self.assertEqual(self.response.charset, 'utf-8')

    def test_get_body_content(self):
        self.assertEqual(self.response.content.decode('utf-8'), 'Hello World, from webhook!')


class AppEmptyPostTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.response = cls.client.post('/', data=dumps({}), format='json', content_type='application/json')

    def test_post_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_content_length(self):
        self.assertGreater(len(str(self.response.content)), 0)

    def test_post_charset_type(self):
        self.assertEqual(self.response.charset, 'utf-8')

    def test_post_body_content(self):
        self.assertJSONEqual(self.response.content.decode('utf-8'),
                             {'fulfillmentText': 'Something happened on our end.'})


class AppSamplePostTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.response = cls.client.post('/', dumps(dict({'queryResult': {'intent': {'displayName': 'Test'}}})),
                                       format='json', content_type='application/json')

    def test_post_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_content_length(self):
        self.assertGreater(len(str(self.response.content)), 0)

    def test_post_charset_type(self):
        self.assertEqual(self.response.charset, 'utf-8')

    def test_post_body_content(self):
        self.assertJSONEqual(self.response.content.decode('utf-8'), {'fulfillmentText': 'Test Passed'})


class IntentTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

# ---------------------------------------------- models.py ----------------------------------------------
class ModelsTestCase(TestCase):
    @classmethod
    def setUp(self):
        ShortCourse.objects.create(Subject_area = 'Archaeology Classical Studies and Egyptology', Title = 'Ancient Egypt and the Bible', Class_code = 9248, Start_time = 19.00, End_time = 21.00, Cost = 125.00, Duration = 64, Tutor = 'Judit Blair', Venue = 'University of Glasgow- Building will be confirmed by email three days before the start date. Room number will be listed at reception on the day/evening of the class', Link_to_Course_specification = 'http://www.gla.ac.uk/coursecatalogue/course/?code=ADED11520E', Description = 'Christian thinking has been greatly influenced by ancient traditions. According to the Bible, throughout history there had always been a contact between the Egyptians and the Israelites. Indeed, Egyptology in the 19th century was mainly concerned with discovering cultural records and thus evidence for certain biblical events. Without intending to prove or disprove the historicity of biblical events or characters, this course looks at similar themes in the religions of ancient Egypt and Israel, as well as key figures using the latest discoveries in the field./', Credits_attached = 10, Language_Level_of_Study_links = 'NA', Start_date = datetime.date(2019, 1, 17), End_date = datetime.date(2019, 3, 21))
        ShortCourse.objects.create(Subject_area = 'Art and Art History', Title = 'Botanical painting and illustration', Class_code = 13926, Start_time = 9.30, End_time = 12.30, Cost = 180.00, Duration = 10, Tutor = 'Clare Crines', Venue = 'University of Glasgow- Building will be confirmed by email three days before the start date. Room number will be listed at reception on the day/evening of the class', Link_to_Course_specification = 'http://www.gla.ac.uk/coursecatalogue/course/?code=ADED11217', Description = 'This course is suitable for beginners and students with some previous experience. It is for people with little or no prior drawing experience who want to learn how to draw flowers, fruit and vegetables with ease. Through tutor demonstrations you will see how to use watercolour properly and by the end of the course you will have a body of completed work. Materials are not included.', Credits_attached = 0, Language_Level_of_Study_links = 'NA', Start_date = datetime.date(2018, 9, 24), End_date = datetime.date(2018, 11, 26))
        #ShortCourse.objects.create(Subject_area = 'Creative Writing', Title = 'Writing Fiction', Class_code = 10307, Start_time = 19.00, End_time = 21.00, Cost = 125.00, Duration = 64, Tutor = 'Alan McMunnigall', Venue = 'University of Glasgow- Building will be confirmed by email three days before the start date. Room number will be listed at reception on the day/evening of the class', Link_to_Course_specification = 'http://www.gla.ac.uk/coursecatalogue/course/?code=ADED11217', Description = "This course will focus on the discussion of students' fiction. Literary forms and structures will be discussed. Published work from a range of authors will be studied and students will learn a range of literary techniques that they can develop and employ in their own fiction.", Credits_attached = 0, Language_Level_of_Study_links = 'NA', Start_date = datetime.datetime(2019, 4, 16), End_date = datetime.datetime(2019, 6, 18))


    def test_all_course_titles(self):
        titles = ShortCourse.all_course_titles()
        titles_list = [row.Title for row in titles]
        self.assertEqual(titles_list, ['Ancient Egypt and the Bible', 'Botanical painting and illustration'])

    def test_all_subjects(self):
        subjects = ShortCourse.all_subjects()
        subjects_list = [row.get('Subject_area') for row in subjects]
        self.assertEqual(subjects_list, ['Archaeology Classical Studies and Egyptology', 'Art and Art History'])

    def test_specific_subject_courses(self):
        subject_courses = ShortCourse.specific_subject_courses('Archaeology Classical Studies and Egyptology')
        subject_courses_list = [row.Title for row in subject_courses]
        self.assertEqual(subject_courses_list, ['Ancient Egypt and the Bible'])

    def test_find_id(self):
        result = ShortCourse.find_with_filters('Class_code', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('Class_code'), 9248)

    def test_find_starttime(self):
        result = ShortCourse.find_with_filters('Start_time', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('Start_time'), 19.00)

    def test_find_endtime(self):
        result = ShortCourse.find_with_filters('End_time', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('End_time'), 21.00)

    def test_find_cost(self):
        result = ShortCourse.find_with_filters('Cost', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('Cost'), 125.00)
        
    def test_find_duration(self):
        result = ShortCourse.find_with_filters('Duration', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('Duration'), 64)

    def test_find_tutor(self):
        result = ShortCourse.find_with_filters('Tutor', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('Tutor'), 'Judit Blair')

    def test_find_venue(self):
        result = ShortCourse.find_with_filters('Venue', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('Venue'), 'University of Glasgow- Building will be confirmed by email three days before the start date. Room number will be listed at reception on the day/evening of the class')

    def test_find_specification(self):
        result = ShortCourse.find_with_filters('Link_to_Course_specification', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('Link_to_Course_specification'), 'http://www.gla.ac.uk/coursecatalogue/course/?code=ADED11520E')

    def test_find_description(self):
        result = ShortCourse.find_with_filters('Description', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('Description'), 'Christian thinking has been greatly influenced by ancient traditions. According to the Bible, throughout history there had always been a contact between the Egyptians and the Israelites. Indeed, Egyptology in the 19th century was mainly concerned with discovering cultural records and thus evidence for certain biblical events. Without intending to prove or disprove the historicity of biblical events or characters, this course looks at similar themes in the religions of ancient Egypt and Israel, as well as key figures using the latest discoveries in the field./')
        
    def test_find_credits(self):
        result = ShortCourse.find_with_filters('Credits_attached', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('Credits_attached'), 10)

    def test_find_language(self):
        result = ShortCourse.find_with_filters('Language_Level_of_Study_links', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('Language_Level_of_Study_links'), 'NA')

    def test_find_startdate(self):
        result = ShortCourse.find_with_filters('Start_date', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('Start_date'), datetime.date(2019, 1, 17))
        
    def test_find_enddate(self):
        result = ShortCourse.find_with_filters('End_date', {'Tutor': 'Judit Blair'})
        self.assertEqual(result.get('End_date'), datetime.date(2019, 3, 21))
		

# ---------------------------------------------- intent_handler.py ----------------------------------------------

class IntentHandlerTestCase(TestCase):
    @classmethod
    def setUp(self):
        ShortCourse.objects.create(Subject_area = 'Archaeology Classical Studies and Egyptology', Title = 'Ancient Egypt and the Bible', Class_code = 9248, Start_time = 19.00, End_time = 21.00, Cost = 125.00, Duration = 64, Tutor = 'Judit Blair', Venue = 'University of Glasgow- Building will be confirmed by email three days before the start date. Room number will be listed at reception on the day/evening of the class', Link_to_Course_specification = 'http://www.gla.ac.uk/coursecatalogue/course/?code=ADED11520E', Description = 'Christian thinking has been greatly influenced by ancient traditions. According to the Bible, throughout history there had always been a contact between the Egyptians and the Israelites. Indeed, Egyptology in the 19th century was mainly concerned with discovering cultural records and thus evidence for certain biblical events. Without intending to prove or disprove the historicity of biblical events or characters, this course looks at similar themes in the religions of ancient Egypt and Israel, as well as key figures using the latest discoveries in the field./', Credits_attached = 10, Language_Level_of_Study_links = 'NA', Start_date = datetime.date(2019, 1, 17), End_date = datetime.date(2019, 3, 21))
        ShortCourse.objects.create(Subject_area = 'Art and Art History', Title = 'Botanical painting and illustration', Class_code = 13926, Start_time = 9.30, End_time = 12.30, Cost = 180.00, Duration = 10, Tutor = 'Clare Crines', Venue = 'University of Glasgow- Building will be confirmed by email three days before the start date. Room number will be listed at reception on the day/evening of the class', Link_to_Course_specification = 'http://www.gla.ac.uk/coursecatalogue/course/?code=ADED11217', Description = 'This course is suitable for beginners and students with some previous experience. It is for people with little or no prior drawing experience who want to learn how to draw flowers, fruit and vegetables with ease. Through tutor demonstrations you will see how to use watercolour properly and by the end of the course you will have a body of completed work. Materials are not included.', Credits_attached = 0, Language_Level_of_Study_links = 'NA', Start_date = datetime.date(2018, 9, 24), End_date = datetime.date(2018, 11, 26))
        #ShortCourse.objects.create(Subject_area = 'Creative Writing', Title = 'Writing Fiction', Class_code = 10307, Start_time = 19.00, End_time = 21.00, Cost = 125.00, Duration = 64, Tutor = 'Alan McMunnigall', Venue = 'University of Glasgow- Building will be confirmed by email three days before the start date. Room number will be listed at reception on the day/evening of the class', Link_to_Course_specification = 'http://www.gla.ac.uk/coursecatalogue/course/?code=ADED11217', Description = "This course will focus on the discussion of students' fiction. Literary forms and structures will be discussed. Published work from a range of authors will be studied and students will learn a range of literary techniques that they can develop and employ in their own fiction.", Credits_attached = 0, Language_Level_of_Study_links = 'NA', Start_date = datetime.datetime(2019, 4, 16), End_date = datetime.datetime(2019, 6, 18))

    def test_all_course_titles_intent(self):
	    self.assertEqual(all_course_titles(), 'All courses that are available to take are as follows: Ancient Egypt and the Bible, Botanical painting and illustration')

    def test_all_subjects_intent(self):
	    self.assertEqual(all_subjects(), 'All subjects that are available are as follows: Archaeology Classical Studies and Egyptology, Art and Art History')
		
    def test_specific_subject_courses_intent(self):
	    self.assertEqual(specific_subject_courses('Archaeology Classical Studies and Egyptology'), 'All courses that belong to Archaeology Classical Studies and Egyptology are as follows: Ancient Egypt and the Bible')

    def test_find_title(self):
	    self.assertEqual(find_title({'Lecturer': 'Judit Blair', 'number':'', 'number1':'', 'Credits':'', 'Class_code':'', 'date1':'', 'Date_start':'' ,'date':'', 'Date_end':'', 'Keyword_Course':'UNNECESSARY'}), 'The title of a course matching that description is Ancient Egypt and the Bible')

    def test_find_id(self):
	    self.assertEqual(find_id({'Lecturer': 'Judit Blair', 'number':'', 'number1':'', 'Credits':'', 'Class_code':'', 'date1':'', 'Date_start':'' ,'date':'', 'Date_end':'', 'Keyword_Course':'UNNECESSARY'}), 'The id of a course matching that description is 9248')

    def test_find_cost(self):
	    self.assertEqual(find_cost({'Lecturer': 'Judit Blair', 'number':'', 'number1':'', 'Credits':'', 'Class_code':'', 'date1':'', 'Date_start':'' ,'date':'', 'Date_end':'', 'Keyword_Course':'UNNECESSARY'}), 'This course costs 125.00 pounds')

    def test_find_credits(self):
	    self.assertEqual(find_credits({'Lecturer': 'Judit Blair', 'number':'', 'Credits':'', 'Class_code':'', 'date1':'', 'Date_start':'' ,'date':'', 'Date_end':'', 'Keyword_Course':'UNNECESSARY'}), 'The number of credits given by that course is 10')

    def test_find_description(self):
	    self.assertEqual(find_description({'Lecturer': 'Judit Blair', 'number':'', 'number1':'', 'Credits':'', 'Class_code':'', 'date1':'', 'Date_start':'' ,'date':'', 'Date_end':'', 'Keyword_Course':'UNNECESSARY'}), 'The description of a course matching those parameters is Christian thinking has been greatly influenced by ancient traditions. According to the Bible, throughout history there had always been a contact between the Egyptians and the Israelites. Indeed, Egyptology in the 19th century was mainly concerned with discovering cultural records and thus evidence for certain biblical events. Without intending to prove or disprove the historicity of biblical events or characters, this course looks at similar themes in the religions of ancient Egypt and Israel, as well as key figures using the latest discoveries in the field./')

    def test_find_duration(self):
	    self.assertEqual(find_duration({'Lecturer': 'Judit Blair', 'number':'', 'number1':'', 'Credits':'', 'Class_code':'', 'date1':'', 'Date_start':'' ,'date':'', 'Date_end':'', 'Keyword_Course':'UNNECESSARY'}), 'The duration of a course matching that description is 64 days')

    def test_find_end_date(self):
	    self.assertEqual(find_end_date({'Lecturer': 'Judit Blair', 'number':'', 'number1':'', 'Credits':'', 'Class_code':'', 'Date_start':'' ,'date':'', 'Date_end':'', 'Keyword_Course':'UNNECESSARY'}), 'The end date of a course matching that description is 2019-03-21 at 21.00')

    def test_find_lecturer(self):
	    self.assertEqual(find_lecturer({'Subject_area': 'Archaeology Classical Studies and Egyptology', 'number':'', 'number1':'', 'Credits':'', 'Class_code':'', 'date1':'', 'Date_start':'' ,'date':'', 'Date_end':'', 'Keyword_Course':'UNNECESSARY'}), 'The lecturer of a course matching that description is Judit Blair')

    def test_find_start_date(self):
	    self.assertEqual(find_start_date({'Lecturer': 'Judit Blair', 'number':'', 'number1':'', 'Credits':'', 'Class_code':'', 'Date_start':'' ,'date':'', 'Date_end':'', 'Keyword_Course':'UNNECESSARY'}), 'The start date of a course matching that description is 2019-01-17 at 19.00')

    def test_find_subject_area(self):
	    self.assertEqual(find_subject_area({'Lecturer': 'Judit Blair', 'number':'', 'number1':'', 'Credits':'', 'Class_code':'', 'date1':'', 'Date_start':'' ,'date':'', 'Date_end':'', 'Keyword_Course':'UNNECESSARY'}), 'The subject area of a course matching that description is Archaeology Classical Studies and Egyptology')

    def test_find_venue(self):
	    self.assertEqual(find_venue({'Lecturer': 'Judit Blair', 'number':'', 'number1':'', 'Credits':'', 'Class_code':'', 'date1':'', 'Date_start':'' ,'date':'', 'Date_end':'', 'Keyword_Course':'UNNECESSARY'}), 'The venue for this course has not been confirmed yet. Room number will be listed at reception on the day/evening of the class')
