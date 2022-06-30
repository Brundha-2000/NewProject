# from django.shortcuts import render,redirect
# from django.http import HttpResponse
#
#
# # Create your views here.
# # def index(request):
# #     return HttpResponse("first view")
#
#
# # def studentForm(request):
# #     return render(request,'trailapp/studentform.html', {'var': studentform()})
# from .forms import studentform
# from .models import studentmodel
#
# def std(request):
#     if request.method == "POST":
#         form =studentform(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/show')
#             except:
#                 pass
#     else:
#         form = studentform()
#     return render(request, 'index.html', {'form': form})
# def show(request):
#     stdu = studentmodel.objects.all()
#     return render(request,"show.html",{'stdu':stdu})
# def edit(request, id):
#     stdu = studentmodel.objects.get(id=id)
#     return render(request,'edit.html', {'stdu':stdu})
#
# def update(request, id):
#     stdu =studentmodel.objects.get(id=id)
#     form = studentform(request.POST, instance = stdu)
#     if form.is_valid():
#         form.save()
#         return redirect("/show")
#     return render(request, 'edit.html', {'stdu': stdu})
# def destroy(request, id):
#     stdu = studentmodel.objects.get(id=id)
#     stdu.delete()
#     return redirect("/show")
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View, generic
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from .models import studentmodel, deptmodel
from .forms import studentform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view
from .serializers import StudentmodelSerializer,DeptmodelSerializer

@api_view(['GET'])
def mmdv(request):
    stdobj = studentmodel.objects.all()
    deptobj = deptmodel.objects.all()
    Stdserialieobj=StudentmodelSerializer(stdobj,many=True)
    Deptserialeobj=DeptmodelSerializer(deptobj,many=True)
    Resultmodel=Stdserialieobj.data+Deptserialeobj.data
    return Response(Resultmodel)
    # return render(request,"show.html",{"studentmodel":stdobj,"deptmodel":deptdisplay})

# class multiplemodel(TemplateView):
#     template_name = 'multiplemodel.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # person = get_object_or_404(,studentmodel)
#         context['studentmodel'] = studentmodel
#         context['studentform'] = studentform(instance=studentmodel)
#         context['deptform'] = deptform(instance=deptmodel)
#         # context['email_form'] = EmailForm(instance=person.email)
#
#         return context


class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'



def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == "POST":
        #id=request.POST['id']
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        phone = request.POST['phone']
        obj = studentmodel.objects.create( name=name, age=age, email=email,phone=phone)
        obj.save()
        return redirect('show/')
def show(request):
    details = studentmodel.objects.all()
    #details1 = deptmodel.objects.all()
    return render(request,'show.html',{'details':details})

    print("details = ", details)
    print("type of details = ", type(details))



def edit(request, id):
    object =studentmodel.objects.get(id=id)
    #object = studentmodel.objects.all()
    return render(request, 'edit.html', {'object': object})


def update(request,id):
    object=studentmodel.objects.get(id=id)
    form=studentform(request.POST,instance=object)
    if form.is_valid:
        form.save()

   # object=studentmodel.objects.all()
    object.save()
    return redirect( "/")

def delete(request, pk):
    studentmodel.objects.filter(id=pk).delete()
    return redirect("/")

@api_view(['GET', 'POST'])
def snippet_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = studentmodel.objects.all()
        serializer = StudentmodelSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentmodelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(['GET','PUT','DELETE'])
# def tutorial_detail(request, pk):
#     try:
#         tutorial = studentmodel.objects.get(pk=pk)
#     except studentmodel.DoesNotExist:
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         tutorial_serializer = StudentmodelSerializer(tutorial)
#         return JsonResponse(tutorial_serializer.data)
#
#     elif request.method == 'PUT':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = StudentmodelSerializer(tutorial, data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data)
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         tutorial.delete()
#         return JsonResponse({'message': 'studentmodel was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET'])
# def tutorial_list_published(request):
#     tutorials = studentmodel.objects.filter(published=True)
#
#     if request.method == 'GET':
#         tutorials_serializer = StudentmodelSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)


# def tutorial_list():
#     return None
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet =studentmodel.objects.get(pk=pk)
    except studentmodel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentmodelSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentmodelSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        snippet.delete()
        message={'message':'deleted successfully'}
        return JsonResponse(message, status=status.HTTP_204_NO_CONTENT)

class CreateClassbasedview(CreateAPIView):
    serializer_class = StudentmodelSerializer

class ListClassbasedview(ListAPIView):
    queryset = studentmodel.objects.all()
    serializer_class = StudentmodelSerializer

class RetrieveClassbasedView(RetrieveAPIView):
    queryset = studentmodel.objects.all()
    serializer_class = StudentmodelSerializer

class UpdateClassbasedView(UpdateAPIView):
    queryset = studentmodel.objects.all()
    serializer_class = StudentmodelSerializer

class DestroyClassbasedView(DestroyAPIView):
    queryset = studentmodel.objects.all()
    serializer_class = StudentmodelSerializer

from rest_framework.viewsets import ModelViewSet

from .models import studentmodel
from .serializers import StudentmodelSerializer

class studentModelView(ModelViewSet):
    queryset = studentmodel.objects.all()
    serializer_class = StudentmodelSerializer


from rest_framework.response import Response
from rest_framework.views import APIView


class ProtectedAPIView(APIView):

    def get(self, request, format=None):
        content = {
            'message': 'Hey! you have authenticated!'
        }
        return Response(content)



class CreateStudentApiView(generics.CreateAPIView):
    queryset = studentmodel.objects.all()
    serializer_class = StudentmodelSerializer


class StudentListView(ListAPIView):
    queryset = studentmodel.objects.all()
    serializer_class = StudentmodelSerializer
    model = studentmodel
    # paginate_by = 10  # the number of students to return in each page

class StudentView(RetrieveAPIView):
    queryset = studentmodel.objects.all()
    serializer_class = StudentmodelSerializer
    model = studentmodel







