#here we are creating a dictionary  using (dict)
# eg type,size and sugar here are the keys and masala chai, large and 2 are there values 

chai_order = dict(type="masala chai", size="large",sugar=2)
print(f'chai_order: {chai_order}')


# We are creating an empty dictionary called chai_recipe.
# Then, we add two key-value pairs: "base" with value "black tea" and "liquid" with value "milk".
# Finally, we print the value associated with the "base"
chai_recipe = {}
chai_recipe ["base"] = "black tea"
chai_recipe ["liquid"] = "milk"
print(f'Recipe base: {chai_recipe["base"]}')

# here we are deleting the liquid key from the chai_recipe dictionary 
del chai_recipe["liquid"]
print(f'Recipe base: {chai_recipe}')


# Membership test in dictionary 
print(f'is suagar in chai order? {'sugar'in chai_order}')

# We create a dictionary called chai_order with type, size, and sugar as keys.
# Then, we print all the keys, values, and key-value pairs (items) of the dictionary using the respective
chai_order = {"type":"ginger chai", "size":"medium", "sugar": 1 }
print(f'chai order (keys): {chai_order.keys()}')
print(f'chai order (values): {chai_order.values()}')
print(f'chai order (items): {chai_order.items()}')

# here we are removing the last item from dictionary chai_order using .popitem()
last_item = chai_order.popitem()
print(f'last item:{last_item}')

# here we are updating the chai_recipe dict with new dict extra spices using .update 
extra_spices = {"cardamom":"crushes", "ginger":"sliced"}
chai_recipe.update(extra_spices)
print(f'updated chai recipe {chai_recipe}')

# We use the .get() method to safely retrieve the value for the "note" key from chai_order.
# If "note" does not exist, it returns "No note" as the default value and prints
chai_customer_note = chai_order.get("note","No note")
print(f'updated chai order with customer note : {chai_customer_note}')

#Lists and tuples store sequences, but only lists can be changed.
#Sets store unique items, no order.
D#ictionaries store data as key-value pairs.