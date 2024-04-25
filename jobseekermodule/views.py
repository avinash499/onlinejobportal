from employermodule.models import JobDetails


def viewjobs(request):
    return render(request, 'jobseekermodule/viewjobs.html')


def job_details_list(request):
    job_details_list = JobDetails.objects.all()
    return render(request, 'jobseekermodule/viewjobs.html', {'job_details_list': job_details_list})


def job_application_list(request):
    return render(request, 'jobseekermodule/job_application_list.html')


def job_applications(request):
    job_applications = JobApplication.objects.all()
    return render(request, 'job_applications.html', {'job_applications': job_applications})


from django.shortcuts import render, redirect
from .models import JobApplication
from .forms import JobApplicationForm


def submit_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jobseekerhomepage')
    else:
        form = JobApplicationForm()
    return render(request, 'submit_application.html', {'form': form})
