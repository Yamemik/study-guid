from django.db import models


class Organization(models.Model):
    TOKEN_IS_EXPIRED = 'token is expired'

    name = models.CharField(max_length=200)
    token = models.CharField(max_length=500, unique=True, default=TOKEN_IS_EXPIRED)
    end_date = models.DateTimeField('date of action')
    description = models.CharField(max_length=500, blank=True)
    avatar_url = models.ImageField(upload_to='main/static/avatars')

    def __str__(self):
        return self.name


class Student(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    fio = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.fio


class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    date = models.DateTimeField('date of achievement')
    data = models.JSONField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.date










