from .forms import ContactModelFormCreate
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from contact.models import Contacto
from django.urls import reverse_lazy
from django.contrib import messages

class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactModelFormCreate
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        comentario = form.cleaned_data['comentario']

        message_content = f'{nombre} con email {email} ha escrito lo siguiente: {comentario}'

        Contacto.objects.create(
            nombre=nombre,
            email=email,
            comentario=comentario
        )

        send_mail(
            "Formulario de contacto de mi Web",
            message_content,
            "w.infanzon.98@gmail.com",
            ["w.infanzon.98@gmail.com"],
            fail_silently=False,
        )
        messages.add_message(self.request, messages.SUCCESS, "Mensaje enviado correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response({'formulario': form})
