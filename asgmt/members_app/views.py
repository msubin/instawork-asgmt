from django.shortcuts import render


# Create your views here.
def member_list(request):
    return render(request, 'members_app/member_list.html', {})