# # Title: "Maximum Sum of Subarray" 
# # Description: Given an integer array nums, find the maximum sum of a subarray within the array. 
# # Example: 
# # Input: nums = [-2,1,-3,4,-1,2,1,-5,4] 
# # Output: 6 
# # Explanation: The maximum sum of a subarray is [4,-1,2,1] which equals 6. 
# # # Constraints: 
# # 1 <= nums.length <= 10^5 
# # -10^4 <= nums[i] <= 10^4 



# def max_sub_array(nums):
#     max_sum = float('-inf')
#     current_sum = 0
#     start  = end = s= 0
#     # for num in nums:
#     #     current_sum= max(num, current_sum + num)
#     #     max_sum = max(max_sum, current_sum)
#     # return max_sum
    
#     for i in range(len(nums)):
#         if nums[i] > current_sum + nums[i]:
#             # print(nums[i],"**")
#             current_sum = nums[i]
#             s = i
#         else: 
#             current_sum += nums[i]
#             # print(nums[i],"--")
#         if current_sum > max_sum:
#             max_sum = current_sum
#             # print(max_sum,"===")
#             start  = s
#             end = i
#     return max_sum, nums[start:end+1]

# nums = [-2,1,-3,4,-1,2,1,-5,4] 

# print(max_sub_array(nums))




# Design a solution for Car Rental System 
# The Car Rental System is a web-based application designed to manage the rental
# of vehicles from a fleet.
# The system allows customers to browse and book available cars, while 
# also providing administrators with tools to manage the fleet, track 
# rentals, and generate reports. 
# // Backend 
# // 


# // Front End 
# //  


 
 
 HLD:
    
1) REQUIREMENTS:
    a) Functional:
        1) user Management
        2)Car Management(admin)
        3)Search and book( Booking)
        4)Tracking servies
        5)Payments
        6)Revie and Rating
    b)Non-functional:
        1)Scalibality
        2)Perforence
        3)Secrity
        4)Reliability
        
Database Schema:
    1)Users(id,name,email,phone)
    2)Cars(id,model,year,Type_of_car,)
    3)Booking(id,user_id,car_id)
    4)Payments(id, Booking_id, status)
    5)Review
    
API_Design:
    1)POST /user/register
    2)POST /user/login --for the Aunthenticate user
    3)GET /car/avilable - Fetch avilable based on query param
    4)POST / Booking_car 
    5)POST /payments/process
    6)POST /add/revivew
    