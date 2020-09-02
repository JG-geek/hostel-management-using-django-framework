from django.shortcuts import render,redirect
from .models import student_details,hostel_rooms
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.template.context_processors import csrf
from django.contrib import messages
from django.core.mail import send_mail
from jayanmol.settings import EMAIL_HOST_USER
# Create your views here.
def get(request, **kwargs):
    return render(request, 'index1.html', context=None)

        
def login(request):
    
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            request.session['userid']=user.id
            student=student_details.objects.get(user_name=user.id)
            return redirect('/home/login/homeview')
        else:
            messages.info(request,'username or password is incorrect!')
            return render(request,'login1.html')
    else:
        return render(request ,'login1.html')
    

def register(request):

    if (request.method == 'POST'):
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password=request.POST['password']
        email=request.POST['email']
        if username == '' or password == '':
             messages.info(request, 'Username or password must not be empty!')
             return redirect('/home/register')
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Taken')
                return redirect('/home/register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('/home/register/personaldetails')
    else:
        return render(request, 'register.html')    
                 
def logout(request):
    auth.logout(request)
    return redirect('/home')

def personaldetails(request):
    if request.method == 'POST':
        user1=request.POST['user_name']
        user=User.objects.get(username=user1)
        stu=student_details()
        stu.user_name=user
        stu.full_name=request.POST['full_name']
        stu.father_name=request.POST['father_name']
        stu.mother_name=request.POST['mother_name']
        stu.father_occupation=request.POST['father_occupation']
        stu.mother_occupation=request.POST['mother_occupation']
        stu.date_of_birth=request.POST['date_of_birth']
        stu.gender=request.POST['gender']
        stu.age=request.POST['age']
        stu.contact_number=request.POST['contact_number']
        stu.city=request.POST['city']
        stu.state=request.POST['state']
        stu.pincode=request.POST['pincode']
        stu.save()
        
        return redirect('/home/register/vacantroom')
    else:    
        return render(request, 'personaldetails1.html')
    
def vacantroom(request):
    if request.method == 'POST':
        roomtype=request.POST['type']
        rooms = hostel_rooms.objects.all()
        vacant_rooms1=[]
        vacant_rooms2=[]
        for room in rooms:
            if room.room_type==roomtype:
                if room.person1=="vacant" or room.person2=="vacant" or room.person3=="vacant":
                    if room.building_no=="1":
                        vacant_rooms1.append(room)
                    else:
                        vacant_rooms2.append(room)
        vacant_rooms=zip(vacant_rooms1, vacant_rooms2)      
        return render(request, 'vacantroom1.html', {'vacant_rooms': vacant_rooms})
    else:
        return render(request, 'vacantroom1.html')
    
def bookroom(request):
    if request.method == 'POST':
        roomno=request.POST['room_no']
        name=request.POST['full_name']
        room=hostel_rooms.objects.get(room_no=roomno)
        if room.person1=="vacant":
            room.person1=name
            room.save(update_fields=['person1'])
        elif room.person2=="vacant":
            room.person2=name
            room.save(update_fields=['person2'])
        elif room.person3=="vacant":
            room.person3=name
            room.save(update_fields=['person3'])
        
        return redirect('/home/login')
        
    else:
        return render(request, 'bookroom.html')

def homeview(request):
    userid=request.session['userid']
    student=student_details.objects.get(user_name=userid)
    return render(request, 'homeview.html', {'student' : student})


def myroom(request):
    userid=request.session['userid']
    student=student_details.objects.get(user_name=userid)
    rooms = hostel_rooms.objects.all()
    fname=student.full_name
    roompartners=[]
    for room in rooms:
        if room.person1 == fname:
            roompartners.append(room.person2)
            roompartners.append(room.person3)
            room_details=room
        elif room.person2 == fname:
            roompartners.append(room.person1)
            roompartners.append(room.person3)
            room_details=room
        elif room.person3 == fname:
            roompartners.append(room.person1)
            roompartners.append(room.person3)
            room_details=room
    
    return render(request, 'myroom.html', {'roompartners' : roompartners, 'room' : room_details, 'student' : student})

def mail(request):
    if request.method == 'POST':
        Message = request.POST['message']
        email = request.POST['email']
        send_mail('Regarding the website', 'hiiiiiieeeee','jaygoru03@gmail.com',['jaygoru03@gmail.com'],fail_silently=False,)
        return HttpResponse("mail sent successfully")