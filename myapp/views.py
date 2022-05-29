from django.shortcuts import render
from django.contrib.auth import authenticate, login as dj_login, logout
from django.shortcuts import redirect
from django.http.response import StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser,Exam,Mcq,Answer, RegisteredExam, Subjective,GivenExam,StudentLog
from proctoring.proctoring import get_analysis, yolov3_model_v3_path

import random
# from tester.admin import Questions
# from tester.camera import VideoCamera, IPWebCam, MaskDetect, LiveWebCam
# from tester.camera import VideoCamera

# Create your views here.
def creatingOTP():
    otp = ""
    for i in range(5):
        otp+= f'{random.randint(0,9)}'
    return otp

def sendEmail(email):
    
    otp = creatingOTP()
    try:

        send_mail(
        'One Time Password',
        f'Your OTP pin is {otp}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        )
        return otp
    except:
        return False 
def index(request):
    return render(request,'index.html')

def instruction(request):
    return render(request,'instruction1.html')
# def instruction2(request):
#     return render(request,'instruction2.html')
def login(request):
    return render(request,'login.html')
    
def mentorship(request):
    return render(request,'mentorship.html')

def brainoregister(request):
    return render(request,'brainregister.html')

def dashboard(request):
    return render(request,'dashboard.html')

def login1(request):
    if request.method=='POST':
        email=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(email=email,password=password)
        if user is not None:
            if(user.is_staff==True):

                dj_login(request,user)
                return redirect('/mentor')
                
            dj_login(request,user)
            return redirect('/student')
        return redirect('/login')
        
        
    return render(request,'login1.html')


def home(request):
    return render(request,'home.html')
def liveproc(request):
    return render(request,'liveproc.html')
@csrf_exempt
def register(req):
    if req.method=='POST':
        email=req.POST.get('email')
        otp=req.POST.get('otp')
        u=CustomUser.objects.get(email=email)
        if(u.otp==otp):
            u.isVerified=True
            u.save()
            return JsonResponse({'status':'true'})
        return JsonResponse({'status':'false'})

    
    return render(req,'register.html')

@csrf_exempt
def sendEmailAndRegister(req):
    if req.method=='POST':
        data=req.POST.items()
        data=dict(data)
        # print(data)
        data.pop('comfirm_password')
        data.pop('checkbox')
        # print(data['email'])
        email=data['email']
        password=data['password']
        data.pop('email')
        data.pop('password')

        otp=sendEmail(email)
        try:
            u=CustomUser.objects.get(email=email)
            if( u.email==email and u.isVerified==True):
                return JsonResponse({'status':'eamil already exist'})
            elif( u.email==email and u.isVerified==False):
                u.otp=otp
                u.save
        except:
                
                data['otp']=otp
                u=CustomUser(email=email,**data)
                u.set_password(password)
                u.save()
        return JsonResponse({'status':'True'})

        


# def addquestion(request):
#     if request.method=='POST':
#         question=request.POST['question']
#         option1=request.POST['option1']
#         option2=request.POST['option2']
#         option3=request.POST['option3']
#         option4=request.POST['option4']
#         q=Questions(question=question,option1=option1,option2=option2,option3=option3,option4=option4)
#         q.save()
   
#     data=Questions.objects.all()
#     return render(request,'createQues.html',{'data':data})

def givetest(request,id):
    if request.method == 'POST':
        answers=request.POST.items()
        answers=dict(answers)
        answers.pop('csrfmiddlewaretoken')
        exam=Exam.objects.get(exam_id=id)
        email=request.user.email
        student=CustomUser.objects.get(email=email)
        GivenExam(student=student,exam=exam).save()
        for qno, ans in answers.items():
            q=Mcq.objects.get(qno=qno)
            Answer(Exam=exam,student=student,qno=q,ans=ans).save()

        return redirect('/student')
    exam=Exam.objects.get(exam_id=id)
    data=Mcq.objects.filter(Exam=id).order_by('Exam')
    return render(request,'givetest.html',{'data':data,'exam':exam})

def giveSubtest(req,id):
    if req.method == 'POST':
        exam=Exam.objects.get(exam_id=id)
        email=req.user.email
        student=CustomUser.objects.get(email=email)
        GivenExam(student=student,exam=exam).save()
        files= req.FILES.items()
        for f in files:
            print(f[1])
            handle_uploaded_file(f[1]) 
        return redirect('/student')

    data=Subjective.objects.filter(exam=id)
    exam=Exam.objects.get(exam_id=id)
    print(data)
    return render(req,'givesubtest.html',{'data':data,'exam':exam,'email':req.user.email})

@login_required(login_url='/login1')
def studentDashboard(req):
    exams=Exam.objects.all()
    student=req.user 
    rexams=RegisteredExam.objects.filter(student=student)
    gexams=GivenExam.objects.filter(student=student)
    rexam_ids=[]
    gexam_ids=[]
    for rexam in rexams:
        rexam_ids.append(rexam.exam.exam_id)
    for gexam in gexams:
        gexam_ids.append(gexam.exam.exam_id) 

    return render(req, 'studentdashboard.html',{'exams':exams,'rexams':rexams,'rexam_ids':rexam_ids,'gexam_ids':gexam_ids})

def logout_view(req):
    logout(req)
    return redirect('/login1')
def handle_uploaded_file(f): 
    print(f.name) 
    with open('myapp/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 

def payment(req,id):
    if req.method=='POST':
        exam=Exam.objects.get(exam_id=id)
        user= req.user 
        RegisteredExam(student=user,exam=exam).save()
        return redirect('/student')
    return render(req,'payment.html')
def instruction(req,id):
    exam=Exam.objects.get(exam_id=id)
    if(exam.exam_type=='mcq'):
        return render(req, 'instruction.html',{'id':id})

    return render(req, 'instruction1.html',{'id':id})
import base64
@csrf_exempt
def videoFeed(req):
    if req.method == 'POST':
        data = req.POST.items()
        data=dict(data)
        # print(data['img'])
        coded_string = data['img']
        email = data['email']
        examId=data['examId']
        with open("myapp/static/screenshot/imageToSave.png", "wb") as fh:
            fh.write(base64.b64decode(coded_string))
        yolov3_model_v3_path("myapp/yolov3.weights")
        proctorData = get_analysis(coded_string, "myapp/shape_predictor_68_face_landmarks.dat")
        if(proctorData['mob_status']!='Not Mobile Phone detected' or proctorData['person_status']!='Normal'):
            print(proctorData['mob_status'],email, examId)
            StudentLog(studentEmail=email,examId=examId,img=coded_string).save()
        return JsonResponse({'status':True})
    
def studentLogs(req):
    exams = Exam.objects.all()
    print(exams)
    return render(req,'studentLogs.html', {'exams':exams})

def examlog(req,id):
    emails = StudentLog.objects.filter(examId=id).values_list('studentEmail',flat=True).distinct()
    print(emails)
    return render(req,'examlog.html',{'emails': emails})

def logdetails(req,email):
    logs = StudentLog.objects.filter(studentEmail=email)
    return render(req, 'logdetails.html',{'logs':logs})
