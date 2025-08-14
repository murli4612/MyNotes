Here’s how you can implement WebSockets in Django using Django Channels.

1️⃣ Install Dependencies

pip install django daphne channels


2️⃣ Create a Django Project

django-admin startproject websocket_project
cd websocket_project
django-admin startapp chat

3️⃣ Update settings.py
Modify websocket_project/settings.py to include Django Channels:
    
INSTALLED_APPS = [
    "daphne",  # Daphne for ASGI server
    "channels",
    "chat",  # Our chat app
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

ASGI_APPLICATION = "websocket_project.asgi.application"

# Channel Layer Configuration (In-Memory)
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}




4️⃣ Update asgi.py
Modify websocket_project/asgi.py to support WebSockets.


import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websocket_project.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # Handles HTTP requests
        "websocket": URLRouter(chat.routing.websocket_urlpatterns),  # Handles WebSockets
    }
)



5️⃣ Create a WebSocket Consumer in chat/consumers.py
This consumer will handle WebSocket connections.


import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Connected to WebSocket!"}))

    async def disconnect(self, close_code):
        print(f"WebSocket closed with code: {close_code}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "")

        # Echo message back
        await self.send(text_data=json.dumps({"message": f"Server received: {message}"}))




6️⃣ Define WebSocket URL Routes in chat/routing.py

from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/$", ChatConsumer.as_asgi()),
]




7️⃣ Add Django URLs in chat/views.py
For rendering a simple WebSocket frontend.

from django.shortcuts import render

def chat_page(request):
    return render(request, "chat.html")


8️⃣ Configure Django URLs in websocket_project/urls.py


from django.contrib import admin
from django.urls import path
from chat.views import chat_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", chat_page, name="chat_page"),
]



9️⃣ Create an HTML WebSocket Client (chat/templates/chat.html)
This page will connect to the WebSocket server.


<!DOCTYPE html>
<html lang="en">
<head>
    <title>WebSocket Chat</title>
</head>
<body>
    <h2>WebSocket Chat</h2>
    <input type="text" id="messageInput" placeholder="Type a message...">
    <button onclick="sendMessage()">Send</button>
    <ul id="messages"></ul>

    <script>
        let socket = new WebSocket("ws://" + window.location.host + "/ws/chat/");

        socket.onmessage = function(event) {
            let data = JSON.parse(event.data);
            let messages = document.getElementById("messages");
            let newMessage = document.createElement("li");
            newMessage.textContent = data.message;
            messages.appendChild(newMessage);
        };

        function sendMessage() {
            let input = document.getElementById("messageInput");
            socket.send(JSON.stringify({ message: input.value }));
            input.value = "";
        }
    </script>
</body>
</html>




🔟 Run the Django WebSocket Server


python manage.py runserver


🔹 How It Works
Django Channels handles WebSocket requests.
ChatConsumer processes WebSocket connections.
The HTML page allows clients to send and receive messages in real time.



🔹 Use Cases
✅ Chat applications (WhatsApp, Slack)
✅ Live notifications (Stock price updates)
✅ Multiplayer gaming (Real-time interaction)
✅ IoT devices (Live sensor updates)


📂 Project Folder Structure

websocket_project/     # Django project root
│── chat/              # Django app for WebSockets
│   │── migrations/    # Django migrations
│   │── templates/     # HTML templates for the chat app
│   │   └── chat.html  # Frontend WebSocket client
│   │── __init__.py    
│   │── consumers.py   # WebSocket Consumer (Handles WebSocket connections)
│   │── routing.py     # WebSocket URL routing
│   │── urls.py        # Django URL routing
│   │── views.py       # Django views (renders HTML template)
│   │── models.py      # (Optional) Database models
│   │── admin.py       # (Optional) Django admin configurations
│   │── apps.py        # Django app config
│── websocket_project/ # Main Django project folder
│   │── __init__.py    
│   │── asgi.py        # ASGI entry point for WebSockets
│   │── settings.py    # Django settings
│   │── urls.py        # Project-wide URL routing
│   │── wsgi.py        # WSGI entry point (for HTTP requests)
│── manage.py          # Django management script
│── db.sqlite3         # Default SQLite database (if used)


🚀 Key Files & Their Roles
File	Purpose
asgi.py	ASGI entry point for handling WebSockets
settings.py	Django settings, including CHANNEL_LAYERS config
routing.py	Defines WebSocket URL patterns
consumers.py	Defines WebSocket logic (connect, receive, disconnect)
chat.html	WebSocket frontend client
views.py	Renders the WebSocket chat page
urls.py	Maps URLs to Django views



q)Yes! To scale Django WebSockets across multiple servers, you need to use Redis as a message broker. Here’s how to integrate Redis with Django Channels.


🔹 Why Use Redis?
In-memory data store → Fast communication between multiple servers.
Avoids WebSocket messages being lost when running multiple Django instances.
Used for pub/sub messaging in Django Channels.


📂 Updated Folder Structure


websocket_project/      
│── chat/              
│   │── templates/     
│   │   └── chat.html  
│   │── consumers.py   # WebSocket Consumer
│   │── routing.py     # WebSocket routes
│   │── views.py       # Renders chat page
│── websocket_project/
│   │── asgi.py        # ASGI entry point for WebSockets
│   │── settings.py    # Django settings
│   │── urls.py        # Django URLs
│── manage.py          
│── db.sqlite3         
│── redis-server/      # Redis (installed separately)



1️⃣ Install Redis & Django Channels

pip install channels_redis



2️⃣ Update settings.py
Modify settings.py to use Redis as the Channel Layer.

INSTALLED_APPS = [
    "daphne",
    "channels",
    "chat",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

ASGI_APPLICATION = "websocket_project.asgi.application"

# 🔹 Configure Redis as Channel Layer
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],  # Redis running on localhost
        },
    },
}


3️⃣ Update asgi.py


Modify websocket_project/asgi.py to include WebSockets & Django Channels.

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websocket_project.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(chat.routing.websocket_urlpatterns)
        ),
    }
)



4️⃣ Modify WebSocket Consumer in chat/consumers.py
Enable real-time messaging across multiple servers using Redis channels.


import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "global_chat"
        self.room_group_name = f"chat_{self.room_name}"

        # Join chat group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave chat group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "chat_message", "message": message},
        )

    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))



5️⃣ Define WebSocket Routes in chat/routing.py

from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/$", ChatConsumer.as_asgi()),
]


