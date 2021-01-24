from django import template

register = template.Library()


@register.inclusion_tag('tag/project_cover.html')
def show_project_cover_image(model):
    cover_image = model.album.images.first().image
    print("efsafesfsafesffseaffefef")
    print(cover_image)
    return {'cover_img': cover_image}