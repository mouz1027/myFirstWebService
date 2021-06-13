from django.shortcuts import render


# Create your views here.
def hello(request):
    # return HttpResponse("Hello World!")
    context = {'hello': 'Hello World!'}
    return render(request, 'hello.html', context)  # 将绑定的数据传入前台
