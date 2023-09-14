from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from .models import Projet
from django.core.paginator import Paginator



class HomeView(View):
    def get(self,request):
        return render(request , 'home.html')

class AboutView(View):
    def get(self,request):
        return render(request , 'about.html')


class ErpView(View):
    def get(self,request):
        return render(request , 'erp.html')




class ListeProjetsView(View):
    template_name = 'project.html'
    items_per_page = 10

    def get(self, request):
        projects = Projet.objects.all()  # Récupérez la liste des projets depuis votre modèle

        paginator = Paginator(projects, self.items_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        context = {'page': page}
        # context['projets'] = Projet.objects.all()
        return render(request, self.template_name, context)



class ProjetDetailView(DetailView):
    model = Projet
    template_name = 'detail.html'
    context_object_name = 'project'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
from django.views.generic.edit import FormView
from .forms import ContactForm  # Assurez-vous de créer un formulaire de contact

class ContactView(FormView):
    template_name = 'contact.html'  # Le modèle de la page de contact
    form_class = ContactForm  # Le formulaire de contact
    success_url = '/Contact'  # L'URL de redirection après une soumission réussie

    def form_valid(self, form):
        # Traitement des données du formulaire ici
        # Par exemple, envoyez un e-mail ou enregistrez les données dans la base de données
        # Vous pouvez accéder aux données du formulaire à l'aide de form.cleaned_data

        # Exemple d'envoi d'e-mail
        from django.core.mail import send_mail

        subject = 'Nouveau message de contact'
        message = f"Nom: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['emailid']}\nTéléphone: {form.cleaned_data['phone']}\nMessage:\n{form.cleaned_data['msg']}"
        from_email = 'mohammedsbtf11@gmail.com'
        recipient_list = ['mohammedsbtf11@gmail.com']

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return super().form_valid(form)
