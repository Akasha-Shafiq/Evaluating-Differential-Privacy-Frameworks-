from utilis import *

#Print the names of the available datasets
print("Available datasets:")
for name in datasets.keys():
    print(f" - {name}")

#Ask the user for the dataset name
dataset_name = input("Enter the name of the dataset: ")

#get the selected dataset
df = datasets[dataset_name]

start_time = time.time()
# A function is defined to count the number of records in a dataset.
def count_records(dataset):
    return len(dataset)

# The original count of records in the dataset is calculated.
original_count = count_records(df)

# An empty list is initialized to store the sensitivities.
sensitivities= []

# The script then loops over the dataset, dropping one record at a time to create a neighbor.
sensitivities_count = {}
for i in range(len(df)):
    neighbor = df.drop(i)
    
# The count of records in the neighbor dataset is calculated.
    count = count_records(neighbor)
    
# The sensitivity (the absolute difference between the neighbor's count and the original count) is calculated.
    sensitivity = abs(count - original_count)
    
# The sensitivity is appended to the list of sensitivities.
    sensitivities.append(sensitivity)
# The global sensitivity (the maximum sensitivity) is calculated.
global_sensitivity = max(sensitivities)

print('Sensitivity for Count:', global_sensitivity)
# The script then initializes another empty list to store the sensitivities for the sum of numerical columns.
sensitivities= []

end_time = time.time()
print(f'Total runtime of the program for count is {end_time - start_time} seconds.')

# save the count sensitivites and execution time in a dictionary also save number of records of each dataset
count_records = {}
sensitivities_count['count'] = global_sensitivity
sensitivities_count['time'] = end_time - start_time
        
        

