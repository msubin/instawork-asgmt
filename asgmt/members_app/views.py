from django.shortcuts import render
from .models import Member


# Create your views here.
def member_list(request):
    members = Member.objects.all()
    return render(request, 'members_app/member_list.html', {'members': members})