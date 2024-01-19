from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title':'Home - Основная',
        'content': 'Магазин товаров для умного дома'
    }


    return render(request, 'main/index.html', context)



def about(request):
    context = {
        'title': 'Home - О нашем сайте',
        'content': 'О нашей работе',
        'text_on_page': 'Вид деятельности нашей компании',
    }

    return render(request, 'main/about.html', context)