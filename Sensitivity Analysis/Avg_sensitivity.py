from utilis import *
#Print the names of the available datasets
print("Available datasets:")
for name in datasets.keys():
    print(f" - {name}")

#Ask the user for the dataset name
dataset_name = input("Enter the name of the dataset: ")

#get the selected dataset
df = datasets[dataset_name]
numerical_columns = df.select_dtypes(include=[np.number]).columns.tolist()
print("Numerical Columns are: ",numerical_columns)
sensitivities_avg = {}

# Get user input
columns = input("Enter columns name for Avg Sensitivity: ")  
columns = [c.strip() for c in columns.split(',')]
start_time = time.time()
for column in columns:

    sensitivities = []

    for i in range(len(df)):

        neighbor = df.drop(i)
            
        original_avg = df[column].mean()
        neighbor_avg = neighbor[column].mean()
            
        sensitivity = abs(original_avg - neighbor_avg)
        
        sensitivities.append(sensitivity)
    sensitivities_avg[column] = max(sensitivities), min(sensitivities), sum(sensitivities) / len(df)
    min_sensitivity = min(sensitivities)  
    avg_sensitivity = sum(sensitivities)/len(sensitivities)
    max_sensitivity = max(sensitivities)

    print(f"Column: {column}")
    print(f"Minimum Sensitivity: {min_sensitivity}")
    print(f"Average Sensitivity: {avg_sensitivity}")
    print(f"Maximum Sensitivity: {max_sensitivity}")
    



#Extract column names and sensitivities from the dictionary
columns = list(sensitivities_avg.keys())
max_sensitivities = [sens[0] for sens in sensitivities_avg.values()]
min_sensitivities = [sens[1] for sens in sensitivities_avg.values()]
avg_sensitivities = [sens[2] for sens in sensitivities_avg.values()]

#save the max senstivities for all the columns in a dictionary and calling it later in the other files
avg_sensitivities={}
avg_sensitivities['max']= avg_sensitivities
avg_sensitivities['columns']=columns


end_time = time.time()
minutes, seconds = divmod(end_time - start_time, 60)
print(f'Total runtime of sum query is {minutes} minutes and {seconds} seconds.')
# #Defone the bar width and positions
# bar_width=0.25
# r1 = np.arange(len(columns))
# r2 = [x + bar_width for x in r1]
# r3 = [x + bar_width for x in r2]

# #create a grouped bar plot
# plt.figure(figsize=(10,6))
# plt.bar(r1, max_sensitivities, color='b', width=bar_width, edgecolor='grey', label='Max')
# plt.bar(r2, min_sensitivities, color='r', width=bar_width, edgecolor='grey', label='Min')
# plt.bar(r3, avg_sensitivities, color='g', width=bar_width, edgecolor='grey', label='Avg')

# #Add labels and title
# plt.xlabel('Columns', fontweight='bold')
# plt.ylabel('Sensitivity')
# plt.xticks([r + bar_width for r in range(len(columns))], columns)
# plt.title('Sensitivities for Average Queries')
# plt.legend()
# plt.show()



