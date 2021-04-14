from django.shortcuts import render
def index(request):
    return render(request,'samp.html',context={'name':'vishwa','mail':'vipvishwa505S@gmail.com'})



def if_loop(request):
    login=False
    return render(request,'if.html',context={'login':login})


def for_loop(request):
    return render(request,'for.html',context={'items':['apple','ball','cat','dog']})



    

