from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import user

def index(req):
    return HttpResponse('My second project');

def help(req):
    my_dict = {'insert_me': "Help page from view"}
    return render(req, 'second_app/index.html', context=my_dict)
    
def users(req):
    user_list = user.objects.order_by('first_name')
    user_dict = {'access_record': user_list}
    return render(req, 'second_app/index.html', context=user_dict)
