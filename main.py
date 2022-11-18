import json
from faker import Faker

fake = Faker()

color_list = [fake.color_name() for x in range(20)]
# create list of 20 random color with faker
# uses list comp
print(color_list)

def remove_dups(list1: list) -> None:
  """ Remove duplicates from list using dict comp

  Args:
      list1 (list): List to check for duplicates
  Return: 
      list with no duplicates
  """
  return list(dict.fromkeys(list1))

color_list = remove_dups(color_list)

print(color_list)

color_dict = {color: len(color) for color in color_list}
# using dict comp to create dictionary where colors are keys and len is value
print(color_dict)

with open("./data/color_dict.json", "w") as json_file:
# write color_dict to json
  json.dump(color_dict, json_file, indent=4, skipkeys=True)

print("Done!")

with open("./data/color_dict.json", "r") as json_file:
# open json file to read, load as color_dict
  color_dict = json.load(json_file)
# for keys and values in dict return string of all greater than or equal to 4
  for key, value in color_dict.items():
    if value >= 4:
      print (f"{key} is {value} letters")
