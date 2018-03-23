from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.utils.timezone import now


def index(request):
    context = {}
    template = loader.get_template('index.html')
    html_str = template.render(context,request)
    return HttpResponse(html_str)

class Student(object):
    def name(self):
        return '对象方法'
def index2(request):
    my_dict = {"name":"字典","name2":"字典2"}
    my_obj = Student()
    my_list = ["列表1","列表2","列表3","列表4"]

    datas = {
        'key01':5,
        'my_dict':my_dict,
        'my_obj':my_obj,
        'my_list':my_list,
    }
    return render(request,'index2.html',datas)


def index3(request):
    my_dict = {"name": "字典", "name2": "字典2"}
    my_obj = Student()
    my_list = ["列表1", "列表2", "列表3", "列表4"]
    my_date = now()
    datas = {
        'key01': 5,
        'my_dict': my_dict,
        'my_obj': my_obj,
        'my_list': my_list,
        'my_date':my_date,

    }
    return render(request,'index3.html',datas)


def inherit(request):
    return render(request,'child.html')


def index4(request):
    my_html='<font color="red">红色</font>'' \
    ''<font color="blue">蓝色</font>'
    datas = {
        'my_html' : my_html,
    }
    return render(request,'index4.html',datas)