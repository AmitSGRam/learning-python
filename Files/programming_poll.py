filename = 'Files/programming_poll.txt'

answer_list = []

while True:
    question1 = input('Why do you like programming?\n')
    answer_list.append(question1)

    question2 = input('Would you like for someone else to answer? (y/n)\n')
    if question1.lower() == 'n':
        break

    if question2.lower() == 'n':
        break
    

with open(filename, 'a') as file_object:
    for line in answer_list:
        file_object.write(f'{line}\n')