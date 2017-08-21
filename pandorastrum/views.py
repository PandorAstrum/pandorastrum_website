import datetime
from functools import reduce

from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import TemplateView
from pandorastrum.models import GamesModel, AboutModel, AboutTeamImage, ThanksName, BlogModel, BlogContentModel
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from urllib.parse import quote_plus
import operator
from django.db.models import Q

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

# blog normal block ------------------------------------------------------------------------
def blog_pageView(request, tag_slug=None, **kwargs):
    blog_list   = BlogModel.objects.all().order_by("-created")
    # paginator
    paginator   = Paginator(blog_list, 10) # Show 25 contacts per page
    page        = request.GET.get('page')
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)

    # tags
    tag_list = Tag.objects.all()
    tag_slugs = request.GET.get("tag_slug")
    if tag_slugs:
        blog_list = BlogModel.objects.filter(tags__slug=tag_slugs)
        # paginator
        paginator = Paginator(blog_list, 10)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            blog_list = paginator.page(page)
        except PageNotAnInteger:
            blog_list = paginator.page(1)
        except EmptyPage:
            blog_list = paginator.page(paginator.num_pages)

    # search
    query = request.GET.get("q")
    if query:
        query_list = query.split()
        blog_list = BlogModel.objects.filter(
                    reduce(operator.and_,(Q(blog_title__icontains=q) for q in query_list)) |
                    reduce(operator.and_, (Q(tags__slug__icontains=q) for q in query_list))
        )
        # paginator
        paginator = Paginator(blog_list, 10)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            blog_list = paginator.page(page)
        except PageNotAnInteger:
            blog_list = paginator.page(1)
        except EmptyPage:
            blog_list = paginator.page(paginator.num_pages)

    # year month
    date_field = 'published_on'
    archive = {}
    years = BlogModel.objects.all().dates(date_field, 'year')[::-1]
    for date_year in years:
        months = BlogModel.objects.filter(published_on__year=date_year.year).dates(date_field, 'month')
        archive[date_year] = months

    archive = sorted(archive.items(), reverse=True)
    ym = request.GET.get("y_m")
    if ym:
        yy = ym.split("-")
        blog_list= BlogModel.objects.filter(published_on__year=yy[0]).filter(published_on__month=yy[1])
        # paginator
        paginator = Paginator(blog_list, 10)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            blog_list = paginator.page(page)
        except PageNotAnInteger:
            blog_list = paginator.page(1)
        except EmptyPage:
            blog_list = paginator.page(paginator.num_pages)


    context = {
        "blog" : blog_list,
        "tags" : tag_list,
        "archive" : archive
    }
    return render(request, "blog.html", context)

# details single blog block ------------------------------------------------------------------------
def blog_detailView(request, id, **kwargs):
    instance = get_object_or_404(BlogModel, id=id)
    blog_content = BlogContentModel.objects.filter(related_to=instance.id)
    share_str = quote_plus(instance.blog_description+" -By "+instance.blog_author.author_name)
    linkedin_msg = quote_plus(instance.blog_title)
    context = {
        "instance" : instance,
        "content" : blog_content,
        "summery_msg" : share_str,
        "title_msg" : linkedin_msg
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




