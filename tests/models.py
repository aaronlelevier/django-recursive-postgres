from django.db import models

from recursive_postgres.models import UniDirectionalManager


class AbastractTestModel(models.Model):
    """
    Base for test models that sets app_label, so they play nicely.
    """
    class Meta:
        app_label = 'tests'
        abstract = True


class Node(AbastractTestModel):
    name = models.CharField(max_length=50)
    children = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='parents')

    objects = UniDirectionalManager()

    def __str__(self):
        return self.name
