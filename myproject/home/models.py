from django.db import models

class Department(models.Model):
    department_code = models.CharField(max_length=10, primary_key=True, unique=True)
    department_name = models.CharField(max_length=50)
    valid = models.BooleanField(default=True)

    class Meta:
        db_table = 'departments'

    def save(self, *args, **kwargs):
        if not self.department_code:
            last_dept = Department.objects.order_by('-department_code').first()
            if last_dept:
                last_code = int(last_dept.department_code) + 1
            else:
                last_code = 1  # Start from 1, resulting in "0001"
            self.department_code = f'{last_code:04d}'  # Format as four digits with leading zeros
        super().save(*args, **kwargs)

    def __str__(self):
        return self.department_name

class Job(models.Model):
    job_code = models.CharField(max_length=10, primary_key=True, unique=True)
    job_name = models.CharField(max_length=50)
    valid = models.BooleanField(default=True)

    class Meta:
        db_table = 'jobs'

    def save(self, *args, **kwargs):
        if not self.job_code:
            last_job = Job.objects.order_by('-job_code').first()
            if last_job:
                last_code = int(last_job.job_code) + 1
            else:
                last_code = 1  # Start from 1, resulting in "0001"
            self.job_code = f'{last_code:04d}'  # Format as four digits with leading zeros
        super().save(*args, **kwargs)

    def __str__(self):
        return self.job_name

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_code = models.CharField(max_length=10, unique=True)
    employee_first_name = models.CharField(max_length=50)
    employee_last_name = models.CharField(max_length=50)
    gender = models.SmallIntegerField()
    department_code = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='department_code')
    job_code = models.ForeignKey(Job, on_delete=models.CASCADE, db_column='job_code')
    birthday = models.DateField()
    valid = models.BooleanField(default=True)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f"{self.employee_first_name} {self.employee_last_name}"