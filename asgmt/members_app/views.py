from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm


# Create your views here.
def get_member_list(request):
    members = Member.objects.all()
    return render(request, 'members_app/member_list.html', {'members': members})


def create_member(request):
    form = MemberForm(request.POST or None, initial={'isAdmin': 'False'})
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = MemberForm()
    return render(request, 'members_app/new_member.html', {'form': form})


def update_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    form = MemberForm(request.POST, instance=member)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/', pk=member.pk)
    else:
        form = MemberForm(instance=member)
    return render(request, 'members_app/update_member.html', {'form': form, 'member': member})


def delete_member(pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()
    return redirect('/')