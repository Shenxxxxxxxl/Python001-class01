from django.shortcuts import render
from .models import Product, ProductComment
from django.db import connection
from django.db.models import Avg, Max, Min, Count, Sum
from datetime import datetime
def index(request):
    param = dict()
    keyWord = request.GET.get('keyWord')
    if keyWord:
        param['pagetitle__contains'] = keyWord
    q_date = request.GET.get('date')
    if q_date :
        cday = datetime.strptime(q_date, '%Y-%m-%d')
        param['release_time__year'] = cday.year
        param['release_time__month'] = cday.month
        param['release_time__day'] = cday.day
    products=Product.objects.filter(**param).order_by('position')#product_list
    result_p = {'product_list':products,'currentLi':'1'}
    if products:
        count_p = Product.objects.filter(**param).aggregate(Sum('pos_count'),Sum('neg_count'))
        count_c = count_p['pos_count__sum']+count_p['neg_count__sum']
        result_p['pos_rate'] = '%.2f' %(count_p['pos_count__sum']/count_c)
        result_p['neg_rate'] = '%.2f' %(count_p['neg_count__sum']/count_c)
        
    return render(request, 'index.html', result_p)

def comment(request):
    product_id = request.GET.get('product_id')
    param = dict()
    if product_id:
        param['product_id'] = product_id
    keyWord = request.GET.get('keyWord')
    if keyWord:
        param['content__contains'] = keyWord
    q_date = request.GET.get('date')
    if q_date :
        cday = datetime.strptime(q_date, '%Y-%m-%d')
        param['comment_time__year'] = cday.year
        param['comment_time__month'] = cday.month
        param['comment_time__day'] = cday.day
    comments=ProductComment.objects.filter(**param).order_by('comment_time')#product_list
    result_p = {'comment_list':comments,'currentLi':'2'}
    if comments:
        count_p = ProductComment.objects.filter(**param).aggregate(Sum('is_pos'))
        count_c = ProductComment.objects.filter(**param).count()
        print(f'count {count_c} pos_count{count_p}')
        result_p['pos_rate'] = '%.2f' %(count_p['is_pos__sum']/count_c)
        result_p['neg_rate'] = '%.2f' %(1.0-float(result_p['pos_rate']))
    return render(request, 'comment.html', result_p)
    