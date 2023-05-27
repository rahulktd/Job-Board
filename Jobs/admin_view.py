from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from Jobs.filters import RecruiterFilter, JobSeekerFilter
from Jobs.models import Reg, Job, Feedback

@login_required
def recruiter_view(request):
    rec_list = Reg.objects.filter(is_recruiter=True)
    rec_filter = RecruiterFilter(request.GET, queryset=rec_list)
    rec_list = rec_filter.qs
    paginator = Paginator(rec_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Admin/view_recruiter_list.html', {"rec_list": page_obj, "rec_filter": rec_filter})

@login_required
def job_seeker_view(request):
    data = Reg.objects.filter(is_seeker=True)
    seek_filter = JobSeekerFilter(request.GET, queryset=data)
    data = seek_filter.qs
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Admin/view_employee_list.html', {"data": page_obj, "seek_filter": seek_filter})
@login_required
def delete_recruiter(request, id):
    data = Reg.objects.get(id=id)
    data.delete()
    return redirect("recruiter_view")

@login_required
def delete_employee(request, id):
    data = Reg.objects.get(id=id)
    data.delete()
    return redirect("job_seeker_view")

@login_required
def posted_jobs_rec(request):
    data = Job.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Admin/view_posted_jobs.html', {"data": page_obj})

@login_required
def delete_job(request, id):
    data = Job.objects.get(id=id)
    data.delete()
    return redirect("posted_jobs_rec")

@login_required
def admin_feedback_view(request):
    feedback = Feedback.objects.all()
    paginator = Paginator(feedback, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'Admin/admin_feedback.html',{'feedback':page_obj})

@login_required
def reply_feedback(request, id):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply=r
        feedback.save()
        messages.info(request,'Reply send')
        return redirect('admin_feedback_view')
    return render(request,'Admin/reply_feedback_admin.html',{'feedback':feedback})

@login_required
def admin_feedback_reply(request):
    return render(request,'Admin/reply_feedback_admin.html')
