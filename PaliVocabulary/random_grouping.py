import random

def flatten_list(lst):
    return sum(lst, [])


def assign_to_groups(items, n):
    items = list(items)
    random.shuffle(items)
    groups = [items[i:i+n] for i in range(0, len(items), n)]
    return groups

def list_to_dict(lst):
    result = {}
    for i, val in enumerate(lst):
        result[i] = val
    return result
	
def random_grouping_map(large_group, group_size):
    items = set(range(large_group))
    groups = assign_to_groups(items, group_size) 
    flattened_list = flatten_list(groups) 
    dict = list_to_dict(flattened_list)
    return dict 
    
items = set(range(10))
groups = assign_to_groups(items, 3)
print(groups)
# Output: [[0, 6, 7], [4, 5, 1], [9, 2, 3], [8]]
flattened_list = flatten_list(groups) 
print(flattened_list) 
dict = list_to_dict(flattened_list)
print(dict)   

#  [i for i in range(1, n+1)] possible  instead of set(range(10)) 

large_group = 20
group_size = 4
print(set(range(large_group)))  
print(random_grouping_map(large_group, group_size))     
