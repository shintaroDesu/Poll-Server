from django.http import JsonResponse, HttpResponse
from .setup import global_account_class, global_answer_class, global_question_class
from .setup import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
import json
import hashlib
from pymongo import cursor

# Create your views here.
def output(error_message = "False"):
	return JsonResponse({'update' : error_message})

def checkLogin(request):
	try:
		login_json = json.loads(request.body)
		hash = hashlib.md5(login_json["password"].encode())
		hash = hash.hexdigest()
		login_json["password"] = hash
		account_login = global_account_class.userLogin(login_json)
		return JsonResponse(account_login)
	except Exception as e:
		print(e)
		return output('False')

def newAccount(request):
	try:
		form_json = json.loads(request.body.decode("utf-8")) # form_json = {"username" : "asdf", "password" : "af"}
		hash = hashlib.md5(form_json["password"].encode())
		hash = hash.hexdigest()
		form_json["password"] = hash
		global_account_class.create(form_json)
		return output("True")
	except Exception as e:
		print(e)
		return output('False')

def getUserByTypeId(request, typeID):
	try:
		data_json = global_account_class.data.find_one({"userID" : typeID})
		data_json["_id"] = ""
		return JsonResponse(data_json)
	except Exception as e:
		print(e)
		return output('False')
def updateUser(request):
	try:
		new_data = json.loads(request.body.decode("utf-8"))
		global_account_class.update(new_data['id'], new_data)
		return output('True')
	except Exception as e:
		print(e)
		return output('False')

def deleteUser(request):
	try:
		data = json.loads(request.body.decode("utf-8"))
		global_account_class.delete(data['id'])
		return output('True')
	except Exception as e:
		print(e)
		return output('False')
