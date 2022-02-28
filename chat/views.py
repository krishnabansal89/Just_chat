from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from django.http import JsonResponse

email = ''
pwd = ''

# Create your views here.
@csrf_exempt
def hello(request):
    # return HttpResponse('hello mic testingsdfds')
    # data = {'name':name}
    # fw = open('test.txt','r')
    # data = fw.readlines()
    # fw.close
    # print(data)
    # data = json.dumps(data)
    return  render(request,'login.html') 

@csrf_exempt
def about(request):
    name = request.POST.get('name')
    fw = open('test.txt','a')
    fw.write(name+"\n")
    fw.close
    data = {'name':name}
    data1 = json.dumps(data)
    return  JsonResponse({"data": data1})

def new(email,passwd,name):
    import csv
    f = open('./text_file/list.csv','a')
    
    wr = csv.writer(f)
    fields = ['Name','Email','password']
    row = [name,email,passwd]
    wr.writerow(row)
    f.close()
def check1(email):
    import csv
    f = open('./text_file/list.csv','r')
    find = False
    r = csv.reader(f)
    for row in r:
        if len(row)>0:
            if row[1].lower()==email.lower():
                find = True 
    return find

@csrf_exempt
def sign(request): 
    if request.method =="POST":
        email = request.POST.get('email').lower()
        passwd = request.POST.get('password')
        name = request.POST.get('name')
        t = check1(email)
        file_making('t',str(t))
        if t == False:
            print(name,email,passwd)
            new(email,passwd,name)
        return HttpResponse(request)
    if request.method =='GET':
        t = file_reading('t')
        return JsonResponse({'data':t},safe=False)


def login(request):
    return render(request,'login.html')


def check(email,pwd):
    import csv
    f = open('./text_file/list.csv','r')
    find = False
    l=[] 

    r = csv.reader(f)
    for row in r:
        if len(row)>0:
            if row[1].lower()==email and row[2]==pwd:
                find = True   
                l = [find,row[0],row[1]] 
    print(l)
    return JsonResponse({'data':l},safe=False)
@csrf_exempt
def loginup(request):
    if request.method == 'POST':
        global email
        global pwd
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        return HttpResponse()
    if request.method =='GET':
        import csv
        f = open('./text_file/list.csv','r')
        find = False
        l=[] 

        r = csv.reader(f)
        for row in r:
            if len(row)>0:
                if row[1].lower()==email and row[2]==pwd:
                    find = True   
                    l = [find,row[0],row[1]] 

        return JsonResponse({'data':l},safe=False)



def file_making(name,content):
    s = './text_file/info/' + name + '.txt'
    f = open(s,'w')
    f.write(content)
    f.close()
def file_reading(name):
    s = './text_file/info/' + name + '.txt'
    data = ''
    try:
        f = open(s,'r')
        data = f.read()
        f.close()
    except:
        pass
    return data
def clear_file(name):
    s = './text_file/info/' + name + '.txt'
    f = open(s,'w')
    f.write('')
    f.close()