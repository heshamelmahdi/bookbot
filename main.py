def main():
    path = "books/frankenstein.txt"
    text = get_file_contents(path)
    num_words = count_words(text)
    character_count = count_characters(text)
    print_report(path, num_words, character_count)


def print_report(path, num_words, character_count):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    for char in character_count:
        print(f"The '{char}' character was found {character_count[char]} times")
    print("-- End report ---")


def get_file_contents(path):
    with open(path) as f:
        text = f.read()
        return text


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lower_text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = {}
    for letter in alphabet:
        num_occure = lower_text.count(letter)
        count[letter] = num_occure

    return count


main()
