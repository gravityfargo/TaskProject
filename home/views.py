from django.shortcuts import render, redirect
from .forms import RegisterForm

# Main Site Room
def index(response):
    return render(response, "home/index.html", {})


# #   <!-- <a class="navbar-brand" href="{% url 'tasks:index' %}">TaskProject</a> -->
# def register(response):
#     form = RegisterForm()
#     if response.method == "POST":
#          form = RegisterForm(response.POST)
#     if form.is_valid():
#         form.save()
#         return redirect("/")
#     else:
#         return render(response, "/register.html", {"form":form})
