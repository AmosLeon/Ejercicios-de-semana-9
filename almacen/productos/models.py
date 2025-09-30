from django.db import models

# Create your models here.

# Importar la clase model de models
class Producto(models.Model): # Aplicando herencia
    
    # Crear los atributos de la clase Producto
    nombre = models.CharField(max_length=50 ) # Nombre varchar(50), not null
    descripcion = models.TextField(null=True, max_length=150) # Descripcion varchar(150)
    precio = models.DecimalField(max_digits=12, decimal_places=2) # Precio decimal(12,2), not null
    stock = models.IntegerField(default=0) # Stock int, not null, default 0
    
    
    
    # Crear un metodo
    def __str__(self): # Polimorfismo
        return f"{self.nombre} - {self.stock} unidades"