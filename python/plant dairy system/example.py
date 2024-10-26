import csv
import time
plant_name = str(input("tell plant name"))
plant_hight = str(input("tell plant hight"))
plant_age = str(input("tell plant age"))
plant_health = str(input("tell plant health"))
# Data to be written to the CSV file
data = [
    {'Name':plant_name,'hight':plant_hight,'age': plant_age,'health':plant_health}
]

# Specify the file name
csv_file = "plantdairy.csv"

# Specify the CSV file's header
fields = ['Name', 'hight', 'age','health']

# Writing to CSV file
with open(csv_file, 'a', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
    
    # Write the header
    csvwriter.writeheader()
    
    # Write the data
    csvwriter.writerows(data)

print("Data has been written to", csv_file)
print("open the program again to write more data")
time.sleep(2)
