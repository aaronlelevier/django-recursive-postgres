from django.test import TestCase

from . import factory
from .models import Node


class FactoryTests(TestCase):

    def test_create_unidirectional_nodes(self):
        nodes_dict = factory.create_unidirectional_nodes()
        for k,v in nodes_dict.items():
            setattr(self, k, v)

        self.assertEqual(Node.objects.count(), len(nodes_dict))

        # a
        self.assertEqual(self.a.children.count(), 1)
        self.assertEqual(self.a.children.first(), self.c)
        # b
        self.assertEqual(self.b.children.count(), 1)
        self.assertEqual(self.b.children.first(), self.c)
        # c
        self.assertEqual(self.c.children.count(), 1)
        self.assertEqual(self.c.children.first(), self.e)
        # d
        self.assertEqual(self.d.children.count(), 1)
        self.assertEqual(self.d.children.first(), self.e)
        # e
        self.assertEqual(self.e.children.count(), 2)
        self.assertIn(self.f, self.e.children.all())
        self.assertIn(self.g, self.e.children.all())
        # f
        self.assertEqual(self.f.children.count(), 0)
        # g
        self.assertEqual(self.g.children.count(), 2)
        self.assertIn(self.h, self.g.children.all())
        self.assertIn(self.i, self.g.children.all())
        # h
        self.assertEqual(self.h.children.count(), 0)
        # i
        self.assertEqual(self.i.children.count(), 0)
