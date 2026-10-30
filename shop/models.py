from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    # YANGI QATOR: Mahsulot tavsifi
    description = models.TextField(verbose_name="Mahsulot haqida ma'lumot", blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="Narxi (so'm)")
    image = models.ImageField(upload_to='products/', verbose_name="Rasm", blank=True, null=True)
    is_bestseller = models.BooleanField(default=False, verbose_name="TOP mahsulot")
    is_new = models.BooleanField(default=True, verbose_name="Yangi mahsulot")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/katalog/{self.pk}/"

    class Meta:
        verbose_name = "Mahsulot "
        verbose_name_plural = "Mahsulotlar"