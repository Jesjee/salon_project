from django.db import models

class Paket(models.Model):
    nama_paket = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    durasi_menit = models.IntegerField()

    def __str__(self):
        return self.nama_paket


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    nama_pelanggan = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=15)
    paket = models.ForeignKey(Paket, on_delete=models.CASCADE)
    tanggal_booking = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.nama_pelanggan} - {self.paket.nama_paket}"