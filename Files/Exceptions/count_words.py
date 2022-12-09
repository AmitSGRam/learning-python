def count_words(filename, word):

    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.read()
    except FileNotFoundError:
            print('File is not found')
    else:
        count = lines.count(word)
        print(f'Number of times the word \'{word}\' appears in {filename.split("/")[2]}: {count}')

filename = 'Files/Exceptions/The_Old_Town.txt'
count_words(filename,'the')
count_words(filename,'the ')