from django.test import TestCase, override_settings
from recursive_postgres.models import UniDirectionalManager

from .models import Node


@override_settings(ROOT_URLCONF=__name__)
class UniDirectionalManagerTests(TestCase):

    def setUp(self):
        """
        Diagram of graph structure being tested

        All flows are directed downwards

        a     b
         \   /
          \ / 
           c     d
            \   /
             \ /
              e
             / \
            /   \
           f     g
                / \
               /   \
              h     i

        """
        self.a = Node.objects.create(name='a')
        self.b = Node.objects.create(name='b')
        self.c = Node.objects.create(name='c')
        self.d = Node.objects.create(name='d')
        self.e = Node.objects.create(name='e')
        self.f = Node.objects.create(name='f')
        self.g = Node.objects.create(name='g')
        self.h = Node.objects.create(name='h')
        self.i = Node.objects.create(name='i')

        # relationships
        # a
        self.a.children.add(self.c)
        # b
        self.b.children.add(self.c)
        # c
        self.c.children.add(self.e)
        # d
        self.d.children.add(self.e)
        # e
        self.e.children.set([self.f, self.g])
        # g
        self.g.children.set([self.h, self.i])

    def test_setup_using_orm(self):
        nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        for n in nodes:
            self.assertIsInstance(getattr(self, n, None), Node)

        self.assertEqual(Node.objects.count(), len(nodes))

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

    def test_in_nodes(self):
        ret = self.e.children.in_nodes()

        for node in [self.f, self.g, self.h, self.i]:
            self.assertIn(node, ret)



