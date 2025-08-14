# from django.db import models

# class Employee(models.Model):
#     first_name = models.CharField(max_length=15)
#     last_name = models.CharField(max_length=15)
#     age = models.IntegerField()
    
    


# database_router.py:


# class Multidb:
#     def de_read(self,Ganesh,models):
        
        
# from myapp.models import Employee


# employe1 = Employee.objects.using('mysql_db').get(id=1)

# list of number , use lamda , filter even number:
    
    
# list1 = [1,2,3,4,5,6]

# even_number = list(filter(lambda x: x % 2 ==0, list1))

# print(even_number)

# even_number = list(map(lambda x: x if x % 2 ==0 else '' , list1))

# print(even_number)

def even_number(nums):
    list2 = []
    for num in nums:
        if num % 2 == 0:
            list2.append(num)
    return list2
list1 = [1,2,3,4,5,6]

print(even_number(list1))