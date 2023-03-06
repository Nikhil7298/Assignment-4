nums = input("Enter the list : ").split(',')
nums = list(map(int,numbers))
def triple_num(b):
    return b*3
print((map(triple_num,nums)))
