from django.db import models


class UniDirectionalQuerySet(models.query.QuerySet):

    def in_nodes(self):
        return self.all()


class UniDirectionalManager(models.Manager):

    def get_queryset(self):
        return UniDirectionalQuerySet(self.model, using=self._db)

    def in_nodes(self):
        return self.get_queryset().in_nodes()
