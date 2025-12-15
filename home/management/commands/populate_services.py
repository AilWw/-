from django.core.management.base import BaseCommand
from home.models import Service

class Command(BaseCommand):
    help = 'Populates the database with initial service data from servisoffice.com'

    def handle(self, *args, **options):
        self.stdout.write("Starting service data population...")

        # Data scraped from the live website (servisoffice.com)
        services_data = [
            # Name, Original Price, Discounted Price, Is On Sale
            ("التسجيل العيني للعقار", 400.00, 199.00, True),
            ("تحويل المؤسسة الى شركة", 800.00, 354.00, True),
            ("التقييم الذاتي قوى للمنشآت", 900.00, 419.00, True),
            ("فك نسبة قوى", 400.00, 289.00, True),
            ("نقل كفالة عامل (منزلي & مهني)", 300.00, 99.00, True),
            ("طباعة الإقامة", 500.00, 275.00, True),
            ("شهادة شطب سجل تجاري", 75.00, 39.00, True),
            ("شطب السجل التجاري", 99.00, 49.00, True),
            ("اصدار سجل تجاري", 300.00, 95.00, True),
            ("اصدار شهادة صحية", 450.00, 99.00, True),
            ("توثيق متجر الكتروني", 100.00, 69.00, True),
            ("تجديد سجل تجاري", 130.00, 70.00, True),
            ("تعديل سجل تجاري", 100.00, 39.00, True),
            ("حجز اسم تجاري", 99.00, 65.00, True),
            ("إضافة موقع في قوقل ماب", 150.00, 150.00, False), # Price not explicitly mentioned, assuming no discount
            ("خدمات أبشر", 150.00, 150.00, False),
            ("خدمات الموارد البشرية", 200.00, 200.00, False),
            ("خدمات منصة قوى", 180.00, 180.00, False),
            ("خدمات حماية الاجور", 250.00, 250.00, False),
            ("خدمات منصة بلدي", 120.00, 120.00, False),
            ("خدمات منصة ناجز", 300.00, 300.00, False),
            ("خدمات التأمينات الإجتماعية", 150.00, 150.00, False),
            ("خدمات وزارة التجارة", 200.00, 200.00, False),
            ("التسجيل بتمارا كتاجر", 100.00, 100.00, False),
        ]

        # Clear existing data to prevent duplicates
        Service.objects.all().delete()
        self.stdout.write(self.style.WARNING("Cleared existing Service data."))

        for name, original_price, discounted_price, is_on_sale in services_data:
            Service.objects.create(
                name=name,
                original_price=original_price,
                discounted_price=discounted_price,
                is_on_sale=is_on_sale,
                description=f"خدمة {name} متوفرة الآن.", # Simple placeholder description
            )
            self.stdout.write(self.style.SUCCESS(f"Successfully added service: {name}"))

        self.stdout.write(self.style.SUCCESS("Service data population complete."))
