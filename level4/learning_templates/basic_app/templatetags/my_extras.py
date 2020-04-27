from django import template

register = template.Library()

# Custom Filter for Templates
@register.filter(name='cut')
def cut(value,arg):
    """
    This cut out all values of "arg" from string!
    """
    return value.replace(arg,'')


#register.filter('cut',cut)
# Decorators method 2 to register -> @register.filter(name='cut')
