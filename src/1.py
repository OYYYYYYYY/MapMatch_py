import random
a = 76
b = int(a * 0.1)
# c = int(b)
print("result is ", b)
array = [0] * 5
num_nnz = 5
for i in range(5):
    array[i] = i
    print(array[i])
print(array)
num_to_remove = 3
data_to_remove = random.sample(array, num_to_remove)
new_index = [x for x in array if x not in data_to_remove]
print(new_index)