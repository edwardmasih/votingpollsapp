from django.shortcuts import render
from .forms import AddQuestionForm, AddChoices
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def addQuestion(request):
    if request.method == 'POST':
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddQuestionForm()
    return render(request, 'pages/addQuestion.html', {'form': form})

def addChoice(request):
    if request.method == 'POST':
        form1 = AddChoices(request.POST)
        if form1.is_valid():
            form1.save()
    else:

        form1 = AddChoices()
    return render(request, 'pages/addChoice.html', {'form1': form1})