from django.db import models

class Timer(models.Model):
    time = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.time:.2f} seconds - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

