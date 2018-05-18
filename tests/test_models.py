from django.test import TestCase, override_settings
from recursive_postgres.models import UniDirectionalManager

from . import factory
from .models import Node


@override_settings(ROOT_URLCONF=__name__)
class UniDirectionalManagerTests(TestCase):

    def setUp(self):
        nodes_dict = factory.create_unidirectional_nodes()
        for k,v in nodes_dict.items():
            setattr(self, k, v)

    def test_in_nodes(self):
        raw_queryset = Node.objects.in_nodes(pk=self.e.pk, field='children')
        nodes = [x for x in raw_queryset]

        for node in [self.a, self.b, self.c, self.d]:
            self.assertIn(node, nodes)

        # test attrs returned by the query - pick Node "a" to test
        node = Node.objects.get(id=self.a.id)

        # NOTE: even though the raw SQL query only returns IDs, once
        # in memory, the whole Django Model instance is present
        self.assertEqual(node.name, self.a.name)

    def test_out_nodes(self):
        raw_queryset = Node.objects.out_nodes(pk=self.e.pk, field='children')
        nodes = [x for x in raw_queryset]

        for node in [self.f, self.g, self.h, self.i]:
            self.assertIn(node, nodes)
