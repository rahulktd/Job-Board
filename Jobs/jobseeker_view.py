from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Jobs.filters import JobsFilter
from Jobs.forms import ProfileForm, FeedbackForm, JobPostForm, JobApplicationForm
from Jobs.models import Job, JobApplication, Feedback, Reg


# def jobs(request):
#     data = Job.objects.all()
#     return render(request, 'JobSeeker/jobs_to.html', {"data": data})

@login_required
# def jobs(request):
#     job_list = Job.objects.all()
#     job_filter = JobsFilter(request.GET, queryset=job_list)
#     job_list = job_filter.qs
#     return render(request, 'JobSeeker/jobs_to.html', {"job_list": job_list, "job_filter": job_filter})

def jobs(request):
    job_list = Job.objects.all()
    job_filter = JobsFilter(request.GET, queryset=job_list)
    job_list = job_filter.qs
    return render(request, 'JobSeeker/jobs_to.html', {"job_list": job_list, "job_filter": job_filter})

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
    feedback_form = FeedbackForm
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
    return render(request,'JobSeeker/fulltime.html',{'jobs':jobs})

@login_required
def parttime(request):
    jobs = Job.objects.filter(type="part_time")
    return render(request,'JobSeeker/parttime.html',{'jobs':jobs})

@login_required
def internship(request):
    jobs = Job.objects.filter(type="internship")
    return render(request,'JobSeeker/internship.html',{'jobs':jobs})

@login_required
def recruiter_view_jobseeker(request):
    data = Reg.objects.filter(is_recruiter=True)
    return render(request, 'JobSeeker/view_recruiters_jobseeker.html', {"data": data})
