from django.db import models
from django.contrib.auth.models import User

class Naver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    birthdate = models.DateField(null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    job_role = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Naver'
        verbose_name_plural='Navers'
        ordering=['id']

    def __str__(self):
        return self.name

class Projeto(models.Model):
    naver = models.ForeignKey(Naver, on_delete=models.CASCADE, related_name='projetos')
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name='Projeto'
        verbose_name_plural='Projetos'
        ordering=['id']

    def __str__(self):
        return self.name
