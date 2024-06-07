from django.db import models

class Ucitel(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    heslo = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Učiteľ"
        verbose_name_plural = "Učitelia"
        ordering = ["priezvisko"]

    def __str__(self):
        return f"{self.meno} {self.priezvisko}"

    
class Student(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    heslo = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"
        ordering = ["priezvisko"]
    
    def __str__(self):
        return f"{self.meno} {self.priezvisko}"


class Odbor(models.Model):
    nazov = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Odbor"
        verbose_name_plural = "Odbory"
        ordering = ["nazov"]

    def __str__(self):
        return f"{self.nazov}"


class Dostupnost(models.Model):
    nazov = models.CharField(max_length=22)

    class Meta:
        verbose_name = "Dostupnosť"
        verbose_name_plural = "Dostupnosti"

    def __str__(self):
        return f"{self.nazov}"


class Tema(models.Model):
    nazov = models.CharField(max_length=50)
    popis = models.TextField()
    konzultant = models.ForeignKey(Ucitel, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    odbor = models.ForeignKey(Odbor, on_delete=models.CASCADE)
    dostupnost = models.ForeignKey(Dostupnost, on_delete=models.CASCADE)
    koznultacie = models.IntegerField()

    class Meta:
        verbose_name = "Téma"
        verbose_name_plural = "Témy"
        ordering = ["nazov"]

    def __str__(self):
        return f"{self.nazov}"