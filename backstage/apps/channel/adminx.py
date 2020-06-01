# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from xlrd import open_workbook
import xadmin
from xadmin import views
from channel.models import Channel,Server,Yangshi,Weishi,Jiaoyu,Qita
from channel.views import TestView   #从你的app的view里引入你将要写的view，你也可以另外写一个py文件，把后台的view集中在一起方便管理
'''
全局样式设置，头标题，脚标题。
'''
class GlobalSetting(object):
    site_title="频道后台管理"
    site_footer="央视网"
    # menu_style = 'accordion' #设置app下拉展开

    """
    自定义页面
    """
    def get_site_menu(self):  #名称不能改
        return [
            {
                # 'title': '测试的',
                # 'icon': 'fa fa-bar-chart-o',
                'menus': (
                    {
                        'title': '移动直播生成器',    #这里是你菜单的名称
                        'url': '/xadmin/test_view',     #这里填写你将要跳转url
                        # 'icon': 'fa fa-cny'     #这里是bootstrap的icon类名，要换icon只要登录bootstrap官网找到icon的对应类名换上即可
                    },
                    # {
                    #     'title': '测试子菜单2',
                    #     'url': 'http://www.taobao.com',
                    #     'icon': 'fa fa-cny'
                    # }
                )
            }
        ]


class XadminChannel(object):
    import_excel = True
    list_display = ['name','bianmaqi','jieru','type','pindao_id','beizhu']

    # 每页显示多少个
    list_per_page = 20
    # 配置在哪些字段搜索
    search_fields = ['name','bianmaqi','jieru','type']
    # 配置过滤字段
    list_filter = ['name', 'type']
    # 导出字段
    list_export_fields = ('name','bianmaqi','jieru','type','pindao_id','beizhu')

    def excelmodel(self,name,bianmaqi,jieru,type,pinda_id,beizhu):
        if type.startswith('央视'):
            channel = Yangshi()
            channel.name = name
            channel.bianmaqi = bianmaqi
            channel.jieru = jieru
            channel.pindao_id = pinda_id
            channel.beizhu = beizhu
            channel.save()
        elif type.startswith('地方') or type.startswith('卫视'):
            channel = Weishi()
            channel.name = name
            channel.bianmaqi = bianmaqi
            channel.jieru = jieru
            channel.pindao_id = pinda_id
            channel.beizhu = beizhu
            channel.save()
        elif type.startswith('教育'):
            channel = Jiaoyu()
            channel.name = name
            channel.bianmaqi = bianmaqi
            channel.jieru = jieru
            channel.pindao_id = pinda_id
            channel.beizhu = beizhu
            channel.save()
        elif type.startswith('其它'):
            channel = Qita()
            channel.name = name
            channel.bianmaqi = bianmaqi
            channel.jieru = jieru
            channel.pindao_id = pinda_id
            channel.beizhu = beizhu
            channel.save()
    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            execl_file = request.FILES.get('excel')
            wb = open_workbook(filename=None, file_contents=request.FILES['excel'].read())
            table = wb.sheets()[0]
            # sheet1 = wb.sheet_by_index(0)
            rows = table.nrows  #获取行数
            cols = table.ncols  #获取列数
            for r in range(1,rows):
                name = table.cell(r,0).value
                bianmaqi = table.cell(r,1).value
                jieru = table.cell(r, 2).value
                type = table.cell(r, 3).value
                pindao_id = table.cell(r, 4).value
                beizhu = table.cell(r, 5).value
                try:
                    a = Channel.objects.filter(name=name)
                    if a:
                        print(name  + "  存在")
                        continue
                    elif name == None or name == '':
                        continue
                    else:
                        print(name)
                        channel = Channel()
                        channel.name = name
                        channel.bianmaqi = bianmaqi
                        channel.type = type
                        channel.jieru = jieru
                        channel.save()
                        self.excelmodel(name, bianmaqi, jieru, type,pindao_id,beizhu)
                except:
                    pass
            # print(sheet1.rcols)
            return HttpResponseRedirect('http://127.0.0.1:8000/channel/channel/')
        print(4444444)
        return super(XadminChannel, self).post(request, args, kwargs)

class YangshiXadmin(object):
    list_display = ['name', 'bianmaqi', 'jieru','pindao_id','beizhu']
    search_fields = ['name', 'bianmaqi', 'jieru']
    # 导出字段
    list_export_fields = ('name', 'bianmaqi', 'jieru', 'pindao_id', 'beizhu')
    # 每页显示多少个
    list_per_page = 20


class WeishiXadmin(object):
    list_display = ['name', 'bianmaqi', 'jieru','pindao_id','beizhu']
    search_fields = ['name', 'bianmaqi', 'jieru']
    # 每页显示多少个
    list_per_page = 20


class JiaoyuXadmin(object):
    list_display = ['name', 'bianmaqi', 'jieru','pindao_id','beizhu']
    search_fields = ['name', 'bianmaqi', 'jieru',]
    # 每页显示多少个
    list_per_page = 20


class QitaXadmin(object):
    list_display = ['name', 'bianmaqi', 'jieru','pindao_id','beizhu']
    search_fields = ['name', 'bianmaqi', 'jieru']
    # 每页显示多少个
    list_per_page = 20


class XadminServer(object):
    import_excel = True
    list_display = ['ip','jifang','type','jiankong']
    # 导出字段
    list_export_fields = ('ip','jifang','type','jiankong')
    # 每页显示多少个
    list_per_page = 20

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            execl_file = request.FILES.get('excel')
            wb = open_workbook(filename=None, file_contents=request.FILES['excel'].read())
            table = wb.sheets()[0]
            # sheet1 = wb.sheet_by_index(0)
            rows = table.nrows  #获取行数
            cols = table.ncols  #获取列数
            for r in range(1,rows):
                ip = table.cell(r,0).value
                jifang = table.cell(r,1).value
                type = table.cell(r, 2).value
                jiankong = table.cell(r, 3).value
                server = Server()
                server.ip = ip
                server.jifang = jifang
                server.type = type
                server.jiankong = jiankong
                server.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/channel/server/')
        print(4444444)
        return super(XadminServer, self).post(request, args, kwargs)




xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register_view(r'test_view/$', TestView, name='bug_report')
xadmin.site.register(Channel, XadminChannel)
xadmin.site.register(Yangshi, YangshiXadmin)
xadmin.site.register(Weishi, WeishiXadmin)
xadmin.site.register(Jiaoyu, JiaoyuXadmin)
xadmin.site.register(Qita, QitaXadmin)
xadmin.site.register(Server,XadminServer)
