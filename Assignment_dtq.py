from scipy.stats import expon
from numpy.random import normal, uniform ,randint, random_sample, exponential,poisson
import matplotlib.pyplot as plt	
import matplotlib.mlab as mlab	
import numpy as np
import math
import csv
from collections import defaultdict
from pylab import *
import scipy.stats 

def rng():
	b=int(raw_input("Enter the limit for RNG (<10)\n"));
	n=int(raw_input("How many numbers do you wish to generate?\n"));
	a=13;
	c=17;
	x=[];
	m=math.pow(2,b);
	frst_val=int(raw_input("Enter seed\n"));
	x.append(frst_val);
	for i in range(1,n):
		x.append((a*x[i-1]+c)%m);
	r=[];
	for i in range(n):
		r.append(x[i]/m);
	lamda=float(raw_input("Enter the average value\n"));
	v=[];
	for i in range(n):
		if(r[i]==0):
			temp=0;
		else:
			temp=((-1)*math.log(r[i]))/lamda;
		v.append(temp);

	for i in range(len(v)):
		v[i]=math.floor(v[i]);
	if input("Output data to csv (True/False)? "):
		outfile=open('Random number generation-(%s).csv' %(lamda),'wb')
		output=csv.writer(outfile)
		output.writerow(['Serial no','Random number','Normalized Random number','Variates'])
		i=0
		for i in range(n):
			outrow=[]
			outrow.append(i)
			outrow.append(r[i])
			outrow.append(v[i])
			outrow.append(x[i])
			output.writerow(outrow)
			outfile.close()
	print ""

def histogram():
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
	print "Chi Square for poisson: "+str(sum(chi));
	kam=chi;	
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
	#print sum(chi);
	print "Chi Square for exponential: "+str(sum(chi));
	if(chi<kam and choice==1):
		print "Distribution is exponential";
	elif(chi<kam and choice==3):
		print "Distribution is Uniform";
	else:
		print "Distribution is Poisson"
	plt.title("Histogram of Observed Data")
	plt.xlabel("Random Variate")
	plt.ylabel("Frequency")
	plt.hist(o, histtype='stepfilled', alpha=0.2)
	plt.show()

def conf():

	z=[];
	w=[];
	num=int(raw_input('How many inputs do you require?'));
	print 'Enter System Production values Z one by one';
	for i in range(0,num):
		z.append(int(raw_input()));
	m1=min(z);m2=max(z);
	#w=uniform(m1,2*m2,num);
	print 'Enter Model Production values W one by one';
	w=[]
	for i in range(0,num):
		w.append(int(raw_input()));

	for i in range(len(w)):
		w[i]=math.floor(w[i])
	diff=[];
	for i in range(len(z)):
		diff.append(z[i]-w[i]);
	diff_avg=sum(diff)/num;
	std_dev=[];
	for i in range(len(z)):
		p2=math.pow((diff[i]-diff_avg),2)
		std_dev.append(p2);
	sum_d=sum(diff);
	sum_sd=sum(std_dev)/(num-1);
	t=(diff_avg)*(math.sqrt(float(num)))/(math.sqrt(sum_sd));

	print("T test statistic value is :"+str(t)); 
	for i in range(len(z)):
		z[i]=(z[i]-m1)/(m2-m1);

	N=num    # sample size
	gamma=0.95  # confidence level
	mu=10      # true mean
	sigma=2    # true standard diviation 
	mu_hat=mean(z)           # sample mean
	sigma_hat=std(z, ddof=1) # sample standard deviation
	 
	print('sample mean mu_hat                  : %f' % mu_hat)
	print('sample standard deviation sigma_hat : %f' % sigma_hat)
	l=scipy.stats.t.ppf( (1-gamma)/2, N-1)    # lower percentile
	u=scipy.stats.t.ppf( 1-(1-gamma)/2, N-1)  # upper percentile
	print('confidence interval mu_hat          : (%f, %f)' % 
	      (mu_hat+l*sigma_hat/sqrt(N), mu_hat+u*sigma_hat/sqrt(N)))
	l=scipy.stats.chi2.ppf( (1-gamma)/2, N-1)    # lower percentile
	u=scipy.stats.chi2.ppf( 1-(1-gamma)/2, N-1)  # upper percentile
	print('confidence interval sigma_hat       : (%f, %f)' % 
	      ( sqrt((N-1)/u)*sigma_hat, sqrt((N-1)/l)*sigma_hat))


def main():
	ch=int(raw_input(' 1.Random Number generation and Random variate\n 2.Test Distribution\n 3.Model Validation\n 4.Exit\n'))
	while(ch!=4):
		if(ch==1):
			rng();
		elif(ch==2):
			histogram();
		elif(ch==3):
			conf();
		elif(ch==4):
			exit();
		else:
			print "Wrong choice Re-enter value : ";
			#ch=int(raw_input('1.Random Number generation and Random variate\n 2.Test Distribution\n 3.Model Validation\n 4.Exit\n'));
		ch=int(raw_input('1.Random Number generation and Random variate\n 2.Test Distribution\n 3.Model Validation\n 4.Exit\n'));

if __name__=="__main__":main() 