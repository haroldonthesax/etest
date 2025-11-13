from django.db import models
import datetime

# Create your models here.
class Pcb(models.Model):
    # Represents instances of PCBs
    part_num = models.CharField(max_length=100, null=True, blank=True)
    rev = models.CharField(max_length=100, null=True, blank=True)
    serial_num =models.CharField(max_length=100, null=True, blank=True) 
    mac = models.CharField(max_length=100, null=True, blank=True)
    ip = models.CharField(max_length=100, null=True, blank=True)
    firmware = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f'{self.part_num} {self.mac}'

class TestSequence(models.Model):
    #Represents instances of test sequences.
    pcb = models.ForeignKey(Pcb, on_delete=models.CASCADE, related_name='test_sequences') 
    name = models.CharField(max_length=120, blank=True)
    date_created = models.DateField(
        null=True, 
        blank=True, 
        default=datetime.date.today, 
        verbose_name="Date Test Sequence Created:", 
        help_text="The date this sequence was created." )
    date_edited = models.DateField(
        null=True, 
        blank=True, 
        default=datetime.date.today, 
        verbose_name="Date Test Sequence Edited:", 
        help_text="The date this sequence was last edited." )

    def __str__(self):
        return f'{self.name}'


