import unittest


class Node:
    def __init__(self, x: int, next_: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next_ = next_
        self.random = random

    def __iter__(self):
        yield self

        next_node = self.next_
        while next_node:
            yield next_node
            next_node = next_node.next_

    @staticmethod
    def head_to_repr(head: 'Node') -> str:
        id_to_index = {}

        next_node = head
        index = 0
        while next_node:
            id_to_index[id(next_node)] = index
            index += 1
            next_node = next_node.next_

        return str([
            [node.val, id_to_index[id(node.random)] if node.random else None]
            for node in head
        ]).replace('None', 'null')


class Solution:
    def copyRandomList(self, head: Node) -> Node:

        items_identity_map = {}
        current_node = head

        previous_node_copy = Node(0)

        while current_node:
            current_node_copy = items_identity_map.get(id(current_node))

            if not current_node_copy:
                current_node_copy = Node(current_node.val)
                items_identity_map[id(current_node)] = current_node_copy

            previous_node_copy.next_ = current_node_copy

            if current_node.random:
                current_node_copy.random = items_identity_map.get(id(current_node.random))
                if not current_node_copy.random:
                    current_node_copy.random = Node(current_node.random.val)
                    items_identity_map[id(current_node.random)] = current_node_copy.random

            if not current_node.next_:
                break

            current_node = current_node.next_
            previous_node_copy = current_node_copy

        return items_identity_map[(id(head))]


class MainTest(unittest.TestCase):

    @staticmethod
    def assemble_nodes(nodes_n_randoms):

        node = None
        previous_node = None

        for i in range(len(nodes_n_randoms)-1, -1, -1):
            node, random = nodes_n_randoms[i]
            node.next_ = previous_node
            previous_node = node

            if random is not None:
                node.random = nodes_n_randoms[random][0]

        return node

    def test_repr(self):
        nodes_n_randoms = [
            (Node(7, ), None),
            (Node(13, ), 0),
            (Node(11, ), 4),
            (Node(10, ), 2),
            (Node(1, ), 0),
        ]

        head = self.assemble_nodes(nodes_n_randoms)

        self.assertEqual(
            '[[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]',
            Node.head_to_repr(head)
        )

    def test_1(self):
        nodes_n_randoms = [
            (Node(7, None), None),
            (Node(13, None), 0),
            (Node(11, None), 4),
            (Node(10, None), 2),
            (Node(1, None), 0),
        ]

        head = self.assemble_nodes(nodes_n_randoms)
        head_copy = Solution().copyRandomList(head)
        self.assertEqual(
            '[[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]',
            Node.head_to_repr(head_copy)
        )


if __name__ == '__main__':
    unittest.main()
