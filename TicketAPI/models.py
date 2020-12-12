from django.db import models

from .forms import TicketForm

# Create your models here.

class Ticket(models.Model):
	model=TicketForm