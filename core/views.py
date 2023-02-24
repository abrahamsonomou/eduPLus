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

def blogDetails(request):
    return render(request,'client/pages/blog-detail.html')

def shop(request):
    return render(request,'client/pages/shop.html')

def shopProductDetail(request):
    return render(request,'client/pages/shop-product-detail.html')

def checkout(request):
    return render(request,'client/pages/checkout.html')

def cart(request):
    return render(request,'client/pages/cart.html')


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

def examen(request):
    return render(request,'client/examen/examen.html')  