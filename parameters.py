# def a_function(string):
#     return len(string)
# print("length of the string is :",a_function("rameshwaram"))
# print("length of the string python is:",a_function("python"))


def square(item_list):
    squares=[]
    for l in item_list:
        squares.append(l**2)
    return squares
my_list=[10,20,30];
print(square(my_list))