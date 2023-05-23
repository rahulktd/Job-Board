from django.urls import path
from Jobs import views, employer_view, admin_view, jobseeker_view

urlpatterns = [
    path('', views.index, name='index'),
    path('registration',views.registration,name='registration'),
    path('user_login/',views.user_login,name='user_login'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('employee_registration',views.employee_registration,name='employee_registration'),
    path('seeker_dashboard',views.seeker_dashboard,name='seeker_dashboard'),
    path('employer_dashboard',views.employer_dashboard,name='employer_dashboard'),
    path('logout_view', views.logout_view, name='logout_view'),


    path('recruiter_view', admin_view.recruiter_view, name='recruiter_view'),
    path('job_seeker_view', admin_view.job_seeker_view, name='job_seeker_view'),
    path('delete_employee/<int:id>/', admin_view.delete_employee, name='delete_employee'),
    path('delete_recruiter/<int:id>/', admin_view.delete_recruiter, name='delete_recruiter'),
    path('posted_jobs_rec', admin_view.posted_jobs_rec, name='posted_jobs_rec'),
    path('delete_job/<int:id>/', admin_view.delete_job, name='delete_job'),
    path('reply_feedback/<int:id>/', admin_view.reply_feedback, name='reply_feedback'),
    path('admin_feedback_view', admin_view.admin_feedback_view, name='admin_feedback_view'),
    path('admin_feedback_reply', admin_view.admin_feedback_reply, name='admin_feedback_reply'),



    path('create_job_post',employer_view.create_job_post,name='create_job_post'),
    path('jobs_posted',employer_view.jobs_posted,name='jobs_posted'),
    path('applied_job_seeker/<int:id>/',employer_view.applied_job_seeker,name='applied_job_seeker'),
    path('delete_job_rec/<int:id>/',employer_view.delete_job_rec,name='delete_job_rec'),
    path('recruiter_feedback',employer_view.recruiter_feedback,name='recruiter_feedback'),
    path('recruiter_feedback_view',employer_view.recruiter_feedback_view,name='recruiter_feedback_view'),
    path('reply_view',employer_view.reply_view,name='reply_view'),
    path('job_application_detail/<int:id>/',employer_view.job_application_detail,name='job_application_detail'),
    path('recruiter_responses',employer_view.recruiter_responses,name='recruiter_responses'),



    path('jobs', jobseeker_view.jobs, name='jobs'),
    path('apply_job/<int:id>/', jobseeker_view.apply_job, name='apply_job'),
    path('application/<int:id>/', jobseeker_view.application, name='application'),
    path('applied/', jobseeker_view.applied, name='applied'),
    path('profile', jobseeker_view.profile, name='profile'),
    path('jobseeker_feedback', jobseeker_view.jobseeker_feedback, name='jobseeker_feedback'),
    path('jobseeker_feedback_view', jobseeker_view.jobseeker_feedback_view, name='jobseeker_feedback_view'),
    path('fulltime', jobseeker_view.fulltime, name='fulltime'),
    path('parttime', jobseeker_view.parttime, name='parttime'),
    path('internship', jobseeker_view.internship, name='internship'),
    path('recruiter_view_jobseeker', jobseeker_view.recruiter_view_jobseeker, name='recruiter_view_jobseeker'),
    path('job_application_detail/<int:id>/', jobseeker_view.job_application_detail, name='job_application_detail'),
    path('profile_view', jobseeker_view.profile_view, name='profile_view'),

]