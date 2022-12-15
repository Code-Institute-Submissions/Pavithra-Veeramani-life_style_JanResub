from django.shortcuts import render, redirect, get_object_or_404


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)
