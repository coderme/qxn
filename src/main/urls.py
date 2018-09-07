from django.urls import path
from . import views as v

urlpatterns = [
    path('<slug:slug>/', v.detailed, name='question_details'),
    path('tag/<slug:title>/', views.tagged, name='tagged'),

    # forms view
    # answer forms
    path('answer/<int:pk>/add/', views.add_answer, name='add_answer'),
    path('answer/<int:pk>/edit/', views.edit_answer, name='edit_answer'),
    path('answer/<int:pk>/del/', views.del_answer, name='del_answer'),

    # voting
    path('upvote/answer/<int:pk>/', views.upvote_answer, name='upvote_answer'),
    path('downvote/answer/<int:pk>/',
         views.downvote_answer, name='downvote_answer'),

    # comment forms
    path('comment/<int:pk>/add/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:pk>/del/', views.del_comment, name='del_comment'),

    # voting
    path('upvote/comment/<int:pk>/',
         views.upvote_answer, name='upvote_comment'),
    path('downvote/comment/<int:pk>/',
         views.downvote_answer, name='downvote_comment'),

    # reply forms
    path('reply/<int:pk>/add/', views.add_reply, name='add_reply'),
    path('reply/<int:pk>/edit/', views.edit_reply, name='edit_reply'),
    path('reply/<int:pk>/del/', views.del_reply, name='del_reply'),

    # reply voting
    path('upvote/reply/<int:pk>/', views.upvote_reply, name='upvote_reply'),
    path('downvote/reply/<int:pk>/',
         views.downvote_reply, name='downvote_reply'),


]
