from django.shortcuts import render
from .models import customer
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def insert_customer(request):
	my_customer = customer()
	my_customer.customer_id = 3
	my_customer.first_name = "Ali"
	my_customer.last_name = "Khan"
	my_customer.date_of_birth = datetime.now()
	my_customer.is_gold_customer = True
	my_customer.save()
	text = """<h1>Customer Inserted !</h1>"""
	return HttpResponse(text)


def get_customer(request):
	# all_customers = Customer.objects.all()
	my_customer = customer.objects.get(pk=3)
	# gender_value_from_db = my_customer.gender
	# gender_display_value = my_customer.get_gender_display()
	text = """<h1>Customer Fetched !</h1> """

	return HttpResponse(my_customer.first_name)

def update_customer(request):
    my_customer = customer.objects.get(pk=3)
    my_customer.first_name='someNewName'
    my_customer.save()
    text = """<h1>Customer Updated !</h1>"""
    return HttpResponse(text)


def delete_customer(request):
    my_customer = customer.objects.get(pk=3)
    my_customer.delete()
    text = """<h1>Customer Deleted !</h1>"""
    return HttpResponse(text)


def get_customer_advanced(request):
	my_customer = customer.objects.filter(is_gold_customer= False)

	#this will return all results
	#my_customer = customer.objects.all()

	# filer or ALL will return a list which is then concatenated
	text = ""
	for c in my_customer:
		text += c.first_name + ", "

	return HttpResponse(text)
