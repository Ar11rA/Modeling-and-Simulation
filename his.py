from numpy.random import normal, uniform, randint , exponential, poisson
import math
import matplotlib.pyplot as plt	


choice=randint(1,4);
print choice;
if choice==1:
	o=exponential(0.5,100);
elif choice==2:
	o=[];
	a=poisson(10,100);
	m=max(a);
	for i in range(len(a)):
		o.append(float(a[i])/float(m));
else:
	o=uniform(0.0,1.0,100);


f1=0;f2=0;f3=0;f4=0;f5=0;f6=0;f7=0;f8=0;f9=0;f10=0;
for i in range(len(o)):
	if o[i]>=0.0 and o[i]<0.1:
		f1+=1;
	elif o[i]>=0.1 and o[i]<0.2:
		f2+=1;
	elif o[i]>=0.2 and o[i]<0.3:
		f3+=1;
	elif o[i]>=0.3 and o[i]<0.4:
		f4+=1;
	elif o[i]>=0.4 and o[i]<0.5:
		f5+=1;
	elif o[i]>=0.5 and o[i]<0.6:
		f6+=1;
	elif o[i]>=0.6 and o[i]<0.7:
		f7+=1;
	elif o[i]>=0.7 and o[i]<0.8:
		f8+=1;
	elif o[i]>=0.8 and o[i]<0.9:
		f9+=1;
	else:
		f10+=1;

print "1 "+str(f1);
print "2 "+str(f2);
print "3 "+str(f3);
print "4 "+str(f4);
print "5 "+str(f5);
print "6 "+str(f6);
print "7 "+str(f7);
print "8 "+str(f8);
print "9 "+str(f9);
print "10 "+str(f10);
obsrvd=[];
obsrvd.append(f1);
obsrvd.append(f2);
obsrvd.append(f3);
obsrvd.append(f4);
obsrvd.append(f5);
obsrvd.append(f6);
obsrvd.append(f7);
obsrvd.append(f8);
obsrvd.append(f9);
obsrvd.append(f10);

expctd=[]
#poisson
j=0;
while j<10:
	ex=2.71828;
	alpha=3.64;
	k=math.pow(ex,(-1*alpha));
	k1=math.pow(alpha,j);
	k2=math.factorial(j);
	k3=(100*k*k1)/k2;
	expctd.append(k3);
	j+=1;
chi=[];j=0;
while j<10:
	k4=math.pow((obsrvd[j]-expctd[j]),2);
	k5=k4/expctd[j];
	chi.append(k5);
	j+=1;
print sum(chi);
	
#eq prob exponential 
expctd1=[];
j=0;
while j<10:
	expctd1.append(10);
	j+=1;
chi=[];j=0;
while j<10:
	k4=math.pow((obsrvd[j]-expctd1[j]),2);
	k5=k4/expctd1[j];
	chi.append(k5);
	j+=1;
print sum(chi);

plt.title("Histogram of Observed Data")
plt.xlabel("Random Variate")
plt.ylabel("Frequency")
plt.hist(o, histtype='stepfilled', alpha=0.2)
plt.show()
