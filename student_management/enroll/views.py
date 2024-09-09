from django.http import JsonResponse
from .form import StudentRegistration
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import User

# Home view to display the student registration form and a list of all registered users
def home(request):
    form = StudentRegistration()  # Instantiate a blank student registration form
    stud = User.objects.all()  # Fetch all users from the User model
    return render(request, 'enroll/home.html', {'form': form, 'stu': stud})  # Render the home template with the form and user data

# Function to handle saving new user data or updating existing user data via AJAX
def save_data(request):
    if request.method == "POST":  # Ensure the request is a POST request
        form = StudentRegistration(request.POST)  # Bind the form with POST data
        if form.is_valid():  # Validate the form
            sid = request.POST.get('stuid')  # Get the student ID from the form, if any
            name = request.POST['name']  # Extract the 'name' field
            email = request.POST['email']  # Extract the 'email' field
            password = request.POST['password']  # Extract the 'password' field
            # Check if it's a new record or an update to an existing record
            if sid == '':
                usr = User(name=name, email=email, password=password)  # Create a new user if no ID is present
            else:
                usr = User(id=sid, name=name, email=email, password=password)  # Update the existing user
            usr.save()  # Save the user data to the database
            stud = User.objects.values()  # Fetch all user records as a list of dictionaries
            student_data = list(stud)  # Convert queryset to a list
            return JsonResponse({'status': 'Save', 'student_data': student_data})  # Return JSON response with updated data
        else:
            return JsonResponse({'status': 0})  # Return error response if form is invalid

# Function to register a new user via POST request, using AJAX
def register(request):
    if request.method == "POST":  # Handle POST request for registration
        form = StudentRegistration(request.POST)  # Bind form with submitted data
        if form.is_valid():  # Check if form data is valid
            sid = request.POST.get('stuid')  # Get student ID if updating an existing user
            name = request.POST['name']  # Extract the 'name' field
            email = request.POST['email']  # Extract the 'email' field
            password = request.POST['password']  # Extract the 'password' field
            # Save a new user or update existing user
            if sid == '':
                usr = User(name=name, email=email, password=password)  # Create a new user if no ID exists
            else:
                usr = User(id=sid, name=name, email=email, password=password)  # Update existing user data
            usr.save()  # Save user to the database
            stud = User.objects.values()  # Fetch all users
            student_data = list(stud)  # Convert queryset to a list of dictionaries
            return JsonResponse({"status": "Save", "student_data": student_data})  # Return JSON response
        else:
            return JsonResponse({"status": 0})  # Return error response if form is invalid
    else:
        form = StudentRegistration()  # Load a blank form for the GET request
    return render(request, 'enroll/register.html', {'form': form})  # Render the registration form

# Function to delete a user's data via POST request, using AJAX
def delete_data(request):
    if request.method == "POST":  # Ensure it's a POST request
        id = request.POST.get('sid')  # Get the student ID to be deleted
        pi = User.objects.get(pk=id)  # Fetch the user instance by primary key (ID)
        pi.delete()  # Delete the user

        # Reassign sequential IDs after deletion
        users = User.objects.all().order_by('id')  # Fetch all users in order of ID
        for index, user in enumerate(users):
            user.id = index + 1  # Reassign ID sequentially
            user.save()  # Save the updated user

        # Fetch updated user data
        stud = User.objects.values()  # Get all users after deletion
        student_data = list(stud)  # Convert queryset to list
        return JsonResponse({'status': 1, 'student_data': student_data})  # Return updated user data in JSON response
    else:
        return JsonResponse({'status': 0})  # Return error response if not a POST request

# Function to fetch user data for editing via POST request, using AJAX
def edit_data(request):
    if request.method == "POST":  # Ensure it's a POST request
        id = request.POST.get('sid')  # Get the student ID for editing
        student = User.objects.get(pk=id)  # Fetch the user instance by primary key (ID)
        # Return the student's current data in JSON format
        student_data = {"id": student.id, "name": student.name, "email": student.email, "password": student.password}
        return JsonResponse(student_data)  # Return user data for the frontend to populate the form

# Function to handle user login via the built-in Django AuthenticationForm
def user_login(request):
    if request.method == 'POST':  # Handle POST request for login
        form = AuthenticationForm(request, data=request.POST)  # Bind form with login data
        if form.is_valid():  # Check if the login data is valid
            username = form.cleaned_data.get('username')  # Get the username from the form
            password = form.cleaned_data.get('password')  # Get the password from the form
            user = authenticate(username=username, password=password)  # Authenticate the user
            if user is not None:  # If authentication is successful
                login(request, user)  # Log in the user
                return redirect('home')  # Redirect to home page
    else:
        form = AuthenticationForm()  # Show blank login form for GET request
    return render(request, 'enroll/login.html', {'form': form})  # Render the login page with the form

# Function to handle user logout
def user_logout(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to login page
