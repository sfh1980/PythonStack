#range(start, stop, step)
#start defaults at zero and exits at number provided
#stop begins at start number and exits at index of stop number provided
#step increases by provided integer until reaching index of stop integer
#for i in range(x, x, x)
    #print(i)



#BASIC
for i in range(150):
    print(i)

#Multiples of Five
for i in range(5, 1000, 5):
    print(i)

#Counting, the Dojo Way -  Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1,101,1):
    print(i)
    if i % 10 == 0:
        print("coding dojo")
    elif i % 5 == 0:
        print("coding")
        

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
min = 0
max = 500000
Oddtotal = 0

for i in range(0, 500001):
    if(i % 2 !=0):
        #print('{0}'.format(i))
        Oddtotal = Oddtotal + i
print("final sum from 0 to {0}={1}".format(i, Oddtotal))


#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for i in range(2018, 0, -4):
    print(i)


#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 10
mult = 3

for i in range (lowNum, highNum):
        if i % mult == 0:
            print (i)

