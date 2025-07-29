is_boiling = True
stir_count = 5 
total_actions = stir_count + is_boiling # upcasting because in o/p we will get 1 the true is treated as 1
print(f'total actions {total_actions}')

milk_present = 0  # no milk
print(f'is there milk? {bool(milk_present)}') # if 0 it will show false in o/p if 1 it will show true in 0/p

water_hot = True
chai_added = False
can_server = water_hot and chai_added # use of logical (and) operation if for true than its true if any one of them is false then it shows false 
print(f'chai should be served {can_server}') 