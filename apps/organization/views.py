from django.shortcuts import render

from django.views import View

from organization.models import CourseOrg, CityDict


class OrgView(View):
    '''课程列表'''

    def get(self, request):
        # 列出所有课程机构
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        # 列出所有城市
        all_citys = CityDict.objects.all()

        return render(request, 'org-list.html', {
            "all_orgs": all_orgs,
            "org_nums": org_nums,
            "all_citys": all_citys,

        })


class TeacherView(View):
    pass
