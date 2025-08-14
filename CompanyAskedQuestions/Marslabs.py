# # my_set = {10,20,30,40,40}
# # my_set1 = set([50,60,70,80,80])
# # # print(type(my_set))
# # for value in my_set1:
# #     print(value)

# def is_anagrams(string1, string2):
#     s1 = string1.replace(" ","").lower()
#     s2 = string2.replace(" ","").lower()
    
#     if len(s1) != len(s2):
#         return False
    
#     map_count = {}
    
#     for char in s1:
#         if char in map_count:
#             map_count[char] +=1
#         else:
#             map_count[char] = 1
#     for char in s2:
#         if char not in map_count:
#             return False
#         map_count[char] -=1
#         if map_count[char] < 0:
#             return False
#     # print(map_count)
#     for value in map_count.values():
#         if value != 0:
#             return False
        
        
#     return True
    
    
# print(is_anagrams("Silent", "Listen"))
# print(is_anagrams("Silent", "Hello"))
# print(is_anagrams("Dormitory", "Dirty Room"))



 
# import asyncio
# import redis
# from datetime import datetime
# from typing import Dict, List, Optional
# import pickle
# class TaskScheduler:
#     def __init__(self, redis_url: str = "redis://localhost:6379"):
#         self.redis = redis.Redis.from_url(redis_url)
#         self._running = False
#         self._tasks: Dict[str, asyncio.Task] = {}
#     async def add_task(
#         self,
#         task_id: str,
#         func,
#         priority: int = 1,
#         delay: int = 0,
#         *args,
#         **kwargs
#     ) -> bool:
#         """Add a task to the scheduler with optional delay."""
#         if task_id in self._tasks:
#             return False
        
#         async def _wrapped_task():
#             if delay > 0:
#                 await asyncio.sleep(delay)
#             return await func(*args, **kwargs)
        
#         task = asyncio.create_task(_wrapped_task())  # Typo here
#         self._tasks[task_id] = task
#         self.redis.set(f"task:{task_id}", pickle.dumps(task))
#         return True
#     async def cancel_task(self, task_id: str) -> bool:
#         """Cancel a running task."""
#         if task_id not in self._tasks:
#             return False
        
#         task = self._tasks[task_id]
#         task.cancel()
#         del self._tasks[task_id]
#         self.redis.delete(f"task:{task_id}")
#         return True
#     async def get_task_result(self, task_id: str) -> Optional[bytes]:
#         """Retrieve task result from Redis."""
#         cached = self.redis.get(f"task:{task_id}")
#         if cached:
#             return pickle.loads(cached)
#         return None
#     async def run(self):
#         """Start the scheduler loop."""
#         self._running = True
#         while self._running:
            
#             await asyncio.sleep(1)  # Dummy loop
#     async def stop(self):
#         """Stop the scheduler."""
#         self._running = False
#         for task in self._tasks.values():
#             task.cancel()

"select * from users where username = %s and password = %s"
 