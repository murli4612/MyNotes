# # def calculator(a, b, operation):
# #     if operation == 'add':
# #         return a + b
# #     elif operation == 'subtract':
# #         return a - b
 
# from  abc import ABC, abstractmethod

# class Calculator(ABC):
#     @abstractmethod
#     def operation(self, a, b):
#         pass

# class add(Calculator):
#     def operation(self, a, b):
#         return  a + b
    
# class subtract(Calculator):
#     def operation(self, a, b):
#         return  a - b


# class Cal:
#     def Calulate(self, a, b, ope:Calculator):
#         return ope.operation(a,b)
    
# calc = Cal()

# print(calc.Calulate(2,3, add()))
# print(calc.Calulate(4,3, subtract()))


# 0001:0002:0003:0004:0005:0006:0007:0008
# 1:2:3:4:5:6:7:8
 
# 2001:0db8:0000:0000:0000:0000:0000:0001
# 2001:db8::1
 
# 0:0:0:0:0:0:0:1
# ::1

def compress_ip6(ip6):
    ip6_list = ip6.split(":")
    trailing_ip6_list = [h.lstrip("0") or "0" for h in ip6_list]
    print(trailing_ip6_list)
    
    compress_out= []
    for i,h in enumerate(trailing_ip6_list):
        if h =="0":
            compress_out.append(":")
        else:
            compress_out.append(h)
    return ":".join(compress_out)
            
        
        
    

# input = "0001:0002:0003:0004:0005:0006:0000:0008"
input ="2001:0db8:0000:0000:0000:0000:0000:0001"

print(compress_ip6(input))