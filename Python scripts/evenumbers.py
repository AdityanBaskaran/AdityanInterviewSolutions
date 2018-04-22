listlength = int(input('Enter the length of the list ...  '))
numlist = []
for x in range(listlength):
    number = int(input('Please enter a number: '))
    numlist.append(number)

numlist.sort()
def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print (is_even_num(numlist))
print (is_even_num(numlist))
