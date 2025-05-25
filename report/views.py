
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        passwords = request.POST.get('passwords')

        try:
            user = sale.objects.get(user=user)
            if user.passwords == passwords:
                request.session['user_id'] = user.id
                return redirect(powerbi_dashboard)
            else:     
                return HttpResponse("<script>alert('Incorrect password');window.location='/'</script>")
        except sale.DoesNotExist:
            return HttpResponse("<script>alert('User not Found');window.location='/'</script>")

    return render(request, 'index.html')

def powerbi_dashboard(request):
    embed_url = "https://app.powerbi.com/view?r=eyJrIjoiNWJmMGI1M2UtM2YyZC00ZjNiLWI1NjAtYWE0Nzc3ODgxYTI3IiwidCI6IjUwMDBmZmM1LTgxNjQtNDc2MC04MDNkLTE3ZWMwYzdiY2E5ZSJ9"
    return render(request, "sale.html", {'embed_url': embed_url})
