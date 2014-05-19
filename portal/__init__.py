from models import Tag, TagItem, Layout
from django.contrib.contenttypes.models import ContentType

def aplicar_tags(obj, tags):
    """ 
    override all tags related in object and context by type
    """
    tipo_dinamico = ContentType.objects.get_for_model(obj)
    
    TagItem.objects.filter(
        content_type = tipo_dinamico,
        object_id = obj.id,
        ).delete()

    if tags:
        tags = tags.split(',')
        for tag_nome in tags:
            tag, nova = Tag.objects.get_or_create(nome = tag_nome.strip())
         
            TagItem.objects.get_or_create(
                tag = tag,
                content_type = tipo_dinamico,
                object_id = obj.id)

def tags_para_objeto(obj):
    """ 
    return all tags related by object in param
    """
    tipo_dinamico  = ContentType.objects.get_for_model(obj)
     
    tags = TagItem.objects.filter(
        content_type=tipo_dinamico,
        object_id=obj.id,
        )

    return ', '.join([item.tag.nome for item in tags])

def aplicar_layout(obj, layout, data_expiracao):
    tipo_dinamico = ContentType.objects.get_for_model(obj)
    Layout.objects.filter(content_type = tipo_dinamico, object_id = obj.id).delete()

    if layout:
        Layout.objects.get_or_create(
            local = layout,
            content_type = tipo_dinamico,
            object_id = obj.id,
            data_expiracao = data_expiracao)
    
def layout_para_objeto(obj):
    tipo_dinamico  = ContentType.objects.get_for_model(obj)
    if Layout.objects.filter(content_type=tipo_dinamico, object_id=obj.id).exists():
        layout = Layout.objects.get(content_type=tipo_dinamico, object_id=obj.id)
        return layout.local.id
    return 0
