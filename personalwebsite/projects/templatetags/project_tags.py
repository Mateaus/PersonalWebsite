from django import template

register = template.Library()


@register.inclusion_tag('tag/project_cover.html')
def show_project_cover_image(model):
    cover_image = model.album
    if cover_image:
        cover_image = model.album.images.first().image
    return {'cover_img': cover_image}