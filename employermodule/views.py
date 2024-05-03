from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from jobseekermodule.models import JobApplication
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def jobpost(request):
    return render(request, 'employermodule/jobpost.html')


def employerlist(request):
    return render(request, 'employermodule/employerlist.html')


def add_job_details(request):
    if request.method == 'POST':
        work_title = request.POST.get('workTitle')
        salary_offered = request.POST.get('salaryOffered')
        job_type = request.POST.get('jobType')
        benefits = request.POST.get('benefits')
        education = request.POST.get('education')
        work_location = request.POST.get('workLocation')
        required_skills = request.POST.get('requiredSkills')
        experience = request.POST.get('experience')
        job_details = JobDetails(
            work_title=work_title,
            salary_offered=salary_offered,
            job_type=job_type,
            benefits=benefits,
            education=education,
            work_location=work_location,
            required_skills=required_skills,
            experience=experience,
        )
        job_details.save()
        return render(request, 'employermodule/datainserted.html')
    return render(request, 'employeerhomepage/jobpost.html')


def view_job_details(request):
    job_details_list = JobDetails.objects.all()
    return render(request, 'employermodule/view_job_details.html', {'job_details_list': job_details_list})


def edit_job_details(request, job_id):
    job_details = get_object_or_404(JobDetails, id=job_id)
    if request.method == 'POST':
        job_details.work_title = request.POST.get('workTitle')
        job_details.salary_offered = request.POST.get('salaryOffered')
        job_details.job_type = request.POST.get('jobType')
        job_details.benefits = request.POST.get('benefits')
        job_details.education = request.POST.get('education')
        job_details.work_location = request.POST.get('workLocation')
        job_details.required_skills = request.POST.get('requiredSkills')
        job_details.experience = request.POST.get('experience')
        job_details.save()
        return redirect('employermodule:view_job_details')
    return render(request, 'employermodule/edit_job_details.html', {'job_details': job_details})


def delete_job_details(request, job_id):
    job_details = get_object_or_404(JobDetails, id=job_id)
    if request.method == 'POST':
        job_details.delete()
        return redirect('employermodule:view_job_details')
    return render(request, 'employermodule/delete_job_details.html', {'job_details': job_details})


def job_applications(request):
    job_applications = JobApplication.objects.all()
    return render(request, 'employermodule/employerlist.html', {'job_applications': job_applications})


def accept_application(request, job_application_id):
    job_application = get_object_or_404(JobApplication, id=job_application_id)

    # Update the application status
    job_application.status = 'Accepted'
    job_application.save()

    # Retrieve associated EventDetails
    event_details = job_application.job_details

    # Get additional information (username and registered event)
    user_email = job_application.email  # Assuming email is used for identifying the user

    # Send acceptance email with user email and registered event details
    send_mail(
        'Application Accepted',
        f'Congratulations! "{job_application.name}" Your application for the Job "{JobDetails.job_type}" has been '
        f'accepted.',
        'avinash49922@gmail.com',  # Sender's email address
        [user_email],  # Recipient's email address
        fail_silently=False,
    )

    return redirect('employermodule:job_application_list')



def reject_application(request, job_application_id):
    job_application = get_object_or_404(JobApplication, id=job_application_id)

    # Update the application status
    job_application.status = 'Rejected'
    job_application.save()

    # Retrieve associated EventDetails
    event_details = job_application.event_details

    # Send rejection email
    send_mail(
        'Application Rejected',
        f'Dear "{job_application.name}", We regret to inform you that your application for the event "{event_details.event_title}" has been rejected.',
        'sakethkunuku205@gmail.com',  # Sender's email address
        [job_application.email],  # Recipient's email address
        fail_silently=False,
    )

    return redirect('employermodule:job_application_list')
