from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Description(models.Model):  
    DEPT_CHOICES=(
        ('Análisis de Riesgos', 'Análisis de Riesgos'), 
        ('Asistencia Humanitaria', 'Asistencia Humanitaria'), 
        ('Cordinación General de Asesoría Jurídica', 'Cordinación General de Asesoría Jurídica'), 
        ('Estratégia Internacionales para la Reducción de Riesgos', 'Estratégia Internacionales para la Reducción de Riesgos' ), 
        ('Fortalecimiento y Desarrollo de capacidades en Gestión de Riesgos', 'Fortalecimiento y Desarrollo de capacidades en Gestión de Riesgos' ), 
        ('Gestión de la Información', 'Gestión de la Información'), 
        ('Gestión de Riesgos', 'Gestión de Riesgos'), 
        ('Monitoreo de Eventos Adversos', 'Monitoreo de Eventos Adversos'), 
        ('Operaciones', 'Operaciones'), 
        ('Política y Estandares de Gestión de Riesgos', 'Política y Estandares de Gestión de Riesgos'), 
    )

    SEQ_CHOICES=(
        ('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'),
        ('106', '106'), ('107', '107'), ('108', '108'), ('109', '109'), ('110', '110'),
    )

    sequence = models.CharField(_('sequence'), max_length=3, unique=True, choices=SEQ_CHOICES) 
    department = models.CharField(_('department'), max_length=100, choices=DEPT_CHOICES)
    index_name = models.CharField(_('index name'), max_length=200)
    description = models.TextField(_('description'),) 

    def __str__(self):
        return self.department 
        