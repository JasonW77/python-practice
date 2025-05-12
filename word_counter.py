def count_words(text):
    # Remove punctuation for cleaner word counting
    for char in "-.,\n":
        text = text.replace(char, " ")
    text = text.lower()

    words = text.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return words, word_count

def main():
    print("Enter a paragraph of text:")
    user_input = input("> ")

    words, word_count = count_words(user_input)

    print(f"\nTotal words: {len(words)}")
    print("Word frequencies:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()