from django.shortcuts import render, redirect

posts = [
    {
        "Title": "Some title",
        "Description": "Some description etc.",
        "Category": "Some category",
        "Date": "Some date",
        "Author": "Someone"
    }
]

def index(request):
    return render(request, 'index.html', {"articles": posts, 'page': 'index'})

def about_us(request):
    return render(request, 'about_us.html', {'page': 'about_us'})

def contact(request):
    if request.method == "GET":
        return render(request, 'contacts.html', {'page': 'contacts'})
    else:
        with open('C:/Users\пк\Documents\My_projects\django_by_stepik\main\info_from_users.txt', 'a') as file:
            file.writelines(f"Name: {request.POST['name']}, Email: {request.POST['email']}, Subject: {request.POST['subject']}, Message: {request.POST['message']}")
        return redirect(contact)
