from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import TemplateView
from pandorastrum.models import GamesModel, AboutModel, AboutTeamImage, ThanksName, BlogModel

# Redirection of root url
def redirect_root(request):
    return redirect("/home/")

# Create your views here.
def home_pageView(request):
    # queryset =
    context = {

    }
    return render(request, "index.html", context)

def game_pageView(request):
    queryset = GamesModel.objects.all()
    context = {
        "games" : queryset
    }
    return render(request, "games.html", context)

def portfolio_pageView(request):
    # queryset =
    context = {

    }
    return render(request, "portfolio.html", context)

def blog_pageView(request):

    blog = BlogModel.objects.all()
    
    context = {
        "blog" : blog,
    }
    return render(request, "blog.html", context)

def blog_detailView(request, id):
    instance = get_object_or_404(BlogModel, id=id)
    context = {
        "instance" : instance
    }
    return render(request, "blog_detail.html", context)



def about_pageView(request):
    queryset = AboutModel.objects.all()
    team = AboutTeamImage.objects.all()
    thanks = ThanksName.objects.all()
    pro_address1 = AboutModel.objects.values_list('pro_address1', flat=True)[0]
    pro_address2 = AboutModel.objects.values_list('pro_address2', flat=True)[0]
    pro_city = AboutModel.objects.values_list('pro_city', flat=True)[0]
    pro_country = AboutModel.objects.values_list('pro_country', flat=True)[0]
    pro_mob = AboutModel.objects.values_list("pro_mobile", flat=True)[0]
    pro_email = AboutModel.objects.values_list("pro_email", flat=True)[0]
    op_address1 = AboutModel.objects.values_list("op_address1", flat=True)[0]
    op_address2 = AboutModel.objects.values_list("op_address2", flat=True)[0]
    op_city = AboutModel.objects.values_list("op_city", flat=True)[0]
    op_country = AboutModel.objects.values_list("op_country", flat=True)[0]
    op_email = AboutModel.objects.values_list("op_email", flat=True)[0]
    context = {
        "about" : queryset,
        "team" : team,
        "ty" : thanks,
        "pro_address1" : pro_address1,
        "pro_address2" : pro_address2,
        "pro_city" : pro_city,
        "pro_country" : pro_country,
        "pro_mob" : pro_mob,
        "pro_email" : pro_email,
        "op_address1" : op_address1,
        "op_address2" : op_address2,
        "op_city" : op_city,
        "op_country" : op_country,
        "op_email" : op_email
    }
    return render(request, "about.html", context)

def error_pageView(request):
    # queryset =
    context = {

    }
    return render(request, "error.html", context)


from django.shortcuts import render_to_response
from django.template import RequestContext
def handler404(request):
    response = render_to_response('error.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response




