from django.conf.urls import url
from .views import submit_ticket,home,login,ticket_manage
from django.contrib.auth import views as auth_views


urlpatterns=[
	url(r'^$',login,name='login'),
	url(r'^submit_ticket/',submit_ticket,name='submit_ticket'),
	url(r'^ticket_manage/',ticket_manage,name='ticket_manage')
	

	


]