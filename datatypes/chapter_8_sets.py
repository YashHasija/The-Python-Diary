essential_spices = {"cardamom", "ginger", "cinamon"}
optional_spices = {"cloves", "ginger", "black_pepper"}

# | this is used to merge two sets 
all_spices = essential_spices | optional_spices
print(f'All spices: {all_spices}')

# & this is used find common in set
common_spices = essential_spices & optional_spices
print(f'common spices: {common_spices}')

# - is used 
only_in_essential = essential_spices - optional_spices
print(f'only in essential spices :{only_in_essential}')

# Membership test - (in) is used to check exclusive item
print(f"Is 'clove'in essential spices? {'cloves'in essential_spices}" )

# Frozenset - This is immutable (Unlike regular sets, which can be changed (add, remove elements), frozensets cannot be modified after creation)
list = {"a","b"}
fset = frozenset(list)
print(f'{list}')