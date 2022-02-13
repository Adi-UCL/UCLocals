import random as r
import csv

# Societies
societies = []
societies_file = open("societies.txt", "r")
for society in societies_file.readlines():
    societies.append(society[:-1])
societies_file.close()
print(societies)

# Courses
courses = []
courses_file = open("courses.txt", "r")
for course in courses_file.readlines():
    courses.append(course[:-9])
courses_file.close()
print(courses)

# Names
names = []
names_file = open("names.txt", "r")
for name in names_file.readlines():
    names.append(name[:-1])
names_file.close()
print(names)

# Locations
locations = []
locations_file = open("locations.txt", "r")
for location in locations_file.readlines():
    locations.append(location[:-6])
locations_file.close()
print(locations)

statuses = ["Study", "Socialize", "Food"]

csv_file = open("testdata.csv", "w")
csv_writer = csv.writer(csv_file)

for i, name in enumerate(names):
    int_id = i + 1
    str_first_name = name.split(" ")[0]
    str_last_name = name.split(" ")[1]
    int_year = r.randint(1, 4)
    str_course = courses[r.randint(0, 189)]
    lst_societies = []
    n_societies = r.randint(0, 3)
    for _ in range(n_societies):
        lst_societies.append(societies[r.randint(0, 359)])
    str_societies = ", ".join(lst_societies)
    str_status = statuses[r.randint(0, 2)]
    str_location = locations[r.randint(0, 320)]
    int_ghost_mode = r.randint(0, 1)
    user = [int_id, str_first_name, str_last_name, int_year, str_course, str_societies, str_status, str_location,
            int_ghost_mode]
    csv_writer.writerow(user)

csv_file.close()
