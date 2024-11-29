from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem
from .forms import MenuItemForm

def index(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/index.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MenuItemForm()
    return render(request, 'menu/add_item.html', {'form': form})

def update_item(request, id):
    item = get_object_or_404(MenuItem, id=id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'menu/update_item.html', {'form': form})

def delete_item(request, id):
    item = get_object_or_404(MenuItem, id=id)
    item.delete()
    return redirect('index')
