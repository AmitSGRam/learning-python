def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

#count_words(filename='/run/media/amit/New Volume/lin/python/Files/Exceptions/alice.txt')
filenames = ['Files/Exceptions/alice.txt', 'Files/Exceptions/siddhartha.txt', 'Files/Exceptions/moby_dick.txt','little_women.txt  ']
for filename in filenames:
    count_words(filename)