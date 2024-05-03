from django.db import models
from django.core.mail.backends.smtp import EmailBackend as DjangoEmailBackend


# Create your models here.
class CustomEmailBackend(DjangoEmailBackend):
    def open(self):
        if self.connection:
            return False
        try:
            self.connection = self.connection_class(self.host, self.port, timeout=self.timeout,
                                                    local_hostname=self.local_hostname, **self.kwargs)
            if self.use_tls:
                self.connection.ehlo()
                if self.use_ssl or self.connection.has_extn('starttls'):
                    self.connection.starttls()  # Start TLS without passing keyfile
                    self.connection.ehlo()  # Re-identify ourselves over TLS connection
            return True
        except Exception:
            if not self.fail_silently:
                raise


class JobDetails(models.Model):
    work_title = models.CharField(max_length=255)
    salary_offered = models.CharField(max_length=255)
    JOB_TYPES = [
        ('fulltime', 'Full-time'),
        ('parttime', 'Part-time'),
        ('contract', 'Contract'),
    ]
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    benefits = models.TextField()
    education = models.CharField(max_length=255)
    work_location = models.CharField(max_length=255)
    required_skills = models.TextField()
    experience = models.TextField(max_length=255)

    def __str__(self):
        return self.work_title
