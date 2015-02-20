import urlparse
from django import template
from django.template.defaulttags import URLNode, url
from django.contrib.sites.models import Site
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def classname(obj):
    classname= obj.__class__.__name__
    return classname

@register.filter
def normdegree(value):
    degree_choices = {
            'MI':'Minor',
            'BA': 'Bachelor of Arts',
            'BS': 'Bachelor of Science',
            'MA': 'Master of Arts',
            'MS': 'Master of Science',
            'MB': 'MBA',
            'PD': 'Ph.D',
            'PR': 'Professional Degree',
            'OT': 'Other'}
    return degree_choices[value]

@register.filter
def tagline(value):
    soup = BeautifulSoup(value)
    text = soup.get_text()
    return text[:140] + '...'

@register.filter
def normcompname(value):
    return value.replace(' ', '%20')

@register.filter()
def rating(value):
    starstring = ""
    for x in range (0, value):
        starstring = starstring + "<span class=fill>&#9733;</span>"
    for x in range(0, 5-value):
        starstring= starstring +"<span>&#9734;</span>"
    return starstring

@register.filter()
def normsalarytype(value):
    pay_choices= {
            'Yearly Salary': '/yr',
            'Monthly Salary': '/mo',
            'Weekly Salary': '/wk',
            'Hourly Salary': '/hr',
            'Total Salary': '/total',
            'Other': '/other'
            }
    return pay_choices[value];

class AbsoluteURLNode(URLNode):
    def render(self, context):
        path = super(AbsoluteURLNode, self).render(context)
        domain = "http://%s" % Site.objects.get_current().domain
        return urlparse.urljoin(domain, path)

def absurl(parser, token, node_cls=AbsoluteURLNode):
    """Just like {% url %} but ads the domain of the current site."""
    node_instance = url(parser, token)
    return node_cls(view_name=node_instance.view_name,
        args=node_instance.args,
        kwargs=node_instance.kwargs,
        asvar=node_instance.asvar)

absurl = register.tag(absurl)


"""
Decorator to facilitate template tag creation
"""
def easy_tag(func):
    """deal with the repetitive parts of parsing template tags"""
    def inner(parser, token):
        #print token
        try:
            return func(*token.split_contents())
        except TypeError:
            raise template.TemplateSyntaxError('Bad arguments for tag "%s"' % token.split_contents()[0])
    inner.__name__ = func.__name__
    inner.__doc__ = inner.__doc__
    return inner



class AppendGetNode(template.Node):
    def __init__(self, dict):
        self.dict_pairs = {}
        for pair in dict.split(','):
            pair = pair.split('=')
            self.dict_pairs[pair[0]] = template.Variable(pair[1])
            
    def render(self, context):
        get = context['request'].GET.copy()

        for key in self.dict_pairs:
            get[key] = self.dict_pairs[key].resolve(context)
        
        path = context['request'].META['PATH_INFO']
        
        #print "&".join(["%s=%s" % (key, value) for (key, value) in get.items() if value])
        
        if len(get):
            path += "?%s" % "&".join(["%s=%s" % (key, value) for (key, value) in get.items() if value])
        
        
        return path

@register.tag()
@easy_tag
def append_to_get(_tag_name, dict):
    return AppendGetNode(dict)
