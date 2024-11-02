from models.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        if self.head is None:
            return
        # перший крок - це те значення що збережене в голові
        previous_node = self.head
        
        # дії для голови, зберегти вказівник, і затерти його
        current_node = previous_node.next
        previous_node.next = None
        
        # для кожної ноди: 
        while current_node is not None:
            # зберегти її вказівник
            next_node = current_node.next
            # замінити вказівник на попередню ноду
            current_node.next = previous_node

            # поточна стає попереднью
            previous_node = current_node
            # наступна нода стає поточною
            current_node = next_node

        # коли вже current_node is None, то значить попередня була останньою, фіксуємо голову
        self.head = previous_node

    def find_middle(self) -> None | Node:
        if self.head is None:
            return None

        # Перевіряємо, якщо список має тільки два елементи
        if self.head.next is not None and self.head.next.next is None:
            return self.head

        slow = self.head  # Повільний вказівник
        fast = self.head  # Швидкий вказівник

        # Швидкий вказівник рухається на два кроки, а повільний - на один
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    @staticmethod
    def merge_sorted(left, right):
        result_list = LinkedList()
        # Дозволяє тримати останню ноду, з якою ми працюємо, для швидшої вставки наступної
        result_last = None
        current_left = left.head
        current_right = right.head

        # функція для вставки ноди
        def insert_node(current_node, result_last):
            # зберігаємо вказівник наступної ноди
            next_node = current_node.next

            # випадок для самої першої ноди
            if result_list.head is None:
                result_list.head = current_node
            
            # якщо не перша, то примаємо останню ноду, і відразу працюємо з нею
            else:
                result_last.next = current_node
            
            # оновлюємо останню ноду
            result_last = current_node

            # затираємо вказівник для тільки що вставленої ноди, вона в новому списку остання
            current_node.next = None
            # замінюємо ноду для подальшої роботи в циклі
            current_node = next_node

            return current_node, result_last

        while current_left is not None and current_right is not None:
            if current_left.data <= current_right.data:
                current_left, result_last = insert_node(current_left, result_last)
            else:
                current_right, result_last = insert_node(current_right, result_last)

        while current_left is not None:
            current_left, result_last = insert_node(current_left, result_last)

        while current_right is not None:
            current_right, result_last = insert_node(current_right, result_last)

        return result_list
    
    def sort(self):
        # якщо пустий, або з одним значенням - відразу повертаємо
        if self.head is None or self.head.next is None:
            return self
        
        # інакше ділимо список на два
        middle_node = self.find_middle()

        # другу половину списку офорлюємо в окремий список
        right_list = LinkedList()
        right_list.head = middle_node.next
        middle_node.next = None

        # кожен отриманий список треба відправити на сортування
        left_sorted = self.sort()
        right_sorted = right_list.sort()
        
        # повертаємо зʼєднаний, відсортований список
        return LinkedList.merge_sorted(left_sorted, right_sorted)
