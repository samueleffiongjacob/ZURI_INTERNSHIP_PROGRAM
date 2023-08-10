# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

print (' --------------  Anagrams  ---------------------------')

def find_anagrams(first_string,second_string):
    if sorted(first_string) == sorted(second_string):
        return True
    else:
        return False

print('--------------FIRST WORD anagrams -------------------')
print('--------------------------------------------------------')
first_string = input("Provide the first string: ")
print('------------------------------------------')
second_string = input("Provide the second string: ")
print('----------------------------------------------')


find_anagrams(first_string, second_string)
print(find_anagrams('python1','yptho1n'))

print('-------------------- sECOND WORD anagrams--------------------------')


def find_anagrams(first_string, second_string):
    if sorted(first_string) > sorted(second_string):
        return True
    else:
        return False

print('------------------------------')
first_string = str(input("Provide the first string: "))
print('------------------------------')
second_string = str(input("Provide the second string: "))
print('------------------------------')


find_anagrams(first_string, second_string)
print(find_anagrams('effiong','gffione'))
print('---------------------- End -----------------------')
