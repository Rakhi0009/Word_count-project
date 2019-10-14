from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def hit_enter(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] = 1
    return render(request,'hitenter.html',{'fulltext':full_text , 'count' : len(word_list),'word_dict':word_dict})