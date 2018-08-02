"""PollServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls import views_questions, views_answers, views_accounts, views_sessions, views_subjects

urlpatterns = [
	#path('admin/', admin.site.urls),
	path('questions/<str:ide>/', views_questions.getQuestion, name = 'getQuestion'),
	path('questions/<str:ide>/answers/', views_answers.getAnswer, name = 'getAnswer'),

	path('answers/submit/', views_answers.submitAnswer, name = 'submitAnswer'),

	path('questions/submit/',  views_questions.submitQuestion, name = 'submitQuestion'),
	path('questions/update/', views_questions.updateQuestion, name = 'updateQuestion'),
	path('questions/delete/', views_questions.deleteQuestion, name = 'deleteQuestion'),

	path('questions/<str:creatorID>/<int:status>/', views_questions.getCreatorQuestionByStatus, name = 'getCreatorQuestionByStatus'),
	path('questions/creator/<str:creatorID>/', views_questions.getQuestionsByCreatorId, name = 'getQuestionsByCreatorId'),
	path('questions/user/<str:userID>/', views_questions.getQuestionsByUserId, name = 'getQuestionsByUserId'),
	path('questions/allanswers/<str:questionID>/', views_answers.getAllAnswersByQuestionId, name = 'getAllAnswersByQuestionId'),
    
    path('subjects/<str:studentID>/', views_subjects.getAllSubjectsByStudentId, name = 'getAllSubjectsByStudentId'),
    
    path('sessions/<str:studentID>/', views_sessions.getAllSessionsByStudentId, name = 'getAllSessionsByStudentId'),
    
    path('login/', views_accounts.checkLogin, name = 'checkLogin'),
]
