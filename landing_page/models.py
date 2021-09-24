from django.db import models

class Plan(models.Model):

    name = models.CharField(max_length=255)
    price = models.IntegerField(null = True, blank=True)
    price_anual = models.IntegerField(null = True, blank = True)
    highlight = models.BooleanField()
    max_peaple = models.IntegerField(null = True, blank=True)
    contact = models.BooleanField()
    discount = models.IntegerField()
    founder = models.BooleanField()
    order = models.IntegerField()

    @property
    def final_price(self):
        if(self.discount != 0):
            return int(round((self.price * (100 - self.discount)) / 100 ,2))
        else:
            return self.price

    @property
    def final_anual_price(self):
        if(self.discount != 0):
            return int(round((self.price_anual * (100 - self.discount)) / 100 ,2))
        else:
            return self.price


    def __str__(self):
        return self.name

class PlanInclude(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='features')
    enable = models.BooleanField()
    feature = models.ForeignKey('landing_page.PlanFeature', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.enable) + " " + self.feature.text

class PlanFeature(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    rol = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField()
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Feature(models.Model):
    title=models.CharField(max_length=400)
    description=models.TextField()
    image = models.ImageField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Faq(models.Model):
    title = models.CharField(max_length = 300)
    answer = models.TextField()
    time_stamp = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Emails(models.Model):

    SOCIAL_MEDIA_CHOICES = [
        ('IG', 'Instagram'),
        ('YT', 'Youtube'), 
        ('TW', 'Twitter'),
        ('Tk', 'TIK TOK'),
        ('FC', 'Facebook'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    rssc = models.CharField(max_length=200)
    social_media = models.CharField(choices=SOCIAL_MEDIA_CHOICES, max_length=50)
    confirm_privacy = models.BooleanField()
    has_used_other_tool = models.CharField(null=True, blank=True, max_length=6)

    def __str__(self):
        return self.email

class Market(models.Model):

    nombre = models.CharField(max_length=200, null=False)
    apellidos = models.CharField(max_length=200, null=False)
    horario = models.CharField(max_length=200, null=False)
    edad = models.IntegerField(null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + self.email + " viene a las " + self.horario