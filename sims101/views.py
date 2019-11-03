from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import PermissionRequiredMixin 
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,  PageNotAnInteger
from decimal import Decimal
from .models import Index101
from .forms import IndexForm 
from commons.models import Description
from django.contrib import messages

@permission_required('sims101.index101_contributor')
def IndexListView(request):
    object_list = Index101.objects.all() 
    first = Index101.objects.first()  
    # description= Description.objects.get(sequence=Index101.SEQUENCE)
    description = get_object_or_404(Description, sequence=Index101.SEQUENCE)

    paginator = Paginator(object_list, 333)
    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage: 
        object_list = paginator.page(paginator.num_pages) 

    if request.method == 'POST':
        form = IndexForm(request.POST)
        context = {'form':form, 'object_list':object_list, 'first':first, 'description':description}
        if form.is_valid():              
            index_data = form.save()
            index_data.save()
            request.session['created'] = "true"    
            # request.session.modified = True
            return render(request, 'sims101/index_list.html', context)
    else:
        form = IndexForm()
        context = {'form':form, 'object_list':object_list, 'first':first, 'description':description}
    return render(request, 'sims101/index_list.html', context)

def ajax_change_session(request):  
    request.session['created'] = ""
    return render(request, 'sims101/index_delete.html') 

def ajax_calculate(request):     ###  must be the same as 'calculate' function  in model.py 
    data_one = int(request.GET.get('data_one'))
    data_two = int(request.GET.get('data_two'))
    data_three = int(request.GET.get('data_three')) 
    calculated_value = ((data_one + data_two) / data_three ) * 100000
    calculated_value = format(calculated_value, '.2f')
    return render(request, 'sims101/calculated_value.html', {'calculated_value':calculated_value})

class IndexUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('sims101.index101_validator') 
    model = Index101
    form_class = IndexForm
    template_name = 'sims101/index_update.html'
    success_url = reverse_lazy('sims101:index_list')  

# @permission_required('sims101.index101_validator')
# def IndexUpdateView(request, pk): 

#     obj = get_object_or_404(Index101, pk=pk)

#     form = IndexForm(request.POST or None, instance=obj)
    
#     if form.is_valid():              
#         # obj = form.save(commit=False)
#         object = obj.save()
#         context = {'form':form, 'object':object}
#         messages.success(request, "You successfully updated the index")
#         return render(request, 'sims101/index_update.html', context)

#     context = {'form':form, 'error':'The form was not updated successfully. Please enter values again.'}
#     return render(request, 'sims101/index_update.html', context)





class IndexDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('sims101.index101_validator')    
    model = Index101
    template_name = 'sims101/index_delete.html'
    success_url = reverse_lazy('sims101:index_list')  
    


import csv
from django.http import HttpResponse
from django.contrib.auth.models import User

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="index.csv"'

    writer = csv.writer(response)
    writer.writerow(['FT', 'DT', 'PT', 'NPFD'])

    indexes = Index101.objects.all().values_list('data_one', 'data_two', 'data_three', 'calculated_value')
    for index in indexes:
        writer.writerow(index)

    return response

 
 # class IndexCreateView(PermissionRequiredMixin, CreateView):
#     permission_required = ('sims101.index-contributor') 
#     model = Index101
#     form_class = IndexForm 
#     template_name = 'sims101/index_create.html'
#     login_url = 'login'
#     success_url = reverse_lazy('sims101:index_list')  
#     ### CreateView, UpdateView에 success_url을 제공하지 않는 경우, 해당 model instance의 get_absolute_url 주소로 이동이 가능한지 체크한다 by Django ]]

#     def form_invalid(self, form):  
#         first = Index101.objects.first()  
#         description = Description.objects.get(sequence=Index101.SEQUENCE)  
#         object_list = Index101.objects.all()  
#         context = {'first':first, 'description':description, 'form':form, 'object_list':object_list} 
#         return render(self.request, 'sims101/index_list.html', context)

#         # return HttpResponseRedirect('/101/')

#     def setup(self, request, *args, **kwargs): 
#         super().setup(request, *args, **kwargs)
#         request.session['created'] = "true"
#         request.session.modified = True
# 
#  You can populate with some  initialization data for the form. 
    # def get_initial(self, *args, **kwargs):
    #         initial = super(IndexCreateView, self).get_initial(**kwargs)
    #         initial['title'] = 'My Title'
    #         return initial


# class IndexListView(PermissionRequiredMixin, ListView):
#     permission_required = ('sims101.index-contributor') 
#     model = Index101                      ###  Or,   queryset = Post.objects.all()
#     template_name = 'sims101/index_list.html'   ### default context name is 'object_list'. To change it, enter context_object_name = 'posts'
#     # paginate_by = 3       ## 3 objects per page 

#     def get_context_data(self, **kwargs):   ### get the first object to be used in the index_list.html 
#         context = super(IndexListView, self).get_context_data(**kwargs) 
#         context['first'] = Index101.objects.first()  
#         context['description'] = Description.objects.get(sequence=Index101.SEQUENCE)
#         if not ('form' in context):
#             context['form'] = IndexForm()
#         return context


# class IndexDetailView(PermissionRequiredMixin, DetailView):
#     permission_required = ('sims101.index-contributor') 
#     model = Index101
#     template_name = 'sims101/index_detail.html' 