filename = raw_input( "provide complete path of the delimited file....  " )
with open(filename) as my_file:
    line = my_file.readlines()
line = [x.strip() for x in line]
count = line[0].count('|')
print ' the column count is %s ' %count
for x in range(5):
    with open('tabdelimitedoutput.txt', 'a') as the_file:
        the_file.write(line[x].replace('|','\t')+'\n')