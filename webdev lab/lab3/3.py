from collections import Counter

def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def count_words(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts

def print_top_words(word_counts, top_n=10):
    sorted_word_counts = word_counts.most_common(top_n)
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

def main():
    file_path = input("Enter the path to the text file: ")
    text = read_file(file_path)
    word_counts = count_words(text)
    print_top_words(word_counts)

if __name__ == "__main__":
    main()
