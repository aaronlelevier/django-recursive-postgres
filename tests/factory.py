from .models import Node


def create_unidirectional_nodes():
    """
    Returns a dictionary of related unidirectional nodes, where
    the key is the `Node.name` and the value is the `Node instance`

    Diagram of graph structure

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
    a = Node.objects.create(name='a')
    b = Node.objects.create(name='b')
    c = Node.objects.create(name='c')
    d = Node.objects.create(name='d')
    e = Node.objects.create(name='e')
    f = Node.objects.create(name='f')
    g = Node.objects.create(name='g')
    h = Node.objects.create(name='h')
    i = Node.objects.create(name='i')

    # relationships
    # a
    a.children.add(c)
    # b
    b.children.add(c)
    # c
    c.children.add(e)
    # d
    d.children.add(e)
    # e
    e.children.set([f, g])
    # g
    g.children.set([h, i])

    return {n.name: n for n in Node.objects.all()}
