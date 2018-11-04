from django.db import models

# Create your models here.
class CourseOrg(models.Model):
    name = models.CharField('机构名称',max_length=50)