filename = raw_input( "provide complete path of the numbers file....  " )
with open(filename) as my_file:
    numbers = my_file.readlines()
print numbers
nummap = {}
numsort = []
numbers = [x.strip() for x in numbers]
numbers = [ int(x) for x in numbers ]
print numbers
for x in range(len(numbers)):
    nummap[numbers[x]] = numbers.count(numbers[x])
for key,value in sorted(nummap.iteritems(), key =lambda(k,v): (v,k), reverse = True):
    print "%d %d" %(value,key)
