from django.shortcuts import render, get_object_or_404,redirect
from .models import Painting
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PaintingUploadForm
from django.db.models import Q
# from .forms import PaintingSearchForm
def home(request):
    paintings = Painting.objects.all()
    return render(request,'pages/home.html',{'paintings':paintings})

def painting_list(request):
    paintings = Painting.objects.all()
    return render(request,'pages/painting_list.html',{'paintings':paintings})

def painting_detail(request,pk):
    painting = get_object_or_404(Painting,pk=pk)
    paintings = Painting.objects.all()
    return render(request,'pages/paiting_detail.html',{'painting':painting, 'paintings':paintings})

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
        
