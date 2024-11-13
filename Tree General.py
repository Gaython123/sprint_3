class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_tree():
    root = TreeNode('Назар трахер полюбляє:')

    girls_type_1 = TreeNode('шатенки')

    girls_type_1.add_child(TreeNode("Діана"))
    girls_type_1.add_child(TreeNode("Аня"))
    girls_type_1.add_child(TreeNode("Юля"))

    girls_type_2 = TreeNode('блондинки')

    girls_type_2.add_child(TreeNode("Анна-Марія"))
    girls_type_2.add_child(TreeNode("Марта"))
    girls_type_2.add_child(TreeNode("Алла Михайлівна"))

    girls_type_3 = TreeNode('РИЖІ')

    girls_type_3.add_child(TreeNode("Аня"))
    girls_type_3.add_child(TreeNode("Сидор"))
    girls_type_3.add_child(TreeNode("жираф"))

    men_type = TreeNode('довгочленні')

    men_type.add_child(TreeNode('Максим'))
    men_type.add_child(TreeNode('Лесик'))
    men_type.add_child(TreeNode('Портников'))

    root.add_child(girls_type_1)
    root.add_child(girls_type_2)
    root.add_child(girls_type_3)
    root.add_child(men_type)

    #не можна писати add_child(TreeNode())
    # якщо обєкт child уже був оголошений як TreeNode
    #root.add_child(TreeNode(men_type)) - TreeNode лишній бо уже
    #men_type = TreeNode('довгочленні')

    root.print_tree()

build_tree()