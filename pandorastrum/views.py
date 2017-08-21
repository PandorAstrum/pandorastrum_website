import datetime
from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import TemplateView
from pandorastrum.models import GamesModel, AboutModel, AboutTeamImage, ThanksName, BlogModel, BlogContentModel
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from urllib.parse import quote_plus


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
    blog_list = BlogModel.objects.all().order_by("-created")
    paginator = Paginator(blog_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    normal_view = True
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blog = paginator.page(paginator.num_pages)
    tag_list = Tag.objects.all()
    blog_tag = BlogModel.objects.filter(tags__slug=kwargs.get("slug"))

    year_list = []
    month_list = []
    year_month = []
    for b in blog_list:
        if b.published_on.year not in year_list:
            year_list.append(b.published_on.year)
    for y in year_list:
        for b in blog_list:
            if b.published_on.month not in month_list and b.published_on.year is y:
                month_list.append(b.published_on.month)
        year_month.append(month_list)


    context = {
        "blog" : blog,
        "tags" : tag_list,
        "blog_tag" : blog_tag,
        "normal_view" : normal_view,
        "year_list" : year_list
    }
    return render(request, "blog.html", context)

# class based blog block -------------------------------------------------------------------
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context["class_tagged"] = True
        return context

class blog_tagView(TagMixin, ListView):
    model = BlogModel
    template_name = "blog.html"
    paginate_by = 10
    context_object_name = "blog"

    def get_queryset(self):
        return BlogModel.objects.filter(tags__slug=self.kwargs.get("slug"))

    # def get_context_data(self, **kwargs):
    #     context = super(blog_tagView, self).get_context_data(**kwargs)
    #     p = Paginator(BlogModel.objects.all(), self.paginate_by)
    #     context['blog'] =  p.page(context['page_obj'].number)
    #     first = BlogContentModel.objects.filter(related_to=self.kwargs.get("id")).values_list('image', flat=True)
    #     # context['first_image'] = accordion2_content.objects..values_list('image', flat=True)[0]
    #     context['blog_content'] = BlogContentModel.objects.filter(related_to=self.kwargs.get("id")).values_list('image', flat=True)
    #     context['tags'] = Tag.objects.all()
    #     context['normal_view'] = False
    #     return context

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




