from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from Jobs.filters import JobSeekerFilter
from Jobs.forms import JobPostForm, FeedbackForm, JobApplicationReplyForm
from Jobs.models import Job, JobApplication, Feedback, Reg


@login_required
def create_job_post(request):
    if request.method == 'POST':
        job_post_form = JobPostForm(request.POST)
        if job_post_form.is_valid():
            job_post = job_post_form.save(commit=False)
            job_post.posted_by = request.user
            job_post.save()
            messages.success(request, 'Job post created successfully')
            return redirect('jobs_posted')
    else:
        job_post_form = JobPostForm()
    return render(request, 'Employer/create_job.html', {'job_post_form': job_post_form})

@login_required
def jobs_posted(request):
    jobs = Job.objects.filter(posted_by=request.user)
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'Employer/posted_jobs.html',{'jobs':page_obj})

@login_required
def applied_job_seeker(request,id):
    job = Job.objects.get(id=id)
    applications = job.jobapplication_set.all()
    return render(request, 'Employer/rec_applications.html', {'job': job, 'applications': applications})

@login_required
def delete_job_rec(request, id):
    data = Job.objects.get(id=id)
    data.delete()
    return redirect("jobs_posted")

@login_required
def recruiter_feedback(request):
    u = request.user
    if request.method=='POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            obj = feedback_form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request,"Thank you for your feedback.")
            return redirect('recruiter_feedback_view')
    else:
        feedback_form = FeedbackForm
    return render(request, 'Employer/recruiter_feedback.html', {'feedback_form': feedback_form})
@login_required
def recruiter_feedback_view(request):
    u = request.user
    feedback=Feedback.objects.filter(user=u)
    return render(request,'Employer/recruiter_feedback_view.html',{'feedback':feedback})

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
    return render(request, 'Employer/recruiter_feedback_view.html', {'feedback': feedback})


@login_required
def job_application_detail(request, id):
    job_application = JobApplication.objects.get(id=id)
    if request.method == 'POST':
        form = JobApplicationReplyForm(request.POST)
        if form.is_valid():
            reply_message = form.cleaned_data['reply_message']
            job_application.reply_message = reply_message
            job_application.save()
            return redirect("jobs_posted")
    else:
        form = JobApplicationReplyForm()
    return render(request, 'Employer/response_to_application.html', {'job_application': job_application,'form': form})


@login_required
def recruiter_responses(request):
    job_applications = JobApplication.objects.exclude(reply_message__isnull=True)
    return render(request, 'Employer/recruiter_messages_jobseeker.html', {'job_applications':job_applications})

@login_required
def registered_for_job(request):
    data = Reg.objects.filter(is_seeker=True)
    seek_filter = JobSeekerFilter(request.GET, queryset=data)
    data = seek_filter.qs
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Employer/registered_for_job.html', {"data": page_obj, "seek_filter": seek_filter})
