# import itertools

# list1 = [1,2]
# list2 = [3,4]

# result = list(itertools.chain(list1, list2))
# print(result)

# dict1 = {'a' : 1, 'b': 2}
# dict2 = {'c' : 3, 'd': 4}

# # result = {**dict1, **dict2}
# # print(result)

# dict1.update(dict2)
# print(dict1)


employee ={
    "emp1" :{
        "name": "Murli",
        "age": 30
    },
    
    "emp2" :{
        "name": "Manohar",
        "age": 33
    }
}

emp3 ={
    "name" : "kunal",
    "age": 40
}

employee.update(emp3)
print(employee)
# print(employee["emp2"]["age"])