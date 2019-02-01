from django.urls import path
from . import views as v

urlpatterns = [
    path('<slug:slug>/', v.QuestionDetail.as_view(),
         name='question_details'),
    path('tag/<slug:title>/', v.tagged, name='tagged'),

    # forms view
    # answer forms
    path('answer/<int:pk>/add/', v.add_answer, name='add_answer'),
    path('answer/<int:pk>/edit/', v.edit_answer, name='edit_answer'),
    path('answer/<int:pk>/del/', v.del_answer, name='del_answer'),

    # voting
    path('upvote/answer/<int:pk>/', v.upvote_answer, name='upvote_answer'),
    path('downvote/answer/<int:pk>/',
         views.downvote_answer, name='downvote_answer'),

    # comment forms
    path('comment/<int:pk>/add/', v.add_comment, name='add_comment'),
    path('comment/<int:pk>/edit/', v.edit_comment, name='edit_comment'),
    path('comment/<int:pk>/del/', v.del_comment, name='del_comment'),

    # voting
    path('upvote/comment/<int:pk>/',
         views.upvote_answer, name='upvote_comment'),
    path('downvote/comment/<int:pk>/',
         views.downvote_answer, name='downvote_comment'),

    # reply forms
    path('reply/<int:pk>/add/', v.add_reply, name='add_reply'),
    path('reply/<int:pk>/edit/', v.edit_reply, name='edit_reply'),
    path('reply/<int:pk>/del/', v.del_reply, name='del_reply'),

    # reply voting
    path('upvote/reply/<int:pk>/', v.upvote_reply, name='upvote_reply'),
    path('downvote/reply/<int:pk>/',
         views.downvote_reply, name='downvote_reply'),


]
