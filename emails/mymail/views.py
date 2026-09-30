from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailsForm


def send_email(request):
    form = EmailsForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        send_mail(
            form.cleaned_data["subject"],
            form.cleaned_data["message"],
            "your_email@gmail.com",
            [form.cleaned_data["recipient"]],
            fail_silently=False,
        )
        return render(request, "success.html")

    return render(request, "send_email.html", {"form": form})