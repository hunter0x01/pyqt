from django.db import models

# Create your models here.
class Member(models.Model):
	m_name = models.CharField(max_length=100)
	m_major = models.CharField(max_length=100)
	m_age = models.IntegerField(default=0)
	m_grade = models.IntegerField(default=0)
	m_gender = models.CharField(max_length=30)


	def __str__(self):
		return self.m_name


	