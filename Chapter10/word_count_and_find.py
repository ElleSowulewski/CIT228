def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def find_words(search, filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.lower()
        search = search.lower()
        words = contents.count(search)
        print(f"The file {filename} has the word '{search}'' {words} times.")


filenames = ['Chapter10/WSD_quote.txt', 'Chapter10/WSD_quote2.txt', 'Chapter10/WSD_quote3.txt']
for filename in filenames:
    count_words(filename)
print()

answer = input("What word would you like to search for?")
for filename in filenames:
    find_words(answer, filename)