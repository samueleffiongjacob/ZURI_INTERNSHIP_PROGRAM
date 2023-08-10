def anagram_checker(first_value, second_value):
    if sorted(first_string) == sorted(second_string):
        print("The two strings are anagrams of each other.")
    else:
        print("The two strings are not anagrams of each other.") 

first_string = input("Provide the first string: ")
second_string = input("Provide the second string: ")
anagram_checker(first_string, second_string) 


print('-------------------------------------------------------------------------------------------------------')
words = ['enif', 'ollhe', 'aivrre', 'gdo', 'atc', 'neif'] 
def anagram_checker(value, words):
    anagrams = []

    for word in words:
        if sorted(word) == sorted(value):
            anagrams.append(word)

    return anagrams 

print(anagram_checker('hello', words))

print('----------------------------------------------------------------------------------')


a = str(input("Enter string 1:"))

b = str(input("Enter string 2:"))

count = 0

for i in a:

    for j in b:

        if i == j:

            count = count+1

if count == len(a):

    print("Strings are anagram of each other.")

else:
    print("Strings are not anagram of each other.")

