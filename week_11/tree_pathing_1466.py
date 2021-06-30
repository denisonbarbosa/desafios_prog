import queue

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)


def tree_pathing():
    cases = int(input())
    
    i = 1
    while (i <= cases):
        size = int(input())
        entry = list(map(int, input().split()))
        
        root = Node(entry[0])
        
        for n in range(1, size):
            root.insert(entry[n])
        
        print_queue = queue.SimpleQueue()    
        
        answer = f'{root.value}'
        
        if root.left is not None:
            print_queue.put(root.left)
        if root.right is not None:
            print_queue.put(root.right)
        
        while not print_queue.empty():
            aux = print_queue.get()
            answer += f' {aux.value}'
            if aux.left is not None:
                print_queue.put(aux.left)
            if aux.right is not None:
                print_queue.put(aux.right)
        answer += '\n'    
        
        print(f'Case {i}:')
        print(answer)
        i += 1


if __name__ == '__main__':
    tree_pathing()
