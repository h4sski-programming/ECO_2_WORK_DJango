from django.shortcuts import redirect, render
from .forms import SigninForm


def log_in(response):
    return render(response, 'register/log_in.html', {})


def log_out(response):
    return render(response, 'register/log_in.html', {})


def sign_in(response):
    if response.method == 'POST':
        form = SigninForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SigninForm()

    return render(response, 'register/sign_in.html', {
        'form': form,
    })
