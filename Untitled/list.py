import random

class Storage:

    def __init__(self):
        self.set1 = set()
        self.list1 = []
    
    def insert_value(self,user_input1):
        if user_input1 not in self.list1:
            self.list1.append(user_input1)
    
    def remove_value(self,user_input2):
        if user_input2 in self.list1:
            self.list1.remove(user_input2)

    def get_random_value(self):
        print(random.choice(self.list1))

call1 = Storage()
value_list = ['banana1', 'banana1', 'mango2', 'honey3', 'apple4']
print(len(value_list))
for value in value_list:
    call1.insert_value(value)
print(call1.list1)
print(len(call1.list1))

call1.remove_value('banana1')
print(call1.list1)

call1.get_random_value()