# def remove_name_from_list(names , matching_name):
#     # result = []
#     # for name in names:
#     #     if name == matching_name:
#     #         names.remove(name)
    
#     result = [name for name in names if name != matching_name ]
            
#     return  result

def sort_name_based_on_salary(list_typle):
    # for item in list_typle:
    
    sorted_value = sorted(list_typle, key=lambda x: x[1])
    print(sorted_value)
    
# list_name = ["murli","manohar","mohan","suresh"]

list_typle =[ ("murli", 2000, "software"),("manohar", 4000, "Testing")]

# # print(remove_name_from_list(list_name,"mohan"))
print(sort_name_based_on_salary(list_typle)) 

# class Animal_sigleton:
#     _ins = None
    
#     def __new__(cls, *args, ** kwargs):
#         if cls._ins is None:
#             print("sigleton class")
#             cls._ins  = super(Animal_sigleton,cls)
#         return cls._ins
#     # def walk(self , leg):
        
#     #     leg = self.leg
#     #     print("walking with " ,leg)
    
# # class Dog(Animal):
# obj1 = Animal_sigleton("cat")
# obj2 = Animal_sigleton("dd")
# print( obj1 is obj2)