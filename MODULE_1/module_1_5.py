immutable_var = (8, 5.025, 'hello', True, [1, 2, 3])
print(immutable_var)

# mutable_var[2] = 'bye' - error

mutable_list = [1, 2, 3, 4, 5]
mutable_list[2] = 10
mutable_list[0] = 3
mutable_list[-1] = 5.9
print(mutable_list)