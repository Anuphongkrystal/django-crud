from django.shortcuts import render,redirect,get_object_or_404
from Cryptocurrencies.models import *
from .forms import CryptoForm

def home(request):
    data = Crypto.objects.all()

    return render(request,'index.html',{'data':data})

def search(request):
    symbol = request.POST['symbol'];
    if symbol == "":
        data = Crypto.objects.all()
        return redirect('/')
    else:
        data = Crypto.objects.filter(symbol__contains=symbol)

    return render(request,'index.html',{'data':data})

def insert(request):
    context = {}

    form  = CryptoForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request,'form.html',context)

def delete(request,pk):
    delete_id = get_object_or_404(Crypto,pk=pk)

    if request.method == 'POST':
        delete_id.delete()
        return redirect('/')
    return render(request,'index.html',{'delete_id':delete_id})

def edit(request,pk):
    name  = request.POST['name']
    symbol = request.POST['symbol']
    price = request.POST['price']
    image = request.POST['image']

    checked = Crypto.objects.get(id=pk)
    if checked != None:
        checked.name = name
        checked.symbol = symbol
        checked.price = price
        checked.image = image
        checked.save()

        return redirect('/')

    return render(request,'index.html',{'edit_id':edit_id})
