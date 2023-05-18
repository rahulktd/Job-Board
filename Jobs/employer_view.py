from django.contrib import messages
from django.shortcuts import render, redirect

from Jobs.forms import JobPostForm
from Jobs.models import Job, JobApplication


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

def jobs_posted(request):
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request,'Employer/posted_jobs.html',{'jobs':jobs})

def applied_job_seeker(request,id):
    # applied_jobs = JobApplication.objects.all()
    # return render(request, 'Employer/rec_applications.html', {'applied_jobs': applied_jobs})
    # job = Job.objects.get(id=id)
    # applications = JobApplication.objects.filter(job_post=job)
    # return render(request, 'Employer/rec_applications.html', {'job': job, 'applications': applications})
    job = Job.objects.get(id=id)
    applications = job.jobapplication_set.all()
    return render(request, 'Employer/rec_applications.html', {'job': job, 'applications': applications})

def delete_job_rec(request, id):
    data = Job.objects.get(id=id)
    data.delete()
    return redirect("jobs_posted")
