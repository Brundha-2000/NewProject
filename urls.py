from django.urls import path
from . import views
from django.urls import  re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns=[
    path('', views.index, name='index'),
    path('m/', views.mmdv),
    # path('multiplemodel/',views.multiplemodel.as_view()),++++O
    path('create', views.create, name="create"),
    path('show/', views.show, name="show"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    re_path(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
    path('snippets/', views.snippet_list), #function based view
    path('snippets/<int:pk>', views.snippet_detail),
    path('CreateClassbasedview/',views.CreateClassbasedview.as_view()),
    path('ListClassbasedview/',views.ListClassbasedview.as_view()),
    path('RetrieveClassbasedview/<int:pk>',views.RetrieveClassbasedView.as_view()),
    path('UpdateClassbasedview/<int:pk>',views.UpdateClassbasedView.as_view()),
    path('DestroyClassbasedview/<int:pk>',views.DestroyClassbasedView.as_view()),
    # path('Modelbasedview/', views.UserViewSet.as_view({'get':'list'})),
    # path('Modelbasedview/<int:pk>/', views.UserViewSet.as_view({'get':'retrieve'})),
    path('list/', views.studentModelView.as_view({'get':'list'})),
    path('GET/<int:pk>/', views.studentModelView.as_view({'get':'retrieve'})),
    path('update/<int:pk>/', views.studentModelView.as_view({'put':'update'})),
    path('create/', views.studentModelView.as_view({'post':'create'})),
    path('delete/<int:pk>/', views.studentModelView.as_view({'delete':'destroy'})),
    path('partialupdate/<int:pk>/', views.studentModelView.as_view({'patch':'partial_update'})),
    path('api/protected/', views.ProtectedAPIView.as_view(), name='protected'),
    path('api/token-auth/', ObtainAuthToken.as_view(), name='auth_token'),
    # path('api/ExampleView/',views.ExampleView.as_view()),
    path('CreateStudentApiView/create',views.CreateStudentApiView.as_view()),
    path('students/', views.StudentListView.as_view(), name="students"),
    path('students/<int:pk>/',views.StudentView.as_view(), name="student-detail"),

]
urlpatterns = format_suffix_patterns(urlpatterns)
