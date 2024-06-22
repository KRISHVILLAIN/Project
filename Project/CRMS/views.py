import re

from authentication.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate

from .form import signup

from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect

from .models import Register_model, driver_model, order_model
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        data = Register_model.objects.all()
        return render(request, 'index.html', {'data': data})
    # else:
    #     return redirect('/login_view')


def service(request):
    if request.user.is_authenticated:
        return render(request, "service.html")
    # else:
    #     return redirect('/login_view')


def about(request):
    if request.user.is_authenticated:
        return render(request, "about.html")
    # else:
    #     return redirect('/login_view')


def booking(request):
    if request.user.is_authenticated:
        id = request.GET['id']
        data = Register_model.objects.filter(id=id)
        data1 = driver_model.objects.all()
        return render(request, "booking.html", {'data': data, 'driver': data1})
    # else:
    #     return redirect('/login_view')


def car(request):
    if request.user.is_authenticated:
        return render(request, "car.html")
    else:
        return redirect('/login_view')


def contact(request):
    if request.user.is_authenticated:
        return render(request, "contact.html")
    # else:
    #     return redirect('/login_view')


def driver(request):
    if request.user.is_authenticated:
        return render(request, "driver_regi.html")
    # else:
    #     return redirect('/login_view')


def driver_regi_1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            first = request.POST['first']
            last = request.POST['last']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            aadhar = request.POST['aadhar']
            dob = request.POST['dob']
            name_pattern = r'^[a-zA-Z]+$'
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            phone_pattern = r'^[6-9]\d{9}$'
            aadhar_pattern1 = r'\d{12}$'
            if not re.match(name_pattern, first) and re.match(name_pattern, last) and re.match(name_pattern, address):
                messages.warning(request, "Enter Name and address only Character")
                return redirect('/driver')
            elif not re.match(email_pattern, email):
                messages.warning(request, "Invalid Email Format")
                return redirect('/driver')
            elif not re.match(phone_pattern, phone):
                messages.warning(request, "Enter only 10 Digit Mobile Number")
                return redirect('/driver')
            elif not re.match(aadhar_pattern1, aadhar):
                messages.warning(request, "Enter only 12 Digit Aadhar Number")
                return redirect('/driver')
            else:
                messages.success(request, "Registration successful..!")
                data = driver_model(first=first, last=last, email=email, phone=phone, address=address, aadhar=aadhar,
                                    dob=dob)
            data.save()
            return redirect('/driver')
        else:
            return HttpResponse("Fail..!")
    # else:
    #     return redirect('/login_view')


def team(request):
    if request.user.is_authenticated:
        f_name = request.user.first_name
        l_name = request.user.last_name
        data1=order_model.objects.filter(first=f_name,last=l_name)
        return render(request, "team.html",{'data':data1})
    # else:
    #     return redirect('/login_view')


def testimonial(request):
    if request.user.is_authenticated:
        return render(request, "testimonial.html")
    # else:
    #     return redirect('/login_view')


def register_car_page(request):
    if request.user.is_authenticated:
        return render(request, "register_car_page.html")
    # else:
    #     return redirect('/login_view')


# def demo(request):
#     return render(request, 'admin.html')


def admin_1(request):
    return render(request, 'admin.html')
    # return redirect('/login_view_1')


# def login_view_1(request):
#     if not request.user.is_authenticated:
#         if request.method == "POST":
#             fm = AuthenticationForm(request=request, data=request.POST)
#             if fm.is_valid():
#                 uname = fm.cleaned_data['username']
#                 upass = fm.cleaned_data['password']
#                 user = authenticate(username=uname, password=upass)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, "Login Successful..!")
#                     return redirect('/demo')
#             else:
#                 fm = AuthenticationForm()
#             return render(request, 'login.html', {'form': fm})
#     else:
#         return redirect('/login_view')


def admin_2(request):
    if request.user.is_authenticated:
        data = Register_model.objects.all()
        return render(request, "manage_car.html", {'car': data})
    # else:
    #     return redirect('/login_view')


def show_ord(request):
    if request.user.is_authenticated:
        data = order_model.objects.all()
        return render(request, "show_orders.html", {'car': data})
    # else:
    #     return redirect('/login_view')


def show_driver(request):
    if request.user.is_authenticated:
        data = driver_model.objects.all()
        return render(request, "show_drivers.html", {'car': data})
    # else:
    #     return redirect('/login_view')


def Register_car(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            c_name = request.POST['c_name']
            c_model = request.POST['c_model']
            c_am = request.POST['c_am']
            c_price = request.POST['c_price']
            file = request.FILES['c_file']
            name_pattern = r'^[a-zA-Z]+$'
            number_pattern = r'^[A-Z]{2}-\d{2}/[A-Z]{2}-\d{4}$'
            price_pattern = r'^\d+$'
            if not re.match(name_pattern, c_name):
                messages.warning(request, "Car Name Only Character")
                return redirect('/register_car_page')
            elif not re.match(number_pattern, c_model):
                messages.warning(request, "Not Valid Number, eg.MH-16/CS-2023 ")
                return redirect('/register_car_page')
            elif not re.match(price_pattern, c_price):
                messages.warning(request, "Only Enter Numbers")
                return redirect('/register_car_page')
            else:
                messages.success(request, "Car Registered Successful..!")
                data = Register_model(c_name=c_name, c_model=c_model, c_am=c_am, c_price=c_price, file=file)
                data.save()
            return redirect('/admin_2')
        else:
            return redirect('/register_car_page')
    # else:
    #     return redirect('/login_view')


def Edit_car_details(request):
    if request.user.is_authenticated:
        id = request.GET['id']
        data = Register_model.objects.all().filter(id=id)
        return render(request, 'Edit_car.html', {'car': data})
    # else:
    #     return redirect('/login_view')


def Edit_order_details(request):
    if request.user.is_authenticated:
        id = request.GET['id']
        data = order_model.objects.all().filter(id=id)
        data1 = driver_model.objects.all()
        return render(request, 'edit_order.html', {'car': data, 'driver': data1})
    # else:
    #     return redirect('/login_view')


def update_order_details(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = request.POST["id"]
            c_name = request.POST['c_name']
            c_price = request.POST['price']
            c_model = request.POST['model']
            c_am = request.POST['c_am']
            first = request.POST['first']
            last = request.POST['last']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            aadhar = request.POST['aadhar']
            office = request.POST['office']
            time = request.POST['time']
            date1 = request.POST['date1']
            date2 = request.POST['date2']
            days = request.POST['days']
            passengers = request.POST['passengers']
            driver_name = request.POST['driver']
            driver_amount = request.POST['d_bill']
            total_bill = request.POST['bill']
            payment_type = request.POST['payment']
            phone_pattern = r'^[6-9]\d{9}$'
            aadhar_pattern1 = r'\d{12}$'
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            name_pattern = r'^[a-zA-Z]+$'
            if not re.match(phone_pattern, phone):
                messages.warning(request, "wrong mobile number entered")
                return redirect('/show_ord')
            elif not re.match(aadhar_pattern1, aadhar):
                messages.warning(request, "wrong aadhar number entered")
                return redirect('/show_ord')
            elif not re.match(email_pattern, email):
                messages.warning(request, "wrong email address")
                return redirect('/show_ord')
            elif not re.match(name_pattern, first) and re.match(name_pattern, last):
                messages.warning(request, "Enter only character in first Name , last Name and Address")
                return redirect('/show_ord')
            elif not re.match(name_pattern, address):
                messages.warning(request, "Enter only character in address field")
                return redirect('/show_ord')
            else:
                messages.success(request, "Order Updated..!")
                order_model.objects.filter(id=id).update(c_name=c_name, c_model=c_model, c_am=c_am, c_price=c_price,
                                                         first=first, last=last, email=email, phone=phone,
                                                         address=address,
                                                         aadhar=aadhar, office=office, time=time, from_date=date1,
                                                         to_date=date2, days=days,
                                                         passengers=passengers, driver=driver_name,
                                                         d_bill=driver_amount,
                                                         payment_type=payment_type, bill=total_bill)
            return redirect("/show_ord")
    # else:
    #     return redirect('/login_view')


def update_car_details(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = request.POST["id"]
            c_name = request.POST["c_name"]
            c_model = request.POST["c_model"]
            c_am = request.POST["c_am"]
            c_price = request.POST["c_price"]
            file = request.FILES.get('c_file')
            employee_obj = Register_model.objects.get(id=id)
            employee_obj.file = file
            employee_obj.save()
            name_pattern = r'^[a-zA-Z]+$'
            number_pattern = r'^[A-Z]{2}-\d{2}/[A-Z]{2}-\d{4}$'
            price_pattern = r'^\d+$'
            if not re.match(name_pattern, c_name):
                messages.warning(request, "Car Name Only Character")
                return redirect('/admin_2')
            elif not re.match(number_pattern, c_model):
                messages.warning(request, "Not Valid Car Number")
                return redirect('/admin_2')
            elif not re.match(price_pattern, c_price):
                messages.warning(request, "Only Enter Numbers")
                return redirect('/admin_2')
            else:
                messages.success(request, "Data Updated..!")
                Register_model.objects.filter(id=id).update(c_name=c_name, c_model=c_model, c_am=c_am, c_price=c_price)
                return redirect("/admin_2")
    # else:
    #     return redirect('/login_view')


def delete_car_detail(request):
    if request.user.is_authenticated:
        id = request.GET["id"]
        Register_model.objects.filter(id=id).delete()
        messages.success(request, "One Row Deleted..!")
        return redirect('/admin_2')
    # else:
    #     return redirect('/login_view')


def delete_order_detail(request):
    if request.user.is_authenticated:
        id = request.GET["id"]
        order_model.objects.filter(id=id).delete()
        messages.success(request, "One Row Deleted..!")
        return redirect('/show_ord')


def register(request):
    if request.method == 'POST':
        # fm = UserCreationForm(request.POST)
        fm = signup(request.POST)
        if fm.is_valid():
            fm.save()
        return redirect('/login_view')
    else:
        # fm = UserCreationForm()
        fm = signup()
    return render(request, 'register.html', {'form': fm})


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successful..!")
                    return redirect('/index')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return redirect('/login_view')


def logout1(request):
    if request.user.is_authenticated:
        logout(request)
        messages.warning(request, "Logout Successful..!")
        return redirect('/login_view')
    # else:
    #     return redirect('/login_view')


4


def order(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            c_name = request.POST['c_name']
            c_price = request.POST['price']
            c_model = request.POST['model']
            c_am = request.POST['c_am']
            first = request.POST['first']
            last = request.POST['last']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            aadhar = request.POST['aadhar']
            office = request.POST['office']
            time = request.POST['time']
            date1 = request.POST['date1']
            date2 = request.POST['date2']
            days = request.POST['days']
            passengers = request.POST['passengers']
            driver_name = request.POST['driver']
            driver_amount = request.POST['d_bill']
            total_bill = request.POST['bill']
            payment_type = request.POST['payment']
            phone_pattern = r'^[6-9]\d{9}$'
            aadhar_pattern1 = r'\d{12}$'
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            name_pattern = r'^[a-zA-Z]+$'

            if not re.match(phone_pattern, phone):
                messages.warning(request, "wrong mobile number entered")
                return redirect('/index')
            elif not re.match(aadhar_pattern1, aadhar):
                messages.warning(request, "wrong aadhar number entered")
                return redirect('/index')
            elif not re.match(email_pattern, email):
                messages.warning(request, "wrong email address")
                return redirect('/index')
            elif not re.match(name_pattern, first) and re.match(name_pattern, last):
                messages.warning(request, "Enter only character in first Name , last Name and Address")
                return redirect('/index')
            elif not re.match(name_pattern, address):
                messages.warning(request, "Enter only character in address field")
                return redirect('/index')
            else:
                messages.success(request, "Order Successful Placed..!")
                data = order_model(c_name=c_name, c_model=c_model, c_am=c_am, c_price=c_price,
                                   first=first, last=last, email=email, phone=phone, address=address,
                                   aadhar=aadhar, office=office, time=time, from_date=date1, to_date=date2, days=days,
                                   passengers=passengers, driver=driver_name, d_bill=driver_amount,
                                   payment_type=payment_type, bill=total_bill)
                data.save()
                data1 = {'c_name': c_name, 'c_model': c_model, 'c_am': c_am, 'c_price': c_price,
                         'first': first, 'last': last, 'email': email, 'phone': phone, 'address': address,
                         'aadhar': aadhar, 'office': office, 'time': time, 'from_date': date1, 'to_date': date2,
                         'days': days,
                         'passengers': passengers, 'driver': driver_name, 'd_bill': driver_amount,
                         'payment_type': payment_type, 'bill': total_bill}
                return render(request, 'print_bill.html', data1)
        else:
            return HttpResponse("Fail..!")
    # else:
    #     return redirect('/login_view')

# def user(request):
#     return render(request, 'register.html')
#
#
# def user_regi(request):
#     first_name = request.POST['first_name']
#     last_name = request.POST['last_name']
#     username = request.POST['username']
#     gender = request.POST['gender']
#     email = request.POST['email']
#     phone = request.POST['phone']
#     address = request.POST['address']
#     aadhar = request.POST['aadhar']
#     password = request.POST['password']
#     password1 = request.POST['password1']
#     phone_pattern = r'^[6-9]\d{9}$'
#     aadhar_pattern1 = r'\d{12}$'
#     email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     username_pattern = r'^[a-zA-Z][a-zA-Z0-9._]{2,19}$'
#     name_pattern = r'^[a-zA-Z]+$'
#     password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_+=])[A-Za-z\d!@#$%^&*()-_+=]{8,}$'
#
#     if not re.match(phone_pattern, phone):
#         messages.warning(request, "wrong mobile number entered")
#         return redirect('/')
#     elif not re.match(aadhar_pattern1, aadhar):
#         messages.warning(request, "wrong aadhar number entered")
#         return redirect('/')
#     elif not re.match(email_pattern, email):
#         messages.warning(request, "wrong email address")
#         return redirect('/')
#     elif not re.match(username_pattern, username):
#         messages.warning(request, "Enter valid Username")
#         return redirect('/')
#     elif not re.match(name_pattern, first_name) and re.match(name_pattern, last_name):
#         messages.warning(request, "Enter only character in first Name and last Name")
#         return redirect('/')
#     elif not re.match(name_pattern, address):
#         messages.warning(request, "Enter only character in address field")
#         return redirect('/')
#     elif not re.match(password_pattern, password):
#         messages.warning(request,
#                          "password must be 8 character use uppercase, lowercase and special symbols and digits")
#         return redirect('/')
#     elif password != password1:
#         messages.warning(request, 'password not matched')
#     else:
#         data = user_registration_model(first_name=first_name, last_name=last_name, username=username, gender=gender,
#                                        email=email, phone=phone, address=address, aadhar=aadhar, password=password)
#         data.save()
#         messages.success(request, 'registration successful..!')
#         return redirect('/check_login')

# def sample(request):
#     name = request.POST['gender']
#     data = demo(name=name)
#     data.save()
#     return redirect('/')

# mobile_number = self.cleaned_data['mobile_number']
#         # Regular expression to match a typical 10-digit Indian mobile number
#         pattern = r'^[6-9]\d{9}$'
#         if not re.match(pattern, mobile_number):
#             raise forms.ValidationError("Please enter a valid mobile number.")
#         return mobile_number
