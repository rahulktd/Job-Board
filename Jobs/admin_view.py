from django.shortcuts import render, redirect
from Jobs.models import Reg, Job


def recruiter_view(request):
    data = Reg.objects.filter(is_recruiter=True)
    return render(request, 'Admin/view_recruiter_list.html', {"data": data})

def job_seeker_view(request):
    data = Reg.objects.filter(is_seeker=True)
    return render(request, 'Admin/view_employee_list.html', {"data": data})

def delete_recruiter(request, id):
    data = Reg.objects.get(id=id)
    data.delete()
    return redirect("recruiter_view")

def delete_employee(request, id):
    data = Reg.objects.get(id=id)
    data.delete()
    return redirect("job_seeker_view")

def posted_jobs_rec(request):
    data = Job.objects.all()
    return render(request, 'Admin/view_posted_jobs.html', {"data": data})

def delete_job(request, id):
    data = Job.objects.get(id=id)
    data.delete()
    return redirect("posted_jobs_rec")
