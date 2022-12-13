from django import template

register = template.Library()

@register.inclusion_tag('my_tag/headers.html')
def banner(menu_name):
    img_list = [
        "/static/my/img/nav/01.jpg",
        "/static/my/img/nav/02.jpg",
        "/static/my/img/nav/03.jpg",
    ]
    return {"img_list":img_list}