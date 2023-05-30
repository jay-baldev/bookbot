def count_words(input_string):
    words = input_string.split()
    return len(words)

def count_letters(input_string):
    input_string = input_string.lower()
    dict = {}
    count = 0
    for i in range(0, len(input_string)):
        if input_string[i] not in dict:
            dict[input_string[i]] = 0
        dict[input_string[i]] = dict[input_string[i]] + 1
    return dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print("")
    letter_dict = count_letters(file_contents)
    letter_list = [(key, value) for key, value in letter_dict.items()]
    letter_list.sort(key = lambda x: x[1], reverse = True)
    for letter_tupple in letter_list:
        if letter_tupple[0].isalpha():
            print(f"The '{letter_tupple[0]}' character was found {letter_tupple[1]} times")


main()