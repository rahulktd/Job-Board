from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from Jobs.filters import JobsFilter
from Jobs.forms import ProfileForm, FeedbackForm, JobPostForm, JobApplicationForm, JobApplicationReplyForm
from Jobs.models import Job, JobApplication, Feedback, Reg

@login_required
def jobs(request):
    job_list = Job.objects.all()
    job_filter = JobsFilter(request.GET, queryset=job_list)
    job_list = job_filter.qs

    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'JobSeeker/jobs_to.html', {"job_list": page_obj, "job_filter": job_filter})

@login_required
def apply_job(request, id):
    job = Job.objects.get(id=id)
    return redirect ('jobs')


@login_required
def application(request, id):
    job = Job.objects.get(id=id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_post = job
            application.job_seeker = request.user
            application.save()
            return redirect('jobs')
    else:
        form = JobApplicationForm()
    return render(request, 'JobSeeker/job_apply.html', {'form': form, 'job': job})

@login_required
def applied(request):
    user = request.user
    applied_jobs = JobApplication.objects.filter(job_seeker=user)
    return render(request, 'JobSeeker/applied_jobs.html', {'applied_jobs': applied_jobs})


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('seeker_dashboard')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'JobSeeker/profile.html', {'form': form})

@login_required
def jobseeker_feedback(request):
    u = request.user
    if request.method=='POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            obj = feedback_form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request,"Thank you for your feedback.")
            return redirect('jobseeker_feedback_view')
    else:
        feedback_form = FeedbackForm
    return render(request, 'JobSeeker/user_feedback.html', {'feedback_form': feedback_form})

@login_required
def jobseeker_feedback_view(request):
    u = request.user
    feedback=Feedback.objects.filter(user=u)
    return render(request,'JobSeeker/user_feedback_view.html',{'feedback':feedback})

@login_required
def reply_view(request):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        reply_v = request.POST.get('reply')
        feedback.reply = reply_v
        feedback.save()
        return redirect('reply_view', id=id)
    else:
        form = FeedbackForm()
    return render(request, 'JobSeeker/user_feedback_view.html', {'feedback': feedback})

@login_required
def fulltime(request):
    jobs = Job.objects.filter(type="full_time")
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'JobSeeker/fulltime.html',{"page_obj": page_obj})

@login_required
def parttime(request):
    jobs = Job.objects.filter(type="part_time")
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'JobSeeker/parttime.html',{"page_obj": page_obj})

@login_required
def internship(request):
    jobs = Job.objects.filter(type="internship")
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'JobSeeker/internship.html',{"page_obj": page_obj})

@login_required
def recruiter_view_jobseeker(request):
    data = Reg.objects.filter(is_recruiter=True)
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'JobSeeker/view_recruiters_jobseeker.html', {"page_obj": page_obj})


@login_required
def job_application_detail_js(request, id):
    job_application = JobApplication.objects.get(id=id)
    return render(request, 'JobSeeker/job_application_detail.html', {'job_application': job_application})

@login_required
def profile_view(request):
    u = request.user
    return render(request,'JobSeeker/profile_view.html',{'u':u})

@login_required
def response_recruiter(request,id):
    job_application = JobApplication.objects.get(id=id)
    if request.method == 'POST':
        form = JobApplicationReplyForm(request.POST)
        if form.is_valid():
            reply_message = form.cleaned_data['reply_message']
            job_application.reply_message = reply_message
            job_application.save()
    else:
        form = JobApplicationReplyForm()
    return render(request,'JobSeeker/response_recruiter.html',{'job_application': job_application, 'form': form})



