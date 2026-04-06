# Задача №3
def find_common_element(list1, list2):
    list3 = []
    for li1 in list1:
        for li2 in list2:
            if li1 == li2:
                list3.append(li1)
        
    sort_list = sorted(set(list3))
    return sort_list

result = find_common_element([1,2,2,3,5], [2,3,4,5,5])
print(result)



# Можно было вот так, но это не я сам:
'''
def find_common_elements(list1, list2):
    return sorted(set(list1) & set(list2))
'''