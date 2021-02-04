from django import template

register = template.Library()


@register.inclusion_tag('tag/project_cover.html')
def show_project_cover_image(model):
    try:
        cover_image = model.album.images.first().image
    except AttributeError:
        cover_image = None
    return {'cover_img': cover_image}


@register.inclusion_tag('tag/project_images.html')
def show_project_images(model):
    if model.album:
        proj_images = []
        default_not_added = True
        for image in model.album.images.all():
            img_src = image.image.url
            if image.default and default_not_added:
                proj_images.insert(0, img_src)
                default_not_added = False
            else:
                proj_images.append(img_src)
        return {'proj_images': proj_images}
    return