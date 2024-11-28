from utilis import *

#Print the names of the available datasets
print("Available datasets:")
for name in datasets.keys():
    print(f" - {name}")

#Ask the user for the dataset name
dataset_name = input("Enter the name of the dataset: ")

#get the selected dataset
df = datasets[dataset_name]

# SUM QUERIES FOR NUMERIAL COLUMNS
# Dictionary to store the sensitivity for each column
sensitivities_sum = {}
#getting user input 
#print the numerical columns also fraction columns are included
numerical_columns = df.select_dtypes(include=np.number).columns.tolist()
print("Nmerical Columns are: ",numerical_columns)
#print("Numerical Columns are:age,fnlwgt,education-num,capital-gain,capital-loss,hours-per-week")
column = input("Enter the column name for Sum Sensitivtiy: ")
columns= [c.strip() for c in column.split(",")]
start_time = time.time()
#The script then loop overs each column specified by the user 
for column in columns:
    # Define function to analyze, summing
    def sum_records(dataset):
        return dataset[column].sum()
#orignal sum is calculated of column is calculated    
    original_sum = sum_records(df)
#Initializing empty list to store the sensitivities
    sensitivities = []
#Looping over the dataset , creating a copy of the dataset a neighbour  with one records column value set to 0 each time    
    for i in range(len(df)):
        neighbor = df.drop(i)
# The sum of the column in the neighbor dataset is calculated        
        count = sum_records(neighbor)
#The sensitivity(the absolute difference between the neighbour's sum and the original sum) is calculated)        
        sensitivity = abs(count - original_sum)
#The sensitivity is appended to the list of sensitivities        
        sensitivities.append(sensitivity)

#The maximum sensitivity is calculated and stored in the dictionary alsos storing min and avg sensitivities   
    sensitivities_sum[column] = max(sensitivities), min(sensitivities), sum(sensitivities) / len(sensitivities)
    print(f'Max Sensitivity for Sum for column {column}:', sensitivities_sum[column])
# Calculate the minimum, maximum, and average sensitivity
#min_sensitivity = min(sensitivities)
max_sensitivity = max(sensitivities)
#avg_sensitivity = sum(sensitivities) / len(sensitivities)

end_time = time.time()
minutes, seconds = divmod(end_time - start_time, 60)
print(f'Total runtime of sum query is {minutes} minutes and {seconds} seconds.')
#plot the calculated sensitivities for sum 

# Extract column names and sensitivities from the dictionary
columns = list(sensitivities_sum.keys())
max_sensitivities = [sens[0] for sens in sensitivities_sum.values()]
min_sensitivities = [sens[1] for sens in sensitivities_sum.values()]
avg_sensitivities = [sens[2] for sens in sensitivities_sum.values()]

#save the max senstivities for all the columns in a dictionary and calling it later in the other files
sum_sensitivities = {}
sum_sensitivities['max'] = max_sensitivities
sum_sensitivities['columns'] = columns

# # Define the bar width and positions
# bar_width = 0.25
# r1 = np.arange(len(columns))
# r2 = [x + bar_width for x in r1]
# r3 = [x + bar_width for x in r2]

# # Create a grouped bar plot
# plt.figure(figsize=(10, 6))
# plt.bar(r1, max_sensitivities, color='b', width=bar_width, edgecolor='grey', label='Max')
# plt.bar(r2, min_sensitivities, color='r', width=bar_width, edgecolor='grey', label='Min')
# plt.bar(r3, avg_sensitivities, color='g', width=bar_width, edgecolor='grey', label='Avg')

# # Add labels and title
# plt.xlabel('Columns', fontweight='bold')
# plt.ylabel('Sensitivity')
# plt.xticks([r + bar_width for r in range(len(columns))], columns)
# plt.title('Sensitivities for Sum Queries')
# plt.legend()
# plt.show()

