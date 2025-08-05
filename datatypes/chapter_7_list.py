# To APPEND - To add something to list in the end
ingredients = ["water", "milk", "black_tea"]
ingredients.append ("sugar")   
print(f'Ingredients are: {ingredients}')

# To REMOVE - To remove something from list 
ingredients.remove ("water")
print(f'Ingredients are: {ingredients}')

# COMBINING TWO LIST Usinfg    .extend
spice_options = ["ginger","cardamom"]
chai_ingredients = ["water","milk"]
chai_ingredients.extend(spice_options)
print(f'{chai_ingredients}')

# Inserting something into list using    .insert 
chai_ingredients.insert(2 , "black_tea")  #inserting something to a particular location 
print(f'{chai_ingredients}')

# POP - removing last element from the the list using   .pop()
last_added = chai_ingredients.pop()
print(f'{last_added}')
print(f'{chai_ingredients}')

# REVERSING - revesing the whole list using .reverse()
chai_ingredients.reverse()
print(f'{chai_ingredients}')

#SORTING - sorting the list alphabetical order using   .sort()
chai_ingredients.sort()
print(f'{chai_ingredients}')

# to find the maximum and minimum value in the list using MAX and MIN 
sugar_levels = [1,2,3,4,5,6,7,8,9]
print(f'maximum sugar levels : {max(sugar_levels)}')
print(f'maximum sugar levels : {min(sugar_levels)}')

# Operator overloading -Operator overloading means giving special meaning to standard operators (like +, *, etc.) 
# when they are used with custom data types or objects. In Python, lists use operator overloading: 
# when you use + with two lists,
# it joins (concatenates) them into one new list, instead of adding their values like numbers.
base_liquid = ["water","milk"]
extra_flavors =["ginger"]
full_liquid_mix = base_liquid + extra_flavors
print(f'Full liquid mic : {full_liquid_mix}')


strong_brew = ["black_tea"]*3
print(f'Strong brew: {strong_brew}')

# bytarray -A bytearray in Python is a special type of sequence that stores bytes (numbers from 0 to 255)
# . It is like a list, but for bytes instead of regular numbers or strings.
#  You can change (mutate) its contents, just like a list.
raw_spice_data = bytearray(b"cinamon") # treating word cinamon as list 
raw_spice_data = raw_spice_data.replace(b"cina", b"card")
print(f'{raw_spice_data}')

#converting string to list using    .split()
vegetables = "tomato cucumber spinach"
vegetables_list = vegetables.split()
print(f'{vegetables_list}')