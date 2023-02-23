from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'client/pages/home.html')

def about(request):
    return render(request,'client/pages/about.html')

def contact(request):
    return render(request,'client/pages/contact.html')

def blog(request):
    return render(request,'client/pages/blog.html')

def shop(request):
    return render(request,'client/pages/shop.html')

def shopProductDetail(request):
    return render(request,'client/pages/shop-product-detail.html')

def instructors(request):
    return render(request,'client/pages/instructors.html')

def instructorDetails(request):
    return render(request,'client/pages/instructorDetails.html')

def becomeInstructor(request):
    return render(request,'client/pages/become-instructor.html')



def coursDetails(request):
    return render(request,'client/pages/coursDetails.html')

def coursCategorie(request):
    return render(request,'client/pages/coursCategorie.html')

def cours(request):
    return render(request,'client/pages/cours.html')  