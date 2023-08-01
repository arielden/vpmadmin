from typing import Any, Iterable, Optional
from django.db import models

# Create your models here.
from django.db.models.query import QuerySet
from django.contrib.auth.models import User

# class ReleasedManager(models.Model):
#     def get_queryset(self) -> QuerySet:
#         return super().get_queryset()\
#                     .filter(status=Part.Status.RELEASED)
    
#---------------------------------------------------
# These classes convert the charfield into uppercase.

class PartNumber(models.CharField):
    def get_prep_value(self, value: Any) -> Any:
        return str(value).upper()

class Designation(models.CharField):
    def get_prep_value(self, value: Any) -> Any:
        return str(value).upper()
#---------------------------------------------------

class Level(models.Model):
    name = models.IntegerField(unique=True)

    def __str__(self) -> Any:
        return str(self.name)

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name

class PnType(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self) -> str:
        return self.name

class Part(models.Model):

    # Part properties
    partnumber = PartNumber(max_length=20, unique=True)
    designation = Designation(max_length= 200)
    pntype = models.ForeignKey(PnType,
                                on_delete= models.SET_NULL,
                                null=True,
                                blank=True)
    resp = models.ForeignKey(User,
                             on_delete= models.DO_NOTHING,
                             null=False,
                             default=1)
    # Design status
    status = models.ForeignKey(Status,
                               on_delete= models.SET_NULL,
                               null=True,
                               blank=True)
    

    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

    # Mass and cg properties
    mass = models.DecimalField(max_digits=8, decimal_places=1, default=0) # Mass in (g)
    xcg = models.DecimalField(max_digits=8, decimal_places=1, default=0) # Xcg in (mm)
    ycg = models.DecimalField(max_digits=8, decimal_places=1, default=0) # Ycg in (mm)
    zcg = models.DecimalField(max_digits=8, decimal_places=1, default=0) # Zcg in (mm)
    
    # Hierarchy
    # al definir related_name='children', podemos acceder a todos los hijos de una instancia a través del
    # método .children.all()
    parent = models.ForeignKey('self',
                               on_delete = models.SET_NULL,
                               null=True,
                               blank=True,
                               related_name='children')
    level = models.ForeignKey(Level,
                              on_delete = models.DO_NOTHING,
                              # Si hay problemas al migrar, comentar la siguiente línea
                            #   default=Level.objects.get(id=1)
                              )
    file_path = models.FileField(upload_to='catia_data/', null=True, blank=True)
    
    # objects = models.Manager() # Default
    # released = ReleasedManager() # Custom manager for released parts!

    class Meta:
        ordering = ['partnumber']
        indexes = [
            models.Index(fields=['partnumber']),
        ]

    def __str__(self) -> str:
        return self.partnumber
    
    #Next lines, overwrites save method for Part objects
    def save(self, *args, **kwargs):
        if self.parent:
            self.level = Level.objects.get(name=self.parent.level.id + 1)
        else:
            self.level = Level.objects.get(id=1)
        super().save(*args, **kwargs)