from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from Index.slugify import *

TYPE_OF_APPS = (
    ("Presentation WebSite", "Presentation WebSite"),
    ("WebApp", "Webapp"),
    ("Mobile App", "Mobile App"),
    ("Marketing Project", "Marketing Project")
)

WORKING_STATUS = (
    ("On Queue", "On Queue"),
    ("Current Working at", "Current Working at"),
)

PERCENT_CHOICES = (
    ("1%", "1%"),
    ("2%", "2%"),
    ("3%", "3%"),
    ("4%", "4%"),
    ("5%", "5%"),
    ("6%", "6%"),
    ("7%", "7%"),
    ("8%", "8%"),
    ("9%", "9%"),
    ("10%", "10%"),
    ("11%", "11%"),
    ("12%", "12%"),
    ("13%", "13%"),
    ("14%", "14%"),
    ("15%", "15%"),
    ("16%", "16%"),
    ("17%", "17%"),
    ("18%", "18%"),
    ("19%", "19%"),
    ("20%", "20%"),
    ("21%", "21%"),
    ("22%", "22%"),
    ("23%", "23%"),
    ("24%", "24%"),
    ("25%", "25%"),
    ("26%", "26%"),
    ("27%", "27%"),
    ("28%", "28%"),
    ("29%", "29%"),
    ("30%", "30%"),
    ("31%", "31%"),
    ("32%", "32%"),
    ("33%", "33%"),
    ("34%", "34%"),
    ("35%", "35%"),
    ("36%", "36%"),
    ("37%", "37%"),
    ("38%", "38%"),
    ("39%", "39%"),
    ("40%", "40%"),
    ("41%", "41%"),
    ("42%", "42%"),
    ("43%", "43%"),
    ("44%", "44%"),
    ("45%", "45%"),
    ("46%", "46%"),
    ("47%", "47%"),
    ("48%", "48%"),
    ("49%", "49%"),
    ("50%", "50%"),
    ("51%", "51%"),
    ("52%", "52%"),
    ("53%", "53%"),
    ("54%", "54%"),
    ("55%", "55%"),
    ("56%", "56%"),
    ("57%", "57%"),
    ("58%", "58%"),
    ("59%", "59%"),
    ("60%", "60%"),
    ("61%", "61%"),
    ("62%", "62%"),
    ("63%", "63%"),
    ("64%", "64%"),
    ("65%", "65%"),
    ("66%", "66%"),
    ("67%", "67%"),
    ("68%", "68%"),
    ("69%", "69%"),
    ("70%", "70%"),
    ("71%", "71%"),
    ("72%", "72%"),
    ("73%", "73%"),
    ("74%", "74%"),
    ("75%", "75%"),
    ("76%", "76%"),
    ("77%", "77%"),
    ("78%", "78%"),
    ("79%", "79%"),
    ("80%", "80%"),
    ("81%", "81%"),
    ("82%", "82%"),
    ("83%", "83%"),
    ("84%", "84%"),
    ("85%", "85%"),
    ("86%", "86%"),
    ("87%", "87%"),
    ("88%", "88%"),
    ("89%", "89%"),
    ("90%", "90%"),
    ("91%", "91%"),
    ("92%", "92%"),
    ("93%", "93%"),
    ("94%", "94%"),
    ("95%", "95%"),
    ("96%", "96%"),
    ("97%", "97%"),
    ("98%", "98%"),
    ("99%", "99%"),
    ("100%", "100%"),
)


class FinishedProject(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='user')
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    list_of_functionalities = models.TextField()
    type = models.CharField(max_length=100, choices=TYPE_OF_APPS)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    project_classification = models.CharField(max_length=100, default='Finished')
    finished_project_slug = models.SlugField(max_length=200, unique=True, default='')

    def save(self, **kwargs):
        finished_project_slug = "%s %s %s" % (self.project_name, self.project_classification, self.user)
        unique_slugify(self, finished_project_slug, 'finished_project_slug')
        super(FinishedProject, self).save(**kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):

        return self.project_name


class ActiveWorkingProject(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='user')
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    list_of_functionalities = models.TextField()
    type = models.CharField(max_length=100, choices=TYPE_OF_APPS)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    percent_done = models.CharField(max_length=10, choices=PERCENT_CHOICES, default="1%")
    deadline = models.DateTimeField(default=datetime.now, blank=True)
    ready_for_delivery = models.BooleanField(default=False)
    project_classification = models.CharField(max_length=100, default='Active Working')
    active_working_project_slug = models.SlugField(max_length=200, unique=True, default='')

    def save(self, **kwargs):
        active_working_project_slug = "%s %s %s" % (self.project_name, self.project_classification, self.user)
        unique_slugify(self, active_working_project_slug, 'active_working_project_slug')
        super(ActiveWorkingProject, self).save(**kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):

        return self.project_name


class PlannedProject(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='user')
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    list_of_functionalities = models.TextField()
    type = models.CharField(max_length=100, choices=TYPE_OF_APPS)
    price = models.IntegerField()
    working_status = models.CharField(max_length=100, choices=WORKING_STATUS, default="On Queue")
    deadline_for_production = models.DateTimeField(default=datetime.now, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    project_classification = models.CharField(max_length=100, default='Planned')
    planned_project_slug = models.SlugField(max_length=200, unique=True, default='')

    def save(self, **kwargs):
        planned_project_slug = "%s %s %s" % (self.project_name, self.project_classification, self.user)
        unique_slugify(self, planned_project_slug, 'planned_project_slug')
        super(PlannedProject, self).save(**kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):

        return self.project_name
