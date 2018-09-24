import random
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_palette(sns.color_palette("hls",6))
def check_validity(smth):
	# type(smth) must be list/array.
	boolean = True
	i = 0 
	j = 1
	l = 0
	curr = [0,0]
	smth_more = []
	while i<len(smth):
		curr = list(np.add(curr,smth[i]))
		smth_more.append(curr)
		
		i+=1
	while j<len(smth_more):
		while l<j:
			if smth_more[j] == smth_more[l]:
				boolean = False
				break
			l+=1
		l=0
		j +=1

	return boolean



def polymer(len_chain,nb_attempts):
# This routine will try to create polymer of len_chain elements 
# (which do not super-impose) x times (depending on nb_attempts)
	
	m = len_chain
	n = nb_attempts	
	# init
	i = 0
	j = 0
	success = 0
	temp = [[0,0]]
	#main loop
	while i<nb_attempts:
		# i-th attempt

		while j<len_chain:
			# try to create a polymer chain
			rdm = int(3*random.random()+1)
			if rdm == 1:
				temp.append([0,1])  # up
			elif rdm == 2:
				temp.append([1,0])   # right
			elif rdm == 3:
				temp.append([0,-1]) # down
			else :
				temp.append([-1,0]) # left
			j+=1

		if check_validity(temp)!= False:
			success +=1
		# reset
		j = 0
		temp = []

		i +=1
	return success

#annexe : une petite fonction pour faire un plot
def my_plot(nb_attempts,maxSize_polymer):
	i = 2 # not interested in a monomer, at least 2 to make a polymer
	tempx=[]
	tempy=[]
	while i<maxSize_polymer:
		tempx.append(i)
		y = polymer(i,nb_attempts)
		tempy.append(y)
		i+=1
	plt.plot(tempx,tempy,label=str(nb_attempts))
	tempx=[]
	tempy=[]
	



my_plot(10000,40)
my_plot(5000,40)
my_plot(1000,40)
my_plot(100,40)
my_plot(50,40)
my_plot(30,40)
plt.legend(loc = 'center left', bbox_to_anchor=(1,0.5))
plt.savefig("patate.png",format = "png",dpi=150,bbox_inches='tight')
