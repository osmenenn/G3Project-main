from django.shortcuts import render
from .models import Menu, User, Pizza, Topping
# Create your views here.


#menu template  
# menus = [
#     {'id': 2422, 'name': 'Veggie'}, 
#     {'id': 2222, 'name': 'Vggie'}, 
#     {'id': 2322, 'name': 'Vegie'}, 
#     {'id': 2522, 'name': 'Vgie'}, 
#     {'id': 2622, 'name': 'Veie'}, 
#     {'id': 2722, 'name': 'Vegge'}, 
#     {'id': 2822, 'name': 'Veggi'}, 
#     {'id': 2922, 'name': 'egge'}, 
#     {'id': 2122, 'name': 'egi'}, 
    
# ]

def home(request):
    menus = Menu.objects.all()
    context = {'menus': menus}
    return render(request, 'blog/home.html', context)

def menu(request, pk):
    menu = Menu.objects.get(id=pk)
    context = {'menu': menu}
    return render(request, 'blog/menu.html', context)


def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user_detail.html', {'user': user})

def pizza_detail(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    return render(request, 'pizza_detail.html', {'pizza': pizza})


def topping_detail(request, topping_id):
    topping = Topping.objects.get(id=topping_id)
    return render(request, 'topping_detail.html', {'topping': topping})
