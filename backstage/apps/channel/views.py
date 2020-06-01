from django.shortcuts import render
from django.http import response
# Create your views here.
from httplib2 import Response
import time
import hashlib

def test(request):
    return response.HttpResponse('ssss')

from xadmin.views import CommAdminView


class TestView(CommAdminView):
    def get(self, request):
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "移动直播生成器"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        # 下面你可以接着写你自己的东西了，写完记得添加到context里面就可以
        return render(request,'test.html', context)  # 最后指定自定义的template模板，并返回context

    def get_url(self, app_name, stream_name):
        t = time.time() + 172800
        keytime = str(int(t))
        hashstring = "/" + app_name + "/" + stream_name + "-" + keytime + "-0-0-" + app_name + "alipush"
        m = hashlib.md5()
        m.update(hashstring.encode("utf8"))
        mm = m.hexdigest()
        print(mm)
        push = "rtmp://" + app_name + "alipush.v.myalicdn.com/" + app_name + "/" + stream_name + "?auth_key=" + keytime + "-0-0-" + mm
        return push

    def post(self, request):
        print('mmmmmmmmmmmmm')
        app_name = request.POST.get('app')
        stream_name = request.POST.get('name')
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "移动直播生成器"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        # 下面你可以接着写你自己的东西了，写完记得添加到context里面就可以了
        context['app_name'] = app_name
        context['streaa_name'] = stream_name
        context['push'] = self.get_url(app_name,stream_name)
        return render(request,'test.html', context)  # 最后指定自定义的template模板，并返回context

