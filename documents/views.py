from django.shortcuts import get_object_or_404, render, redirect
from .models import document, doc
from .forms import DocumentForm, DocForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#document: categories of document
#doc: documents in each category

def log_in(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user:
         login(request, user=user)
         return redirect('home')
      else:
         messages.error(request, 'Username or Password is Incorrect❌')
   return render(request=request, template_name='auth/login.html')

def log_out(request):
   logout(request)
   return redirect('login')

@login_required
#Home page displaying all document categories
def home_page(request):
  if request.method == 'POST':
     form = DocumentForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('home')

  form = DocumentForm()
  documents = document.objects.all()
  return render(request=request, template_name='pages/home.html', context={'documents': documents, 'form': form, 'request': request})

@login_required
#Document page displaying all document in selected category
def documents_page(request, pk):
  Document = get_object_or_404(document, pk=pk)

  #Post request to add new document(doc)
  if request.method == 'POST':
    Doc = doc(document=Document, title=request.POST['title'], content=request.POST['content'], code=request.POST['code'], image=request.POST['image'])
    Doc.save()
    return redirect('docs', pk=pk)
  
  Docs = Document.docs.all()
  form = DocForm()
  return render(request=request, template_name='pages/docs.html', context={'Document': Document, 'Docs': Docs, 'form': form})

@login_required
#Document page displaying content of selected document
def document_page(request, pk, pk2):
  Doc = get_object_or_404(doc, pk=pk)
  Document = get_object_or_404(document, pk=pk2)
  return render(request=request, template_name='pages/document.html', context={'Document': Document, 'Doc': Doc})

#Edit selected document
class DocumentEditView(UpdateView):
    model = doc
    fields = ['title', 'content', 'code', 'image']
    template_name = 'pages/editpost.html'

    def get_success_url(self):
        return reverse_lazy('document', kwargs={'pk': self.object.pk, 'pk2': self.object.document.pk})

#Delete selected document
class DocumentDeleteView(DeleteView):
    model = doc
    template_name = 'pages/deletepost.html'
    success_url = reverse_lazy('home')

@login_required
def search_result(request):
  search_r_lst = []
  Documents = document.objects.all()
  msgs = ['Search Not Found🔎']
  search_input = ''
  if request.method == 'POST':
    search_input = request.POST['search_input']
    
    if search_input:
      for  Document in Documents:
        print(Document.title)
        for Doc in Document.docs.all():
          print(Doc.title)
          if re.search(search_input, Doc.title, re.IGNORECASE):
            search_r_lst.append(Doc)
          else:
            pass
    return render(request=request, template_name='pages/search_result.html', context={'search_r_lst': search_r_lst, 'msgs': msgs, 'search_input': search_input})






# def document_edit(request, pk):
#   return render(request=request, template_name='pages/editpost.html')

# def document_delete(request, pk):
#   return render(request=request, template_name='pages/deletepost.html')