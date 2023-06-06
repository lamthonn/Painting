from django.shortcuts import render, get_object_or_404,redirect
from .models import Painting, CreateUserForm, Like, Comment
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PaintingUploadForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# from .forms import PaintingSearchForm
def home(request):
    paintings = Painting.objects.all()
    return render(request,'pages/home.html',{'paintings':paintings})

def painting_list(request):
    paintings = Painting.objects.all()
    paintings_like = Like.objects.filter(user=request.user)
    return render(request,'pages/painting_list.html',{'paintings':paintings, "paintings_like": paintings_like})

def painting_detail(request,pk):
    painting = get_object_or_404(Painting,pk=pk)
    comments = Comment.objects.all()
    paintings = Painting.objects.all()
    return render(request,'pages/paiting_detail.html',{'painting':painting, 'paintings':paintings, 'comments': comments})

@login_required
@user_passes_test(lambda u: u.is_staff)
def upload_painting(request):
    if request.method == 'POST':
        form = PaintingUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PaintingUploadForm()
    return render(request,'pages/upload.html',{'form':form})

# def painting_search(request):
#     form = PaintingSearchForm(request.GET)
#     if form.is_valid():
#         query = form.cleaned_data['query']
#         name = form.cleaned_data['name']
#         if name:
#             paintings = Painting.objects.filter(
#                 name__icontains=query,
#                 name=name
#             )
#         else:
#             paintings = Painting.objects.filter(
#                 name__icontains=query
#             )
#         return render(request, 'pages/painting_search.html', {'paintings': paintings})
#     else:
#         return render(request, 'pages/painting_search.html')
#     form = PaintingSearchForm(request.GET)
def painting_search(request):
    # form = PaintingSearchForm(request.GET)
    if 'query' in request.GET:
        query = request.GET.get('query')
        # paintings = Painting.objects.filter(name__icontains = query)
        multiple_query = Q(Q(name__icontains=query) | Q(upload_date__icontains=query))
        paintings = Painting.objects.filter(multiple_query)
        return render(request, 'pages/painting_search.html', {'paintings': paintings})
    else:
        paintings = Painting.objects.all()
        context = {
            'paintings': paintings 
        }
    return render(request, 'pages/painting_search.html',context)
        
def contact(request):
    return render(request, 'pages/contact.html')       

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form}
    return render(request, 'pages/register.html', context)  

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'user or password not correct!')
    context = {}
    return render(request, 'pages/login.html', context)  

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def profile(request):
    painting_likes = Like.objects.filter(user=request.user)
    return render(request, 'pages/profile_user.html', {'painting_likes':painting_likes})  

def like(request, pk):
    pain = get_object_or_404(Painting, pk=pk)
    like = Like(user=request.user, painting=pain)
    like.save()
    return redirect('list')

def like_delete(request, pk):
    pain = get_object_or_404(Painting, pk=pk)
    like = get_object_or_404(Like, user=request.user, painting=pain)
    like.delete()
    return redirect('list')
        
def add_comment(request, pk):
    try: 
        if(request.method == 'POST'):
            pain = get_object_or_404(Painting, pk=pk)
            #vì request.body trả về chuỗi dạng byte nên phải chuyển thành dạng utf8
            cmt_req = json.loads(request.body.decode('utf-8'))
            print(request.body)
            print(cmt_req)
            new_cmt = Comment(user=request.user, painting=pain, cmt=cmt_req.get('cmt'))
            new_cmt.save()
            res = {'messages': 'success'}
            return JsonResponse(res)
    except Exception as e:  
         return JsonResponse({'message': 'error', 'error': str(e)})
