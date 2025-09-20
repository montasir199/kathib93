# شركة كثيب للاستثمار - نظام إدارة العقارات

نظام شامل لإدارة العقارات والعقود والمدفوعات لشركة كثيب للاستثمار.

## 🚀 النشر على Railway

### المتطلبات الأساسية:
- حساب Railway
- GitHub repository

### خطوات النشر:

1. **أضف المشروع إلى GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/kthaib-investment.git
git push -u origin main
```

2. **انشر على Railway:**
   - اذهب إلى [Railway.app](https://railway.app)
   - اضغط "New Project"
   - اختر "Deploy from GitHub"
   - اختر repository المشروع
   - اضغط "Deploy"

3. **إعداد قاعدة البيانات:**
   - Railway سيقوم تلقائياً بإنشاء PostgreSQL database
   - سيتم إضافة `DATABASE_URL` تلقائياً كمتغير بيئة

4. **إعداد متغيرات البيئة:**
   في لوحة تحكم Railway، أضف هذه المتغيرات:

```bash
SECRET_KEY=your-super-secret-key-here
WTF_CSRF_SECRET_KEY=your-csrf-secret-key-here
FLASK_ENV=production
DEBUG=False
```

## 📋 الميزات

- ✅ إدارة الملاك والمستأجرين
- ✅ إدارة المشاريع والوحدات
- ✅ تتبع المدفوعات والعمولات
- ✅ تقارير شاملة (PDF, Excel, CSV)
- ✅ نظام مصادقة آمن
- ✅ رفع وإدارة العقود
- ✅ واجهة عربية متجاوبة
- ✅ دعم التقويم الهجري
- ✅ متوافق مع الأنظمة السعودية

## 🛡️ الأمان

- تشفير كلمات المرور
- حماية CSRF
- تقييد معدل الطلبات
- رؤوس أمان متقدمة
- تشفير البيانات الحساسة
- تسجيل العمليات الأمنية

## 🗄️ قاعدة البيانات

- دعم PostgreSQL (Railway)
- دعم SQLite (التطوير المحلي)
- نسخ احتياطي تلقائي
- فهرسة للأداء الأمثل

## 📱 الاستخدام

1. سجل دخولك كمدير أو موظف
2. أضف الملاك والمستأجرين
3. أنشئ المشاريع والوحدات
4. سجل المدفوعات وتتبع العمولات
5. أنشئ التقارير والإحصائيات

## 🔧 التطوير المحلي

```bash
# استنساخ المشروع
git clone https://github.com/yourusername/kthaib-investment.git
cd kthaib-investment

# إنشاء البيئة الافتراضية
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# تثبيت المتطلبات
pip install -r requirements.txt

# إعداد متغيرات البيئة
cp .env.example .env
# عدل .env بالقيم المناسبة

# تشغيل التطبيق
python app.py
```

## 📞 الدعم

للاستفسارات والدعم الفني، يرجى التواصل مع قسم تقنية المعلومات في شركة كثيب للاستثمار.

## 📄 الترخيص

جميع الحقوق محفوظة © شركة كثيب للاستثمار