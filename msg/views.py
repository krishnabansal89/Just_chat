from django.shortcuts import render
from django.http import HttpResponse, response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):

    return render(request,'chat.html')  


@csrf_exempt
def data(request):

    if request.method =='POST':
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        time = request.POST.get('time')
        new_email = request.POST.get('new_email')
    
        file_making('email',email)
        file_making('new_email',new_email)
        if  email!='' and new_email!= '':
            print(email,msg,time,new_email)

            enter(email,msg,time,new_email)
        return HttpResponse()
    if request.method =='GET' :
        r = []
        email = file_reading('email')
        new_email = file_reading('new_email')
        # file_making('email','')
        # file_making('new_email','')
        if  email!='' and new_email!= '':
            import csv
            print('email',email,new_email)
            email,new_email = great(email,new_email)
            s = 'Just_chat/text_file/chats/' + email + '-' +new_email+'.csv'
            print('lett seeeee',s)
            f = open(str(s),'r')
            wr = csv.reader(f)
            
            for i in wr:
                if len(i)!=0:
                    r.append(i)
            print(r)
        return JsonResponse({'data':r},safe=False)
    return HttpResponse()

def enter(email,msg,time,new_email):
    import csv
    email1,new_email1 = great(email,new_email)
    s = 'Just_chat/text_file/chats/' + email1 + '-' + new_email1+'.csv'
    f = open(str(s),'a')

    w = csv.writer(f)
    r = [email,msg,time,new_email]
    w.writerow(r)
    f.close()

def test(request):
    return render(request,'contact.html')

@csrf_exempt
def contact(request):
    if request.method =='POST':
        email = request.POST.get('email').lower()
        file_making('email1',email)
        print(email)
        return HttpResponse()
    if request.method =="GET" :
        email = file_reading('email1')
        file_making('email1','')
        if email!='': 
            data = file_contact(email)
            email=''
            return JsonResponse({'data':data},safe=False)
    return HttpResponse()

def file_contact(name):
    import csv
    s = 'Just_chat/text_file/'+name + '-contact.csv'
    r = []
    try:
        f = open(s,'r')
        l = csv.reader(f)
        for i in l:
            if len(i)!=0:
                r.append(i)
        return r
    except:
        f = open(s,'a')
        print('koi na gg')
        return r

@csrf_exempt
def click(request):
    if request.method=='POST':
        name = request.POST.get('name').lower().strip()
        # name= ''
        

        idd = request.POST.get('id')[2]
        print('getname',idd,name)
        email1 = request.POST.get('email').lower()
        file_making('email2',email1)
        # print('getemail',new_email)
        import csv
        s = 'Just_chat/text_file/'+email1 + '-contact.csv'
        f = open(s,'r')
        r = csv.reader(f)
        i = 0
        for j in r:
            if len(j)!=0:
                print(i,idd)
                print(name,j[0].lower())
                if i==int(idd) and name==j[0].lower():
                    new_email1 = j[1]
                    print('newemial',new_email1)
                    file_making('new_email2',new_email1)
                    break
                i= i+1
                print(j)
        return HttpResponse(request)
    if request.method=='GET' :
        email1 = file_reading('email2')
        new_email1 = file_reading('new_email2')
        file_making('email2','')
        file_making('new_email2','')
        print('arey kuch to',email1,new_email1)
        if  email1!='' and new_email1!= '':
            data  = []
            import csv
            print('yaar',new_email1)
            new_path = 'Just_chat/text_file/'+ email1 +'-'+new_email1+'.csv'
            
            try:
                f = open(new_path,'r')
                wr = csv.reader(f)
                for i in wr:
                    if len(i)!=0:
                        data.append(i)
                print(data)
                print('ready?')
            except:
                f = open(new_path,'w')
            print('new_email',new_email1)
            new = new_email1
            new_email1 = ''
            return JsonResponse({'data':data,'new_email':new},safe=False)
    return HttpResponse()

def file_making(name,content):
    s = 'Just_chat/text_file/info/' + name + '.txt'
    f = open(s,'w')
    f.write(content)
    f.close()
def file_reading(name):
    s = 'Just_chat/text_file/info/' + name + '.txt'
    data = ''
    try:
        f = open(s,'r')
        data = f.read()
        f.close()
    except:
        pass
    return data

    

def great(a,b):
    if a<b:
        return b,a
    if a>b:
        return a,b
    else:
        return a,b
@csrf_exempt
def search(request):
    if request.method == 'POST':
        name = request.POST.get('name').lower()
        import csv
        f = open('Just_chat/text_file/list.csv','r')
        r = csv.reader(f)
        for i in r:
            if len(i)>0:
                if i[1].lower()==name.strip():
                    k = i[1].lower()
                    print(k)
                    file_making_new('local_name',k)
                    print(i[1])
        # print(name)
    if request.method == 'GET':
        s = 'Just_chat/text_file/info/' + 'local_name' + '.csv'
        import csv
        f = open(s,'r')
        r = csv.reader(f)
        data = []
        for i in r:
            if len(i)!=0:
                data = i
        clear_file('local_name')
        print(data)
        return JsonResponse({'data':data},safe=False)

    return HttpResponse(request)

def file_making_new(name,content):
    s = 'Just_chat/text_file/info/' + name + '.csv'
    import csv
    f = open(s,'a')
    r = csv.writer(f)
    r.writerow([content])
    f.close()
def clear_file(name):
    s = 'Just_chat/text_file/info/' + name + '.csv'
    import csv
    f = open(s,'w')
    r = csv.writer(f)
    r.writerow('')
    f.close()

@csrf_exempt
def make_contact(request):
    if request.method =='POST':
        new_email = request.POST.get('name').strip()
        email = request.POST.get('email').lower()
        real_name = request.POST.get('real_name').lower()
        if  new_email != 'undefined':
            print(new_email)
            k = 'Just_chat/text_file/list.csv'
            s= 'Just_chat/text_file/' + email + '-' + 'contact.csv'
            d = 'Just_chat/text_file/' + new_email + '-' + 'contact.csv'
            import csv
            f = open(k,'r')
            name = ''
            r = csv.reader(f)
            for row in r:
                if len(row)!=0:
                    if row[1].lower()==new_email.lower():
                        name = row[0]
                        # print(name)
            data = [name,new_email]
            data1 = [real_name,email]
            t = False
            file =open(s,'r')
            r1 = csv.reader(file)
            for row1 in r1:
                if len(row1)!=0:
                    if row1[1].lower()==new_email.lower():
                        t = True
            if t==False:
                fr = open(d,'a')
                a = csv.writer(fr)
                a.writerow(data1)
                fr.close()
                fw = open(s,'a')
                c = csv.writer(fw)
                c.writerow(data)
                fw.close()
            # print(name)
    return HttpResponse(request)