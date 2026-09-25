#Question 1: Multiply all items in a list

sample_list = [2, 3, 6]
result = 1

for item in sample_list:
    result *= item

print("Result =", result)

#Question 2: Sort a list of tuples by the last element

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_list = sorted(sample_list, key=lambda x: x[-1])

print("Expected result:", sorted_list)

#Question 3: Combine two dictionaries by adding values for common keys

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = d1.copy()
for key, value in d2.items():
    result[key] = result.get(key, 0) + value

print("Expected result:", result)

#Question 4: Generate a dictionary of (i, i*i)
n = 8

result_dict = {i: i * i for i in range(1, n + 1)}

print(result_dict)

#Question 5: Sort a list of tuples by their float element (Descending)

my_list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

sorted_list = sorted(my_list, key=lambda x: float(x[1]), reverse=True)

print("Expected result:", sorted_list)

#Question 6: Create, iterate, add, and remove items in a set

my_set = {0, 1, 2, 3, 4}
print("Original set:", my_set)

print("Iterating over the set:")
for item in my_set:
    print(item)

my_set.add(5)
print("Set after adding 5:", my_set)

my_set.remove(0)
print("Set after removing 0:", my_set)
