from django.shortcuts import render, redirect
from .models import Laureate

def home(request):
    return render(request, 'laureates/home.html')

def question(request, question_num):
    if request.method == 'POST':
        # Сохраняем ответ в сессии
        answer = request.POST.get('answer')
        request.session[f'q{question_num}'] = answer
        
        if question_num < 4:
            return redirect('question', question_num=question_num+1)
        else:
            return redirect('result')
    
    questions = {
        1: "В какой области получил(а) Нобелевскую премию этот лауреат?",
        2: "В каком десятилетии была присуждена премия?",
        3: "Из какой страны этот лауреат?",
        4: "Какой пол у этого лауреата?"
    }
    
    if question_num == 1:
        options = ["Физика", "Химия", "Медицина", "Литература", "Мир", "Экономика"]
    elif question_num == 2:
        options = ["1900-1910", "1911-1920", "1921-1930", "1931-1940", 
                  "1941-1950", "1951-1960", "1961-1970", "1971-1980", 
                  "1981-1990", "1991-2000", "2001-2010", "2011-2020"]
    elif question_num == 3:
        options = ["США", "Великобритания", "Франция", "Германия", 
                  "Россия/СССР", "Япония", "Канада", "Швеция",
                  "Польша", "Индия", "Китай", "Другие"]
    elif question_num == 4:
        options = ["Мужской", "Женский"]
    
    context = {
        'question_num': question_num,
        'question': questions[question_num],
        'options': options
    }
    return render(request, 'laureates/question.html', context)

def result(request):
    # Получаем ответы из сессии
    answers = {
        'q1_answer': request.session.get('q1'),
        'q2_answer': request.session.get('q2'),
        'q3_answer': request.session.get('q3'),
        'q4_answer': request.session.get('q4'),
    }
    
    # Ищем подходящего лауреата
    laureates = Laureate.objects.filter(
        q1_answer=answers['q1_answer'],
        q2_answer=answers['q2_answer'],
        q3_answer=answers['q3_answer'],
        q4_answer=answers['q4_answer']
    )
    
    if laureates.exists():
        laureate = laureates.first()
    else:
        laureate = None
    
    context = {
        'laureate': laureate,
        'answers': answers
    }
    return render(request, 'laureates/result.html', context)