# -*- coding: utf-8 -*-
#
# implementation main
#

from node import Node


class ProFPtree(object):
    def __init__(self, db):
        self.db = db
        self.root = Node()
        self.item_header_table = {}
        self.uitem_lookup_table = []
        self.construct()

    def __str__(self):
        return "NotImplemetedRepresentation [...]"

    def construct(self):
        for idx, trans in enumerate(self.db):
            self.insert_transaction(trans, idx, self.root, True)

        print(self.root)
        for c in self.root.children:
            print("  ", c)
            for cc in c.children:
                print("    ", cc)
                for ccc in cc.children:
                    print("      ", ccc)
                    for cccc in ccc.children:
                        print("        ", cccc)

        for key in self.item_header_table:
            print("key:", key)
            node = self.item_header_table[key]
            while node is not None:
                print(" node:", node)
                node = node.node_link

    def insert_transaction(self, trans, i, node, u_flag):
        # print(trans)
        for it in trans:
            flag, N = node.find_child(it.Item())
            if flag:
                # print("found", N)
                u_flag = self.update_node_entries(it, i, N, u_flag)
            else:
                # build new child
                N = Node(item=it.Item(), parent=node)
                node.add_child(N)
                u_flag = self.update_node_entries(it, i, N, u_flag)
                if it.Item() not in self.item_header_table:
                    self.item_header_table[it.Item()] = N
                else:
                    # update link list
                    # ntp = self.item_header_table[it.Item()]
                    # while ntp.node_link != None:
                    #    ntp = ntp.node_link
                    # ntp.node_link = N
                    N.node_link = self.item_header_table[it.Item()]
                    self.item_header_table[it.Item()] = N

            # uncertain data
            if it.P() < 1.0:
                self.uitem_lookup_table.append((i, it))
            node = N

    def update_node_entries(self, it, i, node, u_flag):
        if it.P() == 1.0:
            if u_flag:
                node.increment()
            else:
                node.ufp.append(i)
        else:
            node.uft.append(i)
            u_flag = False
        return u_flag
