# Напишіть алгоритм (функцію), який знаходить найменше значення у двійковому дереві пошуку або в AVL-дереві. 
# Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

# Код виконується, і функція знаходить найменше значення в дереві.

# двійкове дерево пошуку
from visual_tree import animate_traversal_avl
class Node(object):  # Вузли в дереві
    def __init__(self, data):
        self.data = data  # Вхідні дані
        self.left_child = None  # Лівий нащадок
        self.right_child = None  # Правий нащадок


# Операції на двійковому дереві пошуку
class BinarySearchTree(object):
    def __init__(self):
        self.root = None  # Ініціалізувати корінь як пустий

    # ------------------------- Додавання нового вузла до двійкового дерева пошуку ----------------------------
    # Додати елемент до BST
    def insert(self, data):
        if not self.root:  # Якщо корінь пустий, це перший елемент
            print(f'Вузол {data} був вставлений')
            self.root = Node(data)  # Створити новий вузол дерева
        else:
            self.insert_node(data, self.root)  # Якщо корінь існує, додати новий вузол

    # Додати новий вузол
    # Складність O(log N) якщо дерево збалансоване
    def insert_node(self, data, node):
        # Якщо нові дані менші за дані кореня
        if data < node.data:  # Якщо новий елемент менший за дані поточного вузла
            if node.left_child:  # Якщо поточний вузол[A] має лівого нащадка [B], то
                self.insert_node(data, node.left_child)  # Додати новий вузол зліва від [B]
            else:
                print(f'Вузол {data} був вставлений')
                node.left_child = Node(data)  # Якщо немає лівого нащадка у [A], створити новий вузол зліва від нього

        # Якщо нові дані більші за дані кореня
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                print(f'Вузол {data} був вставлений')
                node.right_child = Node(data)

    # -------------------------- Отримати мінімальне значення у двоїчному дереві пошуку ---------------------------------
    # Отримати мінімальне значення у двоїчному дереві пошуку
    # Ліве найвіддаленіше значення є найменшим значенням
    def get_min_value(self):
        if self.root:  # Якщо дерево не пусте
            return self.get_min(self.root)  # Перейти до функції getMin

    # Пройти до лівого найвіддаленішого вузла (найменше значення)
    def get_min(self, node):  # Почати проходити від кореня
        if node.left_child:  # Якщо лівий нащадок існує, продовжувати йти поки не досягнемо "NONE"
            return self.get_min(node.left_child)
        return node.data  # Коли ми досягнемо None, отримаємо лівий найвіддаленіший вузол і повернемо його дані
    
    # ------------------------------ Обхід двоїчного дерева пошуку --------------------------------------
    # Пройти через двоїчне дерево пошуку

    def traversal(self, path):
        if self.root:
            self.pre_order_traversal(self.root, path)

    def pre_order_traversal(self, node, path):
        if node:
            path.append(node)
            self.pre_order_traversal(node.left_child, path)
            self.pre_order_traversal(node.right_child, path)


    def display(self, traversal_type=None):
        if traversal_type:
            animate_traversal_avl(self.root, lambda node, path: self.pre_order_traversal(node, path), traversal_type)
        else:
            animate_traversal_avl(self.root, lambda node, path: self.pre_order_traversal(node, path))

# -------------------- Тестування -----------------------
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)  # Корінь
    bst.insert(13)
    bst.insert(14)
    bst.insert(12)
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(8)
    bst.insert(1)
    bst.display()
    found_min_value = bst.get_min_value()
    if found_min_value:
        print(f"Мінімальне значення з числом {found_min_value} знайдено.")
    else:
        print("Значення відсутні у дереві. Додайте значення до дерева.")