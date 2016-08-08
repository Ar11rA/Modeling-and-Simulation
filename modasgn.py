import matplotlib	
import math
m=int(raw_input("Enter the limit for RNG\n"));
n=int(raw_input("How many numbers do you wish to generate?\n"));
a=13;#multiplier
c=17;#increment
x=[];
frst_val=int(raw_input("Enter seed\n"));
x.append(frst_val);
for i in range(1,n):
	x.append((a*x[i-1]+c)%m);
print "Numbers generated are : \n"
for i in range(1,n):
	print str(i)+" element is "+str(x[i])+"\n";

