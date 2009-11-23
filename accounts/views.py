from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from velocette.accounts.forms import UserCreationForm, ProfileForm

def create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            request.notifications.create('Your account has been created. Please sign in.')
            return HttpResponseRedirect(reverse('new_session'))
    else:
        form = UserCreationForm()

    return render_to_response('accounts/new.html', {'new_account_form':form},
        context_instance=RequestContext(request))

@login_required
def update(request, account_id):
    # TODO: extract this into @require_same_user
    if str(request.user.id) != str(account_id):
        request.notifications.create("Editing another user's profile is not allowed.")
        return HttpResponseRedirect(reverse('tasks_index'))

    profile = request.user.get_profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            request.notifications.create('Your account changes were saved.')
    else:
        form = ProfileForm(instance=request.user)

    return render_to_response('accounts/edit.html', {
            'edit_account_form' : form,
            'change_password_form' : PasswordChangeForm(request.user)
        },
        context_instance=RequestContext(request))

@login_required
def change_password(request, account_id):
    # TODO: extract this into @require_same_user
    if str(request.user.id) != str(account_id):
        request.notifications.create("Changing another user's password is not allowed.")
        return HttpResponseRedirect(reverse('tasks_index'))

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # TODO: send an email notification about the password change
            request.notifications.create('Your password has been changed.')
            return HttpResponseRedirect(reverse('edit_account', args=[account_id]))
    else:
        form = PasswordChangeForm(request.user)

    return render_to_response('accounts/change_password.html', {'change_password_form':form},
        context_instance=RequestContext(request))
