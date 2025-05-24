from django.db import models

class Toys (models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.image} - {self.name} - {self.price}'


class Figurines (models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.image} - {self.name} - {self.price}'

class Mugs (models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.image} - {self.name} - {self.price}'

class Soda (models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.image} - {self.name} - {self.price}'

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    product = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer_name} - {self.email} - {self.product} - {self.price} - {self.created_at}'

class StudentProfile(models.Model):
    full_name = models.CharField(max_length=100)
    photo = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.CharField(max_length=100000)

    def __str__(self):
        return f'{self.full_name} - {self.photo} - {self.email} - {self.phone} - {self.resume}'

class EducationalProgram(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    courses = models.TextField(help_text="Что я буду изучать")
    skills = models.TextField(help_text="Чему я научусь")
    advantages = models.TextField()
    prospects = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.description} - {self.link} - {self.courses} - {self.skills} - {self.advantages} - {self.prospects}'

class ProgramManagement(models.Model):
    ROLE_CHOICES = [
        ('AR', 'Академический руководитель'),
        ('M', 'Менеджер'),
    ]
    program = models.ForeignKey(EducationalProgram, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    photo = models.URLField()
    email = models.EmailField()
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.get_role_display()}: {self.full_name} - {self.photo} - {self.email} - {self.role}"

class Classmate(models.Model):
    program = models.ForeignKey(EducationalProgram, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    photo = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.full_name} - {self.photo} - {self.program} - {self.email} - {self.phone}'

