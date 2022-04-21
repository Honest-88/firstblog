from django.urls import path, include
from users import views


#app_name = 'users'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('contact/', views.ContactView.as_view(), name="contact"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('change_password/', views.change_password, name='change_password'),

    path('dmca/', views.DmcaView.as_view(), name="dmca"),
    path('privacy/', views.PrivacyView.as_view(), name="privacy"),
    path('terms/', views.TermsView.as_view(), name="terms"),
    path('about/', views.AboutView.as_view(), name="about"),


    

]

