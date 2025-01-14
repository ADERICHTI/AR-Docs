from django.test import TestCase
import re
from .models import document, doc

# Create your tests here.
search_r_lst = []
Documents = document.objects.all()

search_input = 'python'

if search_input:
  for  Document in Documents:
    for Doc in Document.docs.all():
      if re.search(search_input, Doc.title):
        search_r_lst.append(Doc)
      else:
        pass
print(search_r_lst)