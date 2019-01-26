from django.core.paginator import PageNotAnInteger
from django.shortcuts import render

from django.views import View
from pure_pagination import Paginator

from organization.models import CourseOrg, CityDict


class OrgView(View):
    '''课程列表'''

    def get(self, request):
        # 列出所有课程机构
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        # 列出所有城市
        all_citys = CityDict.objects.all()
        # 对课程机构进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里从allorg中取出5个出来  每页显示5个
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)
        return render(request, 'org-list.html', {
            "all_orgs": orgs,
            "org_nums": org_nums,
            "all_citys": all_citys,

        })


class TeacherView(View):
    pass
