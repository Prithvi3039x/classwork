students = {
    101 : {"Name" : "Prithviraj" , "Scores" : [78, 87, 90]},
    102 : {"Name" : "Atharv" , "Scores" : [87, 89, 95]},
    103 : {"Name" : "Samyak" , "Scores" : [80, 89, 93]},
    104 : {"Name" : "Karan" , "Scores" : [90, 77, 98]},
    105 : {"Name" : "Soham" , "Scores" : [95, 97, 98]}
}

for sid, details in students.items():
    avg = sum(details["Scores"]) // len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg >= 50

print("Students who passed:")
for sid,details in students.items():
    if details["Passed"]:
        print(details["Name"])

# students.update( 106 : {"Name" : "Aryan" , "Scores" : [99, 99, 99]}) 