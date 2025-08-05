#UNPACKING
masala_spices =("cardamom","cloves","cinamon") #using parenthesis
(spice1,spice2,spice3) = masala_spices
print(f'Main Masala spices : {spice1} ,{spice2} ,{spice3} ') # this concept is known as unpacking -Unpacking is a way to assign the elements
#of a collection (like a tuple or list) to multiple variables in a single line.
# For example, if you have a tuple with three items, you can assign each item to its own variable at once:



# SWAPPING
ginger_ratio , cardamom_ratio = 2,1
print(f'ratio is G {ginger_ratio} and c {cardamom_ratio} ')
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio # this is called swapping -Swapping is a way to exchange 
#the values of two variables. In Python, you can do this in one line without needing a temporary variable. 
print(f'ratio is G {ginger_ratio} and c {cardamom_ratio} ')

#MEMBERSHIP
print(f'Is ginger in masala spices ? {'ginger'in masala_spices}')
# to check if it is present or not 

