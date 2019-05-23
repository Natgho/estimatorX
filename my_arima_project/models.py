from django.db import models
from django.contrib.postgres.fields import JSONField


class SpecialData(models.Model):
    task_name = models.CharField(max_length=200)
    raw_data = JSONField()

    def __str__(self):
        return self.task_name
