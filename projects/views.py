from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Project , Tag
from .forms import ProjectForm ,ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProject ,paginateProjects
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger ,EmptyPage
# Create your views here.


def projects(request):
    projects,search_query = searchProject(request)
    custom_range, projects = paginateProjects(request, projects, 6)
    context = {'projects': projects,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request,'projects/projects.html',context=context)


def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    form =ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        
        projectObj.getVoteCount
        
        
        messages.success(request,'Your Review is Successfully Submited ')
        return redirect('project',pk=projectObj.id)
        
    tags = projectObj.tags.all()
    return render(request,'projects/single_project.html',{'project':projectObj,'tags':tags,'form':form})

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            form.save_m2m()
            
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
        
            # Redirect to the projects page after successfully creating the project
            # Assuming 'projects' is the name of the view for the projects page
    context = {'form': form}
    
    return render(request, 'projects/project_form.html', context=context)

@login_required(login_url='login')
def updateProject(request,pk):
    # object get kra jo update krna hai then usko instance bhejo form me to prefill data in form.
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method=='POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        form=ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    context={'form':form,'project':project}
    
    return render(request,'projects/project_form.html',context=context)

@login_required(login_url='login')
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    
    context =  {'object':project}
    return render(request ,'delete_template.html',context= context)
