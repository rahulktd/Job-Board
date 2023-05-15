from django.shortcuts import render, redirect

from Jobs.forms import ProfileForm
from Jobs.models import Job, JobApplication


def jobs(request):
    data = Job.objects.all()
    return render(request, 'JobSeeker/jobs_to.html', {"data": data})

def apply_job(request, id):
    job = Job.objects.get(id=id)
    return redirect ('jobs')

def application(request,id):
    job = Job.objects.get(id=id)
    return render(request, 'JobSeeker/job_apply.html', {"job": job})

def submit_application(request,id):
    if request.method == 'POST':
        job = Job.objects.get(id=id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        cv = request.FILES.get('cv')
        job_application = JobApplication.objects.create(
            name=name,
            email=email,
            cv=cv,
        )
        return redirect('jobs')
    else:
        return redirect('application')

def applied(request):
    # user = request.user
    # applied_jobs = JobApplication.objects.all()
    # return render(request, 'JobSeeker/applied_jobs.html', {'applied_jobs': applied_jobs})
    user = request.user
    applied_jobs = JobApplication.objects.filter(job_seeker=user)
    return render(request, 'JobSeeker/applied_jobs.html', {'applied_jobs': applied_jobs})

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


