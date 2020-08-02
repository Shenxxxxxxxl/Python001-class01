from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Comment
from django.core import serializers
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    keyWord = request.GET.get('keyWord')
    param = {'rating__gt' : 3}
    commensts = Comment.objects.filter(**param).extra(select={'comment_time':'DATE_FORMAT(comment_time, "%%Y-%%m-%%d")'}).all().order_by('comment_time')
    context = {
        'commensts':commensts,
    }
    print(len(commensts))
    return render(request,'index.html',context)

def query(request):
    keyWord = request.POST.get('keyWord')
    param = {'rating__gt' : 3}
    if keyWord:
        print(keyWord)
        param['content__contains'] = keyWord
    commensts = Comment.objects.filter(**param).extra(select={'comment_time':'DATE_FORMAT(comment_time, "%%Y-%%m-%%d")'}).all().order_by('comment_time')
    context = {
        'commensts':commensts,
    }
    html = render_to_string('table.html', context)
    result = {'status': 1, 'msg': '','html': html}
    return JsonResponse(result)
