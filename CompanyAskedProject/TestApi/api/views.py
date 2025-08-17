# from django.shortcuts import render
# from .models import User, Post
# # Create your views here.

import asyncio

from .models import Employee
from .Serializers import EmployeeSerializers
from rest_framework.views import APIView

class AsyncEmplyeeView(APIView):
    executor = ThreadPoolExecutor(max_workers=10)
    
    async def get(self,request, *args,**kwargs):
        employees = await self.get_employee()
        return 
        
    def get_emplo