from django import template

register = template.Library()


@register.inclusion_tag('tag/tag_result.html')
def show_tags(model):
    tag_list = model.tags.all()
    return {'tags': tag_list}

@register.inclusion_tag('tag/tag_css.html')
def default_tag_css():
    # Returns the html containing default css for tags
    return