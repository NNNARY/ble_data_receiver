from django.db import models

# Create your models here.
class RSSIData(models.Model):
    rssi_value = models.IntegerField()
    dist_data = models.FloatField(blank=True, null=True)  # 거리 값을 저장할 필드
    
    def save(self, *args, **kwargs):
        alpha = -60
        n = 3
        
        self.dist_data = 10**((alpha-self.rssi_value)/(10*n))
        super(RSSIData, self).save(*args, **kwargs)