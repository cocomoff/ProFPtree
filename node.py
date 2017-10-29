# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, item=None, parent=None, node_link=None):
        self.item = item
        self.count = 0
        self.uft = []
        self.ufp = []
        self.parent = parent
        self.node_link = node_link
        self.children = []

    def __str__(self):
        pitem = "-" if self.parent is None else self.parent.item
        return "N[{},{},{},{}:P={}]".format(self.item, self.count, self.uft, self.ufp, pitem)

    def increment(self):
        self.count = self.count + 1

    def add_child(self, node):
        self.children.append(node)

    def find_child(self, key):
        for cnode in self.children:
            if cnode.item == key:
                return (True, cnode)
        return (False, None)
