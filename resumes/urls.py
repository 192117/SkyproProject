from django.urls import path

from resumes.views import ResumeDetailView, ResumeListView

urlpatterns = [
    path('', ResumeListView.as_view(), name='resumes_list'),
    path('<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),
]
