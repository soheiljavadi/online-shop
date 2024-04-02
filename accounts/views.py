from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import UserLoginForm, UserRegisterFrom,\
    MyAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from product.models import Comment
from .models import User
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView,\
    DeleteView, UpdateView


# Create your views here.
