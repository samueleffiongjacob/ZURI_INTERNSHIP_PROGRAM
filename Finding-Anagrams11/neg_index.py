# POSITIVE INDEXING
z = [56, 3, 7, 4, 2]
print('----------------------------------------------------------------')
print('printing z values')
print(z)
print('----------------------------------------------------------------')
print('POSITIVE INDEXING')
print(z[4])
print('----------------------------------------------------------------')

# sorting check the defination down in line 36
print('sorting positive index')
z.sort()
print(z)
print('----------------------------------------------------------------')

# NEGATIVE INDEXING
print('NEGATIVE INDEXING')
z = [56, 3, 7, 4, 2]
print(z[-5])
print('----------------------------------------------------------------')


# TO VIEW THING IN DECENDING OTHER  ":"
print('TO VIEW THING IN DECENDING OTHER `:` ')
z = [56, 3, 7, 4, 2]
print(z[:-1])
print('----------------------------------------------------------------')

# TO VIEW THING IN ACENDING OTHER  ":"
z = [56, 3, 7, 4, 2]
print('TO VIEW THING IN ACENDING OTHER `:` ')
print(z[0:])
print('----------------------------------------------------------------')

# UPDATING LIST OR TUPLE
print('UPDATING LIST OR TUPLE')
z[3] = 'samuel'
print(z)
print('----------------------------------------------------------------')

# List Methods
# Index Method
print('List Methods and Index Method `S`')
S = [4, 1, 5, 4, 10, 4]
print(S)
print('----------------------------------------------------------------')
# sorting check the defination down in line 36
print('sorting S')
S.sort()
print(S)
print('----------------------------------------------------------------')
# The index method returns the positive first index at which a value occurs.In the code below,
# ## it will return 0.
print('The index method returns the positive first index at which a value occurs.In the code below,it will return 0')
print(S.index(4))
print('----------------------------------------------------------------')

# Count Method
# The count method works just like how it sounds. It counts the number of times a value occurs in a list
print('Count Method')
print('----------------------------------------------------------------')
print('The count method works just like how it sounds. It counts the number of times a value occurs in a list')
print('----------------------------------------------------------------')
random_list = [4, 1, 5, 4, 10, 4]
print(random_list)
print('----------------------------------------------------------------')
print('noqw using the count function')
print(random_list.count(5))
print('----------------------------------------------------------------')

# Sort Method
# The sort method sorts and alters the original list in place.
print('Sort Method')
print('----------------------------------------------------------------')
print('The sort method sorts and alters the original list in place.')
e = [3, 7, 4, 2]
print('printing variabl e')
print(e)
print('----------------------------------------------------------------')
print('now print the sort function')
e.sort()
print(e)
print('----------------------------------------------------------------')

# The code above sorts a list from low to high. The code below shows that you can also sort a list from high to low.
print('The code above sorts a list from low to high. The code below shows that you can also sort a list from high to low.')
# Sorting and Altering original list
# high to low
e.sort(reverse=True)
print(e)
print('----------------------------------------------------------------')

# Append Method
q = [7, 4, 3, 2]
print('printing q')
print(q)
print('----------------------------------------------------------------')
print('printing the append function')
q.append(3)
print(q)
print('----------------------------------------------------------------')

# The remove method removes the first occurrence of a value in a list.
print('The remove method removes the first occurrence of a value in a list. in q ')
q = [7, 4, 3, 2, 3]
print(q)
print('----------------------------------------------------------------')
print('now using the remove function')
q.remove(2)
print(q)
print('----------------------------------------------------------------')

# Pop Method
# The pop method removes an item at the index you provide. This method will also return
# the item you removed from the list. If you don’t provide an index, it will by default remove the item at the last index.
print('pop Method')
w = [7, 4, 3, 3]
print(w.pop(1))
print(w)
print('----------------------------------------------------------------')

# Extend Method
# The method extends a list by appending items. The benefit of this is you can add lists together.
d = [7, 3, 3]
d.extend([4, 5])
print('EXTENDED method')
print(d)
print('----------------------------------------------------------------')

# Alternatively, the same thing could be accomplished by using the + operator.
print(' Alternatively, the same thing could be accomplished by using the + operator.')
print([1, 2] + [3, 4])
print('----------------------------------------------------------------')

# Insert Method
# The insert method inserts an item before the index you provide
print('INSERT METHOD')
z = [7, 3, 3, 4, 5]
z.insert(4, [1, 2])
print(z)
print('----------------------------------------------------------------')
