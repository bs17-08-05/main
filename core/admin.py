from django.contrib import admin
from django.contrib.admin import AdminSite
from django.http import HttpResponse

from .models import Horecama, Goods, Order, GoodsQuantityOrder, User, Courier
from .reports import make_csv_file

class AdminSiteReports(AdminSite):
    index_template = 'admin/index.html'
    def get_urls(self):
        from django.urls import path
        urls = super(AdminSiteReports, self).get_urls()
        urls += [
            path('business_report/', self.admin_view(self.business)),
        ]
        return urls
    
    def business(self, request):
        orders = Order.objects.all()
        print('test')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="business_report.csv"'
        return make_csv_file(orders, response)


class TemplateReportChange(admin.ModelAdmin):
    change_form_template = 'admin/report_template.html'


admin_site_reports = AdminSiteReports()
admin_site_reports.register(Horecama)
admin_site_reports.register(Goods)
admin_site_reports.register(Order)
admin_site_reports.register(GoodsQuantityOrder)
admin_site_reports.register(User)
admin_site_reports.register(Courier)
