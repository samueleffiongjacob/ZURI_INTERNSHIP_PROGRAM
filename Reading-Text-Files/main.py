# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from collections import Counter

print('--------------------RAW STORY WITHOUT ANY MORDIFICATION-----------------------------------')


def read_file_content(filename="./story.txt"):
    f = open("./story.txt", "r")
    print(f.read())

    return "Hello World"


read_file_content()
print('------------------------ End Raw story---------------------------------')
print('------------------------------------------------------------------------')

print('COUNT THE WORDS IN THE STORY')

print('--------------------------------------------------------------')


def count_word(file_name="./story.txt"):
    with open("./story.txt") as f:
        return Counter(f.read().split())


print("Frequency :", count_word("./story.txt"))
print('-------------------------------------------------------------------------------------------------------------')

print('------------------------ COUNT THE WORDS IN THE STORY Ends Here ---------------------------------------------')

