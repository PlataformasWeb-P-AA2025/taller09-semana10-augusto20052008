from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    username_twitter = models.CharField(max_length=15)

    def __str__(self):
        return "%s - %s - Twitter: %s" % (self.nombre, 
                self.siglas, 
                self.username_twitter)

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=50)
    numero_camiseta = models.IntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s - Camiseta: %d - Sueldo: $%s - Equipo: %s" % (
                self.nombre,
                self.posicion_campo, 
                self.numero_camiseta, 
                self.sueldo, 
                self.equipo.nombre
        )

class Campeonato(models.Model):
    nombre = models.CharField(max_length=100)
    auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return "%s - Auspiciante: %s" % (self.nombre, 
                self.auspiciante)

class CampeonatoEquipos(models.Model):
    anio = models.PositiveIntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('anio', 'equipo', 'campeonato')

    def __str__(self):
        return "Año: %d - Equipo: %s - Campeonato: %s" % (self.anio, 
                self.equipo.nombre, 
                self.campeonato.nombre)


""" Crear las siguientes entidades:
Equipo de Futbol: nombre, siglas, username twitter

Jugador: nombre, posición campo, número camiseta, sueldo, equipo de fútbol

Campeonato: nombre de campeonato, nombre de auspiciante

Campeonato Equipos: año, equipo de fútbol, campeonato """