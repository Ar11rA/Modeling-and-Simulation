from numpy.random import normal, uniform
import matplotlib.pyplot as plt	
import matplotlib.mlab as mlab	
import math
import scipy
b=int(raw_input("Enter the limit for RNG (<10)\n"));
n=int(raw_input("How many numbers do you wish to generate?\n"));
a=13;#multiplier
c=17;#increment
x=[];
m=math.pow(2,b);
frst_val=int(raw_input("Enter seed\n"));
x.append(frst_val);
for i in range(1,n):
	x.append((a*x[i-1]+c)%m);
print "Numbers (X) generated are : \n"
for i in range(n):
	print str(i)+" element is "+str(x[i])+"\n";
r=[];
for i in range(n):
	r.append(x[i]/m);
print "Numbers (R) generated are : \n"

for i in range(n):
	print str(i)+" element is "+str(r[i])+"\n";

avg=sum(r)/(n+1);
print "average "+str(avg);
v=[];
for i in range(n):
	if(r[i]==0):
		temp=0;
	else:
		temp=((-1)*math.log(r[i]))/avg;
	v.append(temp);
print "The random variates are as follows\n";
for i in range(n):
	print str(i)+" element is "+str(v[i])+"\n";
print "\n"+str(avg*m);
 
for i in range(len(v)):
	v[i]=math.floor(v[i]);

plt.hist(v, bins=50, histtype='stepfilled',  color='b', label='Gaussian')
#plt.hist(uniform_numbers, bins=20, histtype='stepfilled', normed=True, color='r', alpha=0.5, label='Uniform')
plt.title("Histogram of RNG Data")
plt.xlabel("Random Variate")
plt.ylabel("Frequency")
plt.axis([0,30,0,(n+1)/2])
plt.show()


