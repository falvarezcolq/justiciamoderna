"""User profile model."""
# Django
from django.db import models

# Models
from justiciamoderna.users.models import User



class profile(models.Model):
    GENDER_CHOICES = [
        ("F", "Female"),
        ("M", "Male"),
        ("NB", "No Binary"),
        ("PND", "I prefer not to say"),
    ]
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="ghuser")
    birth_date = models.DateTimeField(verbose_name="Fecha de Nacimiento")
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES, verbose_name="Genero")
    live_in = models.TextField("Live in", blank=True, null=True)
    phone_number = models.TextField("Número de teléfono", blank=True, null=True, default="")
    web_site = models.TextField("Web Site", blank=True, null=True, default="")
    about_me = models.TextField("About Me", blank=True, null=True, default="")
    country = models.CharField("Pais", max_length=255, blank=True, null=True, default="")
    language = models.CharField("Idioma", max_length=255, blank=True, null=True, default="en")
    head_line = models.CharField("Head line", max_length=255, blank=True, null=True, default="")

    birth_date_state = models.BooleanField("Birth date is public.", default=True)
    gender_state = models.BooleanField("Gender State is public.", default=True)
    live_in_state = models.BooleanField("Live in  is public.", default=True)
    phone_number_state = models.BooleanField("Phone is public.", default=True)
    web_site_state = models.BooleanField("Web Site is public.", default=True)
    about_me_state = models.BooleanField("About Me is public.", default=True)
    country_state = models.BooleanField("Country is public.", default=True)
    language_state = models.BooleanField("Language is public.", default=True)
    head_line_state = models.BooleanField("Headline is public.", default=True)
    email_state = models.BooleanField("Email is public.", default=True)

    # add boolean
    account_state = models.BooleanField("Account visible.", default=True)
    account_public = models.BooleanField("Cuenta publica.", default=True)
    # add boolean for terms
    term_of_services_accepted = models.BooleanField("Term of service.", default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(null=True, blank=True)

    change_password = models.BooleanField("Need to change Password.", default=False)
    old_password = models.CharField("Idioma", max_length=255, blank=True, null=True, default="")

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return "%s %s" % (self.user, self.phone_number)
