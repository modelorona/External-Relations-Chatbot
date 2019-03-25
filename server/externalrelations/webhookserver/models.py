from django.db import models


class ShortCourse(models.Model):
    Subject_area = models.TextField(max_length=150)
    Title = models.TextField(max_length=150)
    Class_code = models.IntegerField()
    Start_time = models.DecimalField(max_digits=10, decimal_places=2)
    End_time = models.DecimalField(max_digits=10, decimal_places=2)
    Cost = models.DecimalField(max_digits=10, decimal_places=2)
    Duration = models.IntegerField()
    Tutor = models.TextField(max_length=120)
    Venue = models.TextField()
    Link_to_Course_specification = models.TextField()
    Description = models.TextField(max_length=65535)
    Credits_attached = models.IntegerField()
    Language_Level_of_Study_links = models.TextField()
    pk_id = models.AutoField(primary_key=True)
    Start_date = models.DateField()
    End_date = models.DateField()

    class Meta:
        db_table = 'Short_Courses'
        #managed = False  # to not override the tables
        verbose_name = 'Short Course'
        verbose_name_plural = 'Short Courses'

    def __str__(self):
        return self.Title

    @classmethod
    def all_course_titles(cls):
        records = ShortCourse.objects.all()
        return records

    @classmethod
    def all_subjects(cls):
        records = ShortCourse.objects.values('Subject_area').distinct()
        return records

    @classmethod
    def specific_subject_courses(cls, subject):
        records = ShortCourse.objects.filter(Subject_area=subject)
        return records

    @classmethod
    def find_with_filters(cls, value, filters):
        return ShortCourse.objects.filter(**filters).values(value).first()