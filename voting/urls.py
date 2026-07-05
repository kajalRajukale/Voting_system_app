from django.urls import path
from . import views

app_name = 'voting'

urlpatterns = [
    path('', views.voting_page, name='voting_page'),
    path('cast-vote/', views.cast_vote, name='cast_vote'),
    path('next-student/', views.next_student, name='next_student'),
    path('machine-status/', views.machine_status, name='machine_status'),
    path('login/', views.AdminLoginView.as_view(), name='admin_login'),
    path('logout/', views.admin_logout_view, name='admin_logout'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('results/', views.result_page, name='result_page'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('export/excel/', views.export_excel, name='export_excel'),
    path('print/', views.print_result, name='print_result'),
    path('reset/', views.reset_election, name='reset_election'),
    path('api/charts-data/', views.charts_data, name='charts_data'),
]
