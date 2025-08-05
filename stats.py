def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    characters= text.lower()

    letters = {}

    for c in characters:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1

    return letters

def sorted_list(input):
    dictionary_list = []
    for i in input:
        number = input[i]
        dictionary_list.append({"char" : i, "num" : (number)})
    return dictionary_list

def sort_on(input):
    return input["num"]


