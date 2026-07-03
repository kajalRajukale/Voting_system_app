from django.urls import path
from . import views

app_name = 'voting'

urlpatterns = [
    # Admin Auth
    path('login/', views.AdminLoginView.as_view(), name='admin_login'),
    path('logout/', views.admin_logout_view, name='admin_logout'),

    # Admin Dashboard
    path('dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),

    # Candidate Management
    path('candidates/', views.CandidateListView.as_view(), name='candidate_list'),
    path('candidates/add/', views.CandidateCreateView.as_view(), name='candidate_add'),
    path('candidates/<int:pk>/', views.CandidateDetailView.as_view(), name='candidate_detail'),
    path('candidates/<int:pk>/edit/', views.CandidateUpdateView.as_view(), name='candidate_edit'),
    path('candidates/<int:pk>/delete/', views.CandidateDeleteView.as_view(), name='candidate_delete'),

    # Public Voting
    path('', views.VotingPageView.as_view(), name='voting_page'),
    path('cast-vote/', views.cast_vote, name='cast_vote'),
    path('check-vote-status/', views.check_vote_status, name='check_vote_status'),

    # Results
    path('results/', views.ResultPageView.as_view(), name='result_page'),

    # AJAX Endpoints
    path('api/live-counter/', views.live_vote_counter, name='live_vote_counter'),
    path('api/charts-data/', views.charts_data, name='charts_data'),

    # Reports
    path('reports/pdf/', views.report_pdf, name='report_pdf'),
    path('reports/excel/', views.report_excel, name='report_excel'),
    path('reports/csv/', views.report_csv, name='report_csv'),
]
