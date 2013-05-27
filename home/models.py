from django.db import models

class home(models.Model):
    message = models.CharField(max_length = 80)
    
def _unicode_ (self):
    return self.message
    
 
