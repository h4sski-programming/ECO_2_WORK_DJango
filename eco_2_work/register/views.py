from django.shortcuts import render

# Create your views here.


def log_in(response):
    return render(response, 'register/log_in.html', {})


def log_out(response):
    return render(response, 'register/log_in.html', {})


def sign_in(response):
    form = 'a'
    return render(response, 'register/sign_in.html', {
        'form': form,
    })
