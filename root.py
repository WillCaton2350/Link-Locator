from config.data import nums
from bot.main import parser

class node:
    def __init__(self,data=None):
        self.data = data
        self.pointer = None
    
    def activate(self):
        func = parser()
        func.get_subdomains()
        print(f'Executon: {i}')
            
class linked_list:
    def __init__(self):
        self.head: node = None
    
    def add_node(self,new_node):
        if not self.head:
            self.head = new_node
        else:
            current_node = new_node
            while current_node.pointer:
                current_node = current_node.pointer
            current_node.pointer = new_node

if __name__ == "__main__":
    instance = linked_list()
    instance.add_node(node(data=0))

    current_node = instance.head
    while current_node:
        for i in range(nums.num_nodes):
            current_node.activate()
            print(f'Node: {node} : {i}')
        current_node = current_node.pointer