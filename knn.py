import numpy as np 
from math import sqrt
import warnings
import pandas as pd
import random
import operator
import pylab as pl

import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')


#dataset = { 'k': [[1,2],[2,3],[3,1]], 'r': [[6,5],[7,7],[8,6]]}
#new_features=[2,6]

dataset2= {'g1':['a','b','e','f'] ,'g2' :['c', 'b', 'e','f','a','g'], 'g3' :['x', 'm', 'z','f','a','g'],
'g4':['r','j','m','c','xx','xz','cb','md','t'] ,'g5' :['c', 'b', 'e','f','a','g','re','xy','mj','yr'], 
'g6' :['r', 'l', 'q','s','t','bg','ss','my','jt','c','bd','sc','jy','qp'],
'g7':['a','b','e','f'] ,'g8' :['c', 'b', 'e','f','a','g'], 'g9' :['x', 'm', 'z','f','a','g'],
'g10':['a','b','e','f'] ,'g11' :['c', 'b', 'e','f','a','g'], 'g12' :['x', 'm', 'z','f','a','g'],
'g13':['a','b','e','f'] ,'g14' :['c', 'b', 'e','f','a','g'], 'g15' :['x', 'm', 'z','f','a','g'],
'g16':['a','b','e','f'] ,'g17' :['c', 'b', 'e','f','a','g'], 'g18' :['x', 'm', 'z','f','a','g'],
'g19':['a','b','e','f'] ,'g20' :['c', 'b', 'e','f','a','g'], 'g21' :['x', 'm', 'z','f','a','g'],
'g22':['a','b','e','f'] ,'g23' :['c', 'b', 'e','f','a','g'], 'g24' :['x', 'm', 'z','f','a','g'],
'g25':['a','b','e','f']}




vote_weight={'g1':[1,2,3,4], 'g2':[1,4,2,5,6,4],'g3':[1,4,2,5,6,3],'g4':[1,2,3,4,2,5,6,7,2], 
	'g5':[1,2,4,0.5,6,4,1,3,5,5],'g6':[1,6,4,3,9,0,4,6,8,9,1.2,12,2,1],
	'g7':[1,2,3,4], 'g8':[1,4,2,5,6,4],'g9':[1,4,2,5,6,3],'g10':[1,2,3,4], 'g11':[1,4,2,5,6,4],'g12':[1,4,2,5,6,3],
	'g13':[1,2,3,4], 'g14':[1,4,2,5,6,4],'g15':[1,4,2,5,6,3], 'g16':[1,2,3,4], 'g17':[1,4,2,5,6,4],'g18':[1,4,2,5,6,3],
	'g19':[1,2,3,4], 'g20':[1,4,2,5,6,4],'g21':[1,4,2,5,6,3], 'g22':[1,2,3,4], 'g23':[1,4,2,5,6,4],'g24':[1,4,2,5,6,3],
	'g25':[1,2,3,4]}
q_user='a'
nearest_neightbour =10


def k_nearest_neighbour(data,user,weight,n):
	occur_group=[]
	check_usr=user
	dict_list=[] # list for creating dictionary having duplicate value
	s=[] # list in sorted order without duplicate value


	for group in data:
		for user in data[group]:
			dict_list.append(user)
		#dict_list= List(set(first_list)|set(second_list))
		#list(set(dict_list))

	for i in dict_list:
   		if i not in s:
   			s.append(i)
   			s.sort()			#sorting the list
	for user in s:
		print(user)
	d = dict.fromkeys(s, 0) # creating dictionary with initial value of 0
	for i in d:
		print (i, d[i])



	for group in data:
		if check_usr in data[group]:
			print([group])
			occur_group.append(group)

	#list(set(occur_group).intersection(data))

	'''for group in occur_group:
		for users in weight[occur_group]:
			sum(occur_group) '''
	#new=[]
	for group in occur_group:
		for group1 in weight:
			if group == group1:

				for user, value in zip(data[group], weight[group1]):
					print(user,value) 
					d[user] +=value							#updating value in dictionary
				'''for user in data[group]:
					new.append(user)
					print(user)
				for value in weight[group1]:
					print(value)'''

	sorted_d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)  		



	print(*occur_group, sep='\n')
	print(sorted_d)
	print(sorted_d[:n]) 

	user_list, value_list= map(list, zip(*sorted_d))
	req_plot_user=user_list[:n]
	req_plot_value=value_list[:n]
	print(user_list)
	print(value_list)

	pl.figure(1)
	x = range(n)
	pl.xticks(x, req_plot_user)
	pl.plot(x,req_plot_value,"g")

	pl.show()


	'''from scipy.interpolate import spline

	T = np.array(req_plot_user)
	power = np.array(req_plot_value)
	plt.plot(T,power)
	plt.show()


	xnew = np.linspace(T.min(),T.max(),300) #300 represents number of points to make between T.min and T.max

	power_smooth = spline(T,power,xnew)

	plt.plot(xnew,power_smooth)
	plt.show()'''





result =k_nearest_neighbour(dataset2,q_user,vote_weight, nearest_neightbour)






#mutiple line for loop different graphs
#for i in dataset:
	#for ii in dataset[i]:

#single line for loop plotted in same graph	
'''[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1])
plt.show()
'''

'''def k_nearest_neighbors(data, predict, k=3):
	if len(data)>=k:
		warnings.warn("k is set to value less than total voting groups!")

	distances=[]
	for group in data:
		for features in data[group]:

			euclidean_distance=np.linalg.norm(np.array(features)-np.array(predict))
			#euclidean_distance=np.sqrt(np.sum((np.array(features)-np.array(predict))**2))
			#euclidean_distance =sqrt((features[0]-predict[0])**2 + (features[1]-predict[1])**2)

			distances.append([euclidean_distance,group])


	votes = [i[1] for i in sorted(distances)[:k]]

	knn= (i[1] for i in sorted(distances)[:3])
	print(votes[:k])
	print(Counter(votes).most_common(1))

	vote_result = Counter(votes).most_common(1)[0][0]

	return vote_result

result =k_nearest_neighbors(dataset, new_features, k=3)



[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1], color=result)
plt.show()'''


