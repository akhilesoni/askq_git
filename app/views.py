from django.shortcuts import render, HttpResponse,redirect, HttpResponseRedirect
from app.models import Person, Topic, Question, Answer
from app.forms import LoginForm, SignupForm, AskQuestion, AddTopicForm, AnswerForm
import datetime
# Create your views here.
User = None
def index(request):
    notice = ''
    if('username' in request.COOKIES):
        username = request.COOKIES['username']
        global User 
        User = Person.objects.filter(username=username).first()
        return redirect(feed)
    return render(request,'index.html',{'notice':notice})

def login(request):
    if(request.method == 'POST'):
        loginform = LoginForm(request.POST)
        if(loginform.is_valid()):
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']
            global User
            User = Person.objects.filter(username=username).first()

            if(User is not None):
                if(password == User.password):
                    response = redirect(feed)
                    response.set_cookie('username',username)
                    return response
                else:
                    return render(request,'index.html',{'notice':'wrong password!!'})
            else:
                notice = "invalid creadetials"
                return render(request,'index.html',{'notice':notice})
        return render(request,'index.html',{'notice':'invalid'})        
    return render(request,'index.html',{'notice':''})


def signup(request):
    if(request.method == 'POST'):
        signupform = SignupForm(request.POST)
        if(signupform.is_valid()):
            name = signupform.cleaned_data['name']
            username = signupform.cleaned_data['username']
            password = signupform.cleaned_data['password']
            global User
            User = Person.objects.filter(username=username).first()
            if(User is not None):
                return render(request,'index.html',{'notice':'username exists!!'})
            Person(name=name,username=username,password=password).save()
            return redirect(feed)
        return render(request,'index.html',{'notice':"invalid"})    
    return render(request,'index.html',{'notice':''})

def feed(request):
    if(User is not None):
        topics = Topic.objects.all()
        questions = Question.objects.all()
        return render(request,'feed.html',{'user':User,'topics':topics,'questions':questions})
    return redirect(index)

def addTopic(request):
    if(request.method == 'POST'):
        form = AddTopicForm(request.POST)
        if(form.is_valid()):
            topic = form.cleaned_data['topic']
            temptopic = Topic.objects.filter(name=topic).first()
            if(temptopic is not None):
                return redirect(feed)
            Topic(name=topic).save()
            return redirect(feed)
        return redirect(feed)
    return redirect(feed)

def addQuestion(request):
    if(request.method == 'POST'):
        form = AskQuestion(request.POST)
        if(form.is_valid()):
            content = form.cleaned_data['question']
            topicid = form.cleaned_data['topic']
            topic = Topic.objects.filter(id=topicid).first()
            views = 0
            if(User is None):
                return redirect(index)
            person = User
            Question(content=content, view=views, topicid=topic, personid=person).save()
            return redirect(feed)
        return redirect(feed)
    return redirect(feed)


def topicFeed(request,id):
    topic_id = Topic.objects.filter(id=id).first()
    topics = Topic.objects.all()
    questions = Question.objects.filter(topicid=topic_id)
    if(User is None):
        return redirect(index)
    return render(request,'topicFeed.html',{'questions':questions,'topics':topics,'topic_id':topic_id,'user':User})

def question(request,id):
    question_id = Question.objects.filter(id=id).first()
    answers = Answer.objects.filter(question=question_id)
    topics = Topic.objects.all()
    return render(request,'question.html',{'question':question_id,'user':User,'answers':answers,'topics':topics})

def answer(request,id):
    if(request.method == 'POST'):
        form = AnswerForm(request.POST)
        if(form.is_valid()):
            content = form.cleaned_data['answer']
            vote = 0
            if(User is None):
                return redirect(index)
            person = User
            question = Question.objects.filter(id=id).first()
            Answer(content=content,vote=vote,question=question,person=person).save()
            return redirect('question',id=id)
        return redirect('question',id=id)
    return redirect('question',id=id)

