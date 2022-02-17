import json


file = open("file.txt","r")
new_dict = []
for line in file:
    new_dict.append(json.loads(line))
keys = []
for key,value in new_dict[0].items():
    keys.append(key)
print("The available keys are:",keys)
result = input("Please what key do you want?")
new_list = [row[result] for row in new_dict]
print("Max value:",max(new_list))
print("Min value:",min(new_list))
