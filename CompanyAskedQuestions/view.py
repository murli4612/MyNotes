from django.http JsonResponse

counter = {"value" : 0}

def get_counter(request):
    return JsonResponse (counter)

def update_counter (request):
    global counter
    if request.method == 'POST':
        data = json.loads(request.body)
        action = data.get("action")
        if action == "increment":
            counter["value"] +=1
        elif action =="decrement":
            counter["value"] -=1
        return JsonResponse(counter)
            