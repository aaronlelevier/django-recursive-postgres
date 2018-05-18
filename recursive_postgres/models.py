import os

from django.conf import settings
from django.db import models
from django.template.loader import render_to_string


class UniDirectionalQuerySet(models.query.QuerySet):

    def in_nodes(self, pk, field):
        """
        Returns all records in the Graph that are "in-nodes"
        for the `pk` record based upon the `field`

        Args:
            pk: Django Model PrimaryKey of the record to query
            field (str): ManyToMany 'self' related field name

        Returns:
            RawQuerySet
        """
        m2m_field = self.model._meta.get_field(field)

        return self.raw(render_to_string(
            os.path.join(settings.BASE_DIR,
                         'recursive_postgres/sql/in_nodes.sql'),
            context=self._query_context(pk, field)))

    def out_nodes(self, pk, field):
        """
        Returns all records in the Graph that are "out-nodes"
        for the `pk` record based upon the `field`

        Args:
            pk: Django Model PrimaryKey of the record to query
            field (str): ManyToMany 'self' related field name

        Returns:
            RawQuerySet
        """
        return self.raw(render_to_string(
            os.path.join(settings.BASE_DIR,
                         'recursive_postgres/sql/out_nodes.sql'),
            context=self._query_context(pk, field)))

    def _query_context(self, pk, field):
        m2m_field = self.model._meta.get_field(field)
        return {
            'pk': pk,
            'db_table': self.model._meta.db_table,
            'm2m_db_table': m2m_field.m2m_db_table(),
            'm2m_column_name': m2m_field.m2m_column_name(),
            'm2m_reverse_name': m2m_field.m2m_reverse_name()
        }


class UniDirectionalManager(models.Manager):

    def get_queryset(self):
        return UniDirectionalQuerySet(self.model, using=self._db)

    def in_nodes(self, pk, field):
        return self.get_queryset().in_nodes(pk, field)

    def out_nodes(self, pk, field):
        return self.get_queryset().out_nodes(pk, field)
