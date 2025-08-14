# from collections import Counter
# import heapq

# def Top_k_frequent_element(array,k):
#     heap =[]
#     heap_dict = Counter(array)
    
#     for key, value in heap_dict.items():
#         heapq.heappush(heap,(value,key))
        
#         if len(heap) > k:
#             heapq.heappop(heap)
    
#     print(heap)
#     result = [item[1] for item in heap]
#     return result

# nums = [1, 1, 1, 2, 2, 3]
# k = 2
# result = Top_k_frequent_element(nums, k)
# print(result)

from collections import Counter
def top_k_frequent(nums, k):
# Count frequencies of each element
    freq_map = Counter(nums)
    # Sort the dictionary by values in descending order
    sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    # Extract the top k elements
    result = [item[0] for item in sorted_freq[:k]]
    return result
# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2
result = top_k_frequent(nums, k)
print(result)

            
    