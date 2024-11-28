#Noise for Count 
from utilis import *
# import sum sensitivity from Sum_sensitivity.py

from count_sensitivity import*


print(df.shape)


#selecting epsilon
epsilon = float(input("Enter the value of epsilon: "))
Sensitivity = sensitivities_count
for key in Sensitivity.keys():
    print(key, Sensitivity[key])
    
scale = Sensitivity['count']/epsilon
print(f"Scale: {scale}")

# laplcian noise with locational parameter 0 and scale parameter scale
locational_parameter = 0
lapalace_noise = [np.random.laplace(locational_parameter,scale)for x in range(100000)]

# generating gaussian noise with locational parameter 0 and scale parameter scale
delta = 1/(len(df)**2)
print(f"Delta: {delta}")
sigma = sensitivity*np.sqrt(2*np.log(1.25/delta))/epsilon
#Can also use df.shape instead of 100000 in the range that is the size of the dataset to generate noise equal to the size of the dataset
gaussian_noise = [np.random.normal(locational_parameter,sigma)for x in range(100000)]
#generating gaussian noise graph for the selected dataset


plt.hist(gaussian_noise, bins=50, alpha=0.5,color='b')
plt.hist(lapalace_noise, bins=50, alpha=0.5, color='r')
plt.title(' Noise')
plt.legend(['Gaussian', 'Laplace'])
plt.xlabel('Noise')
plt.ylabel('Frequency')
plt.show()


