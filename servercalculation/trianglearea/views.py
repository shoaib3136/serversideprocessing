from django.shortcuts import render

# Create your views here.
def trianglearea(request):
    context={}
    context["Height"]='0'
    context["Base"]='0'
    context["Area_of_Triangle"]='0'
    if request.method=="POST":
        print("POST method is used")
        Height=request.POST.get("Height",0)
        Base=request.POST.get("Base",0)
        Height_num=int(Height)
        Base_num=int(Base)
        Area_of_Triangle=0.5*(Height_num)*(Base_num)
        context["Height"]=Height_num
        context["Base"]=Base_num
        context["Area_of_Triangle"]=Area_of_Triangle
        print('Height:',Height_num)
        print('Base:',Base_num)
        print('Area_of_Triangle:',Area_of_Triangle)
    return render(request ,"trianglearea/trianglearea.html" ,context)
