from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import document, doc, key

# Register your models here.
# class DocumentPostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)  # Apply Summernote to specific fields

admin.site.register(document)

# class DocPostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)  # Apply Summernote to specific fields
#e.g admin.site.register(doc, DocPostAdmin)

admin.site.register(doc)

admin.site.register(key)