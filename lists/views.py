from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List
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


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html',{'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))



def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))
