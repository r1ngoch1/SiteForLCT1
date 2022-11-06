from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category, DataBase1, tnved_types_rate_grouped1
from django.views.generic import ListView

from django.core.paginator import Paginator




def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    ratings = tnved_types_rate_grouped1.objects.all()[:5]
    ratings2 = tnved_types_rate_grouped1.objects.all()[5:10]
    ratings3 = tnved_types_rate_grouped1.objects.all()

    p = Paginator(ratings, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {
        'news':     news,
        'title': 'Список новостей',
        'categories': categories,
        'page_obj': page_obj,
        'rating' : ratings,
        'rating2' : ratings2,
    }

    return render(request, 'News/index.html',   context = context)
def Base(request):
    data_base1 = DataBase1.objects.all()
    p = Paginator(data_base1, 2000)
    # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'News/basedate.html', context)


def Base2(request):
    ratings3 = tnved_types_rate_grouped1.objects.all()
    p = Paginator(ratings3,1150)
    # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'News/basedate2.html', context)

def acc(request):

    return render(request, 'News/Account.html', context={} )









#def get_category(request, category_id):
 #   news = News.objects.filter(category_id = category_id)
 #   categories = Category.objects.all()
  #  category = Category.objects.get(pk = category_id)

 #   return render(request, 'news/category.html', {'news' : news, 'categories' : categories, 'category' : category})
