from django.shortcuts import render
from django.http import JsonResponse
from .models import Service # Import the new model

# Helper functions for static content (Testimonials and FAQs)
def get_testimonials():
    """الحصول على شهادات العملاء"""
    return [
        {
            'name': 'علي القفيلي ',
            'text': 'هذا المكتب من المكاتب القليلة الي فعلا يعرف شغله قدمت عندهم على تمويل العمل الحر وتم الانجاز عن جد ولا اروع',
            'rating': 5
        },
        {
            'name': 'مرام  اليامي',
            'text': 'تعامل راقي وسريع موفقين واللى ما عارف وين يسجل يسجل عندهم قدمت معاهم انا وزميتلي وانشاء الله القبول شكرا لكم',
            'rating': 5
        },
       # {
         #   'name': 'حنين',
          #  'text': 'أفضل مكتب خدمات الموظف بالمكتب فاهم سريع ومتعاون ومعظم اللى روحو لا يشكو من شي',
            #'rating': 5
       # },
       # {
        #    'name': 'عبد العزيز',
           # 'text': 'قمت بطلب خدمة اصدار رخصة بلدي والله ما كملت 3 ساعات كان كل حاجة تمت شكرا لكم وتعامل مستمر',
          #  'rating': 5
       # },
    ]

def get_faqs():
    """الحصول على الأسئلة الشائعة"""
    return [
        {
            'question': 'ما اسعار الخدمات المقدمة ؟',
            'answer': 'تختلف الأسعار حسب نوع الخدمة والمتطلبات. يمكنك التواصل معنا للحصول على أسعار دقيقة.'
        },
        {
            'question': 'هل يمكن استرداد سعر الخدمة ؟',
            'answer': 'نعم، يمكن استرجاع المبلغ في حالة عدم إنجاز الخدمة بنجاح خلال المدة المحددة.'
        },
        {
            'question': 'هل الخدمات المقدمة للشركات فقط؟',
            'answer': 'لا، نقدم خدماتنا للأفراد والشركات والمؤسسات على حد سواء.'
        },
        {
            'question': 'كيف اطلب خدمة ؟',
            'answer': 'يمكنك طلب الخدمة عبر الواتس أب أو من خلال الموقع مباشرة.'
        },
        {
            'question': 'هل يمكن إصدار فاتورة ضريبية للخدمة؟',
            'answer': 'نعم، نصدر فواتير ضريبية لجميع الخدمات المقدمة.'
        },
    ]

def index(request):
    """الصفحة الرئيسية"""
    # Use the Service model for featured services
    featured_services = Service.objects.filter(is_on_sale=True)[:8] # Limit to 8 for the home page
    context = {
        'page_title': 'مكتب خدمات',
        'services': featured_services,
        'testimonials': get_testimonials(),
        'faqs': get_faqs(),
    }
    return render(request, 'home/index.html', context)

def services(request):
    """صفحة الخدمات"""
    # Use the Service model for all services
    all_services = Service.objects.all().order_by('name')
    context = {
        'page_title': 'الخدمات',
        'services': all_services,
    }
    return render(request, 'home/services.html', context)

def about(request):
    """صفحة من نحن"""
    context = {
        'page_title': 'من نحن',
    }
    return render(request, 'home/about.html', context)

def contact(request):
    """صفحة التواصل"""
    context = {
        'page_title': 'التواصل',
    }
    return render(request, 'home/contact.html', context)
