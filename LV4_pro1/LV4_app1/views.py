from django.shortcuts import render

# Create your views here.
def index(request):
    context_dic={'text':'hello world','number':200}
    return render(request,'LV4_app1/index.html',context_dic)

def other(request):
    return render(request,'LV4_app1/other.html')

def relative(request):
    return render(request,'LV4_app1/relative_urls_temp.html')
