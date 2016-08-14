from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item
# Create your views here.
def home_page(request):
    # render will seach for home.html from templates directory in any apps directory
    # Then it builds a HttpResponse based on the content of the templates
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world/')
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    #items = Item.objects.all()
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html',{'items': items})

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
