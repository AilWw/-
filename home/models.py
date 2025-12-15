from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم الخدمة")
    description = models.TextField(verbose_name="وصف الخدمة", blank=True, null=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر الأصلي")
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر بعد الخصم")
    is_on_sale = models.BooleanField(default=False, verbose_name="هل يوجد تخفيض؟")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "خدمة"
        verbose_name_plural = "خدمات"
