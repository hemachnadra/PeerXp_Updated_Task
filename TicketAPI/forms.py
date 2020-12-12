from django.forms import forms as fm
from django.contrib.auth.models import User
from django import forms 



class LoginForm(forms.Form):
		username=forms.CharField(max_length=20)
		password=forms.CharField(max_length=32, widget=forms.PasswordInput)




	
class TicketForm(forms.ModelForm):
	DEPT=[
	('PWSLab devops support','PWSLab DevOps Support'),
	('isupport','iSupport')
	]

	CATEGORY=[
	('-none-','-None-'),
	('new Project CI/CD pipeline setup','NEW Project CI/CD Pipeline Setup'),
	('update CI/CD Pipeline configuration','Update CI/CD Pipeline Configuration'),
	('devdecops pipeline setup','DevSecOps Pipeline Setup'),
	('CI/CD pipeline failure','CI/CD pipeline failure'),
	('automated deployment failure','Automated Deployment failure'),
	('docker and containers','Docker and Containers'),
	('kubernetes deployments (like EKS/GCP)','Kubernetes Deployments (like EKS/GCP)'),
	('git source control','Git Source control'),
	('PWSLab server not responding (502/503 errors)','PWSLab server not responding (502/503 errors)'),
	('PWSLab runner not working (jobs not running)','PWSLab Runner not working (jobs not running)'),
	('user management and project access','User management and Project access'),
	('cloud integration consultation - AWS/GCP/Azure','Cloud Integration Consultation - AWS/GCP/Azure'),
	('others','Others')
	]

	PRIORITY=[
	('-none-','-None-'),
	('high','High - Production System Down'),
	('medium','Medium - System Impaired'),
	('low','Low - General Guidance')
	]


	department=forms.ChoiceField(required=True,choices=DEPT)
	category=forms.ChoiceField(required=True,choices=CATEGORY)
	pwslab_project_url=forms.URLField(required=True)
	subject=forms.CharField(max_length=50)
	description=forms.CharField(max_length=250)


	contact_name=forms.CharField(max_length=50)
	email       =forms.EmailField()
	phone       =forms.IntegerField()

	priority=forms.ChoiceField(required=True,choices=PRIORITY)

	upload_file=forms.FileField()








