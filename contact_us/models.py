from django.db import models

# Create your models here.

class Contact_us(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    problem = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:    # class meta dara ei model tar style change krbo
        verbose_name_plural = "Contact Us"   # admin website a ei model tar nam contact_uss dekhacchilo
                                            # shei nam change korar jonno ei code likha 