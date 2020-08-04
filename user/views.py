from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib import messages
import ipdb
from .models import Profile, ResetCodes as reset_codes
from django.conf import settings
import random
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django_email_verification import sendConfirm
from django.contrib.auth.hashers import check_password


from django.contrib.auth import views as auth_views
app_name = 'ad'
User = get_user_model()

def login(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
      remember_me = request.POST.get('remember me')

      if email == '':
        messages.error(request, "Can't leave email empty", extra_tags="email")
        return HttpResponseRedirect(request.path)
      else:
        try:
          validate_email(email)
        except ValidationError:
          messages.error(request, "Please enter a valid email", extra_tags="email")
          return HttpResponseRedirect(request.path)

      if password == '':
        messages.error(request, "Can't leave password empty", extra_tags="password")
        return HttpResponseRedirect(request.path)
      else:
        if len(password) < 8:
          messages.error(request, "Password must be at least 8 characters", extra_tags="password")
          return HttpResponseRedirect(request.path)
      
      if(remember_me == "on"):
        request.session.set_expiry(43200) #12 hours long session
      

      if User.objects.filter(email=email).exists():
        user = auth.authenticate(email=email, password=password)
        if user is not None:
          auth.login(request, user)
          request.session['user_id'] = user.id
          return render(request,'ad/main.html')
        else:
          messages.error(request, "This password is incorrect", extra_tags="password")
          messages.info(request, email , extra_tags="email")
          return HttpResponseRedirect(request.path)
      else:
        messages.error(request, "This email doesn't exist", extra_tags="email")
        return HttpResponseRedirect(request.path)
    else:
      return render(request, 'user/login.html')
  

    
    

def register(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method == 'POST':
      first_name = request.POST.get('fname')
      last_name = request.POST.get('lname')
      email = request.POST.get('email')
      password = request.POST.get('password')
      confirm_password =  request.POST.get('confirm_password')

      if email == '':
        messages.error(request, "Can't leave email empty", extra_tags="email")
        return HttpResponseRedirect(request.path)
      else:
        try:
          validate_email(email)
        except ValidationError:
          messages.error(request, "Please enter a valid email", extra_tags="email")
          return HttpResponseRedirect(request.path)
      if User.objects.filter(email=email).exists():
        messages.error(request, "This email is already registered", extra_tags="email")
        return HttpResponseRedirect(request.path)

      if not first_name.isalpha():
        messages.error(request, "Invalid first name.", extra_tags="fname")
        messages.info(request, email, extra_tags="email")
        return HttpResponseRedirect(request.path)
      
      if not last_name.isalpha():
        messages.error(request, "Invalid last name.", extra_tags="lname")
        messages.info(request, email, extra_tags="email")
        messages.info(request, first_name, extra_tags="fname")
        return HttpResponseRedirect(request.path)

      if password == "":
        messages.error(request, "Can't give empty password", extra_tags="password")
        messages.info(request, email, extra_tags="email")
        messages.info(request, first_name, extra_tags="fname")
        messages.info(request, last_name, extra_tags="lname")
        return HttpResponseRedirect(request.path)
      elif not password == confirm_password:
        messages.error(request, "Password doesn't match.", extra_tags="password match")
        messages.info(request, email, extra_tags="email")
        messages.info(request, first_name, extra_tags="fname")
        messages.info(request, last_name, extra_tags="lname")
        return HttpResponseRedirect(request.path)
      elif len(password) < 8:
          messages.error(request, "Password must be at least 8 characters", extra_tags="password")
          return HttpResponseRedirect(request.path)
      
      user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
      user = auth.authenticate(email=email, password=password)
      if user is not None:
        auth.login(request, user)
        request.session['user_id'] = user.id
        sendConfirm(user)
        return redirect('home')
      else:
        return redirect('profile')
    else:
      return render(request, 'user/register.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required
def send_verification_email_(request):
  if request.method == 'GET':
    user = User.objects.get(id=request.user.id)
    print("THIS IS GET")
    send_verification_email(user)
    return render(request, 'user/email_sent.html')
  else:
    print("THIS IS POST")
    return render(request, 'user/email_sent.html')

def send_verification_email(user):
    sendConfirm(user)
    return 

def home(request):

      return render(request, 'ad/main.html')


@login_required
def verify_password(request):
    print("THIS IS METHOD 1")
    if request.method == 'POST':
      password = request.POST.get('password')
      if password == "":
        messages.error(request, "Can't give empty password", extra_tags="password")
        return HttpResponseRedirect(request.path)
      elif len(password) < 8:
        messages.error(request, "Password must be of minimum 8 characters", extra_tags="password")
        return HttpResponseRedirect(request.path)
      
      user = User.objects.get(pk=request.user.id)
      check = check_password(password, user.password)
      if check:
        request.session['reset_password'] = 'True'
        print("GOT HERE 1"+request.session['reset_password'])
        return redirect('update')
      else:
        messages.error(request, "Password didn't match", extra_tags="password")
        return HttpResponseRedirect(request.path)
      
    else:
      return render(request, 'user/verify_password.html')  
import ipdb
@login_required
def update_password(request):
  if 'reset_password' in request.session:
    if request.method == 'POST':
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm_password')
      if password == "":
        messages.error(request, "Can't give empty password", extra_tags="password")
        return HttpResponseRedirect(request.path)
      if len(password) < 8:
        messages.error(request, "Password must be of minimum 8 characters", extra_tags="password")
        return HttpResponseRedirect(request.path)
      if not password == confirm_password:
        messages.error(request, "Password didn't match", extra_tags="password confirm")
        return HttpResponseRedirect(request.path)

      user = User.objects.get(pk=request.user.id)
      user.set_password(password)
      user.save()
      update_session_auth_hash(request, user)
      del request.session['reset_passwgord']
      return redirect('home')
    else:
      return render(request, 'user/update_password.html')  
  else:
    return redirect('broken_link')
# def reset_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         if email == '':
#           messages.error(request, "Can't leave email empty", extra_tags="email")
#           return HttpResponseRedirect(request.path)
#         else:
#           try:
#             validate_email(email)
#           except ValidationError:
#             messages.error(request, "Please enter a valid email", extra_tags="email")
#             return HttpResponseRedirect(request.path)
        
#         if User.objects.filter(email=email, is_active=True).exists():
#             request.session['reset_email'] = email
#             # del request.session['reset_email']
#             email_code(request, email)
#             print("EXISTS ")
#             # if val: 
#             #   return redirect('matchcode')
#             # else:
#             return redirect('broken_link')
#         else:
#             messages.error(request,"This email is not registered.",extra_tags="email")
#             return HttpResponseRedirect(request.path)
#     else:
#         return render(request, 'user/enteremail.html')

# def email_code(request, email):
#     code = ""
#     for x in range(4):
#       code = code + str(random.randint(0, 9))
    
#     user = User.objects.get(email=email)
#     reset_code = reset_codes.objects.filter(user=User.objects.get(email=email))

#     if not reset_code:
#       reset_code = reset_codes.objects.create(user=user, code=code)
#       reset_code.save()
#     else:
#       reset_code = reset_codes.objects.filter(user=user).update(code=code)

#     subject = 'Recovery code'
#     message = 'Use '+code+' to recover your password.\n\nThank you.'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email, ]
#     val = send_mail(subject, message, email_from, recipient_list)
#     return val



# def code_match(request):
#   if 'reset_email' in request.session:
#       if request.method == 'POST':
#         input_code = request.POST.get('code')
#         if input_code == "":
#           messages.error(request, "Enetr the recovery code. ", extra_tags="code")
#           return render(request, 'user/emailcode.html')
        
#         record_code = reset_codes.objects.get(user=User.objects.get(email=request.session.get('email')))
#         del request.session['reset_email']
#         record_code = record_code.code
#         if input_code == record_code:
#           return redirect('newpassword')
#         else:
#           messages.error(request, "Invalid recovery code", extra_tags="code")
#           return HttpResponseRedirect(request.path)
#       else:
#         return render(request, 'user/emailcode.html')
#   else:
#     return redirect('broken_link')


# def new_password(request):
#   if request.method == 'POST':
#     password = request.POST.get('password')
#     if password ==  "":
#       messages.error(request, "Can't send empty password.",extra_tags="password")
#       return HttpResponseRedirect(request.path)
#     elif len(password) < 8:
#       messages.error(request, "Password too short.",extra_tags="password")
#       return HttpResponseRedirect(request.path)
#     user = User.objects.get(email=request.session.get('email'))
#     user.set_password(password)
#     user.save()
#     messages.success(request, "Your password has been changed successfully.", extra_tags="password")
#     return success(request)
#   else:
#     return render(request, 'user/enternewpassword.html')

def success(request):
    return render(request, 'user/success.html')

def _context(user, profile):
    if profile.profile_picture:
      url = profile.profile_picture.url
    else:
      url = None
    yy = ''
    mm = ''
    dd = ''
    if profile.date_of_birth:
      try:
        yy = str(profile.date_of_birth).split('-')[0]
        mm = str(profile.date_of_birth).split('-')[1]
        dd = str(profile.date_of_birth).split('-')[2]
      except:
        print("error in dob "+str(profile.date_of_birth))
    context = {
        'Name': user.first_name+" "+user.last_name,
        'Email': user,
        'Is_verified': user.is_verified,
        'Country': profile.country,
        'City': profile.city,
        'Contact': profile.phone_number, 
        'URL': url,
        'DOB': ("%s-%s-%s" % (dd, mm, yy)),      
      }
    return context

def profile(request):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
      
      full_name = request.POST.get('full_name')
      country = request.POST.get('country')
      avatar = request.FILES.get('avatar')
      city = request.POST.get('city')
      phone_number = request.POST.get('phone_number')
      date_of_birth = request.POST.get('date_of_birth')
      
      if avatar:
        if not (avatar.name.endswith(".jpg") or 
                      avatar.name.endswith(".jpeg") or 
                            avatar.name.endswith(".png")):
          messages.error(request, "Wrong format has been uploaded", extra_tags="image")
          return HttpResponseRedirect(request.path)
        else:
          if avatar.size > 10000000:
            messages.error(request, "Image size must be smaller than 10 MBs.", extra_tags="image")
            return HttpResponseRedirect(request.path)
          else:
            profile.profile_picture = avatar
            profile.save()
      if full_name != user.first_name+" "+user.last_name:
        if  all(x.isalpha() or x.isspace() for x in full_name):
          if not (len(full_name) > 32 or len(full_name) < 8):
            fname = full_name.split(' ', 1)[0]
            try:
              lname = full_name.split(' ', 1)[1]
            except IndexError:
              lname = ""
            user.first_name = fname
            user.last_name = lname
            user.save()
          else:
            messages.error(request, "Name must be between 8 to 32 characters", extra_tags="name")
            return HttpResponseRedirect(request.path)
        else:
          messages.error(request, "Name must only consis of alphabets", extra_tags="name")
          return HttpResponseRedirect(request.path)
      profile = Profile.objects.get(user=user)
      
      if city != profile.city:
        if (city == 'Lahore' or city == 'Karachi' or city == 'Islamabad'):
          profile.city = city
          profile.save() 
        else:
          messages.error(request, "Invalid city.", extra_tags="city")
          return HttpResponseRedirect(request.path)
      try:      
        dd = date_of_birth.split('-')[0]
        mm = date_of_birth.split('-')[1]
        yy = date_of_birth.split('-')[2]
        date_of_birth = ('%s-%s-%s'%(yy, mm, dd ))
      except:
        messages.error(request, "Invalid date", extra_tags="date")
        return HttpResponseRedirect(request.path)


      if date_of_birth != str(profile.date_of_birth):
        profile.date_of_birth = date_of_birth
        profile.save()

      if phone_number == '':
        phone_number = None
      if phone_number != profile.phone_number:
        if not phone_number.isnumeric():
          messages.error(request, "Invalid phone number", extra_tags="contact")
          return HttpResponseRedirect(request.path)
        else:
          if len(phone_number) != 10:
            messages.error(request, "Phone number must be of 10 characters", extra_tags="contact")
            return HttpResponseRedirect(request.path)
          profile.phone_number = phone_number
          profile.save()
      
      messages.info(request, "Your profile has been successfully updated!", extra_tags="update")
      return redirect('profile')

    else:
      return render(request, 'user/profile.html', _context(user, profile))

def broken_link(request):
    return render(request, 'broken.html')

