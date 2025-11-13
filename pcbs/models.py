from django.db import models
import uuid
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
    
class Serialnumber(models.Model):
    # Use a 128 bit UUIDField as a strong pk 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pcb = models.ForeignKey(Pcb, on_delete=models.CASCADE, related_name='serial_numbers') #This is the name used to access Serialnumber objects from a PCB object. 

    # Auto-incrementing sn field
    sn_num = models.IntegerField(unique=True, null=True, blank=True)
    date_iss = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.sn_num: # Only generate if not already set
            last_instance = Serialnumber.objects.order_by('-sn_num').first()
            if last_instance and last_instance.ser_num: # Checks if there are existing instances of the sn and if the sn is not none.
                self.ser_num = last_instance.ser_num + 1
            else:
                self.ser_num = 245000 # Start from 1 for the first record. 
        super().save(*args, **kwargs)

            

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


