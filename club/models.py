from django.db import models

class Club(models.Model):
    club_name = models.CharField(max_length=100, blank=True, default='')
    club_description = models.TextField()
    club_pic = models.ImageField(width_field= 300, height_field= 300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    #owner = models.ForeignKey(
        #'auth.User', related_name='name', on_delete=models.CASCADE)

    class Meta:
        ordering = ('date_created', )

    # def save(self, *args, **kwargs):
    #     super(Club, self).save(*args, **kwargs)
        

    