from django.shortcuts import render
from django.http.response import HttpResponse ,JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# @csrf_exempt
# def apage(request):
#     user:User=User.objects.get()
#     username=request.POST.get("username")
#     email=request.POST.get("email")
#     # print(email)
#     # print(password)
#     return JsonResponse({"UserName":user.username,"email":user.email})


@csrf_exempt
def apage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            return JsonResponse({"UserName": user.username, "email": user.email})
        else:
            return JsonResponse({"error": "User not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
