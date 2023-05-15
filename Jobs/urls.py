from django.urls import path
from Jobs import views, employer_view, admin_view, jobseeker_view

urlpatterns = [
    path('', views.index, name='index'),
    path('registration',views.registration,name='registration'),
    path('user_login',views.user_login,name='user_login'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('employee_registration',views.employee_registration,name='employee_registration'),
    path('seeker_dashboard',views.seeker_dashboard,name='seeker_dashboard'),
    path('employer_dashboard',views.employer_dashboard,name='employer_dashboard'),

    path('recruiter_view', admin_view.recruiter_view, name='recruiter_view'),
    path('job_seeker_view', admin_view.job_seeker_view, name='job_seeker_view'),
    path('delete_employee/<int:id>/', admin_view.delete_employee, name='delete_employee'),
    path('delete_recruiter/<int:id>/', admin_view.delete_recruiter, name='delete_recruiter'),
    path('posted_jobs_rec', admin_view.posted_jobs_rec, name='posted_jobs_rec'),
    path('delete_job/<int:id>/', admin_view.delete_job, name='delete_job'),

    path('create_job_post',employer_view.create_job_post,name='create_job_post'),
    path('jobs_posted',employer_view.jobs_posted,name='jobs_posted'),

    path('jobs', jobseeker_view.jobs, name='jobs'),
    path('apply_job/<int:id>/', jobseeker_view.apply_job, name='apply_job'),
    path('application/<int:id>/', jobseeker_view.application, name='application'),
    path('submit_application/<int:id>/', jobseeker_view.submit_application, name='submit_application'),
    path('applied', jobseeker_view.applied, name='applied'),
    path('profile', jobseeker_view.profile, name='profile'),

]