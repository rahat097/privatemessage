from django.urls import path
#from . import views
from . views import messageinbox,messagedetailinbox,messageoutbox,messagedetailoutbox,messagedialog



urlpatterns = [
    path('', messageinbox, name='messageinbox'),
    path('outbox', messageoutbox, name='messageoutbox'),
    path('inbox/detail/<int:id>', messagedetailinbox, name='messagedetail'),
    path('outbox/detail/<int:id>', messagedetailoutbox, name='messagedetailoutbox'),
    path('dialog/<int:id>', messagedialog, name='messagedialog'),
    #path('<int:pk>', cricketgame, name='cricketgame'),
    #path('accept/<int:id>', cricketaccept, name='cricketaccept'),
    #path('delete/<int:id>', cricketdelete, name='cricketdelete'),




    ]