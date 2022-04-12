from django import template

register = template.Library()

@register.filter(name='testcut')
def testcut(value,arg):
    return value.replace(arg,'')

# register.filter('cut',cut)
