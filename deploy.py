#!/usr/bin/env python3
"""
سكريبت نشر لـ Railway
يستخدم للتحقق من إعدادات النشر وضمان التوافق
"""

import os
import sys
from app import app, db

def check_environment():
    """فحص متغيرات البيئة المطلوبة"""
    required_vars = ['SECRET_KEY', 'WTF_CSRF_SECRET_KEY']
    missing_vars = []

    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)

    if missing_vars:
        print(f"⚠️  متغيرات البيئة المفقودة: {', '.join(missing_vars)}")
        return False

    print("✅ جميع متغيرات البيئة متوفرة")
    return True

def check_database():
    """فحص الاتصال بقاعدة البيانات"""
    try:
        with app.app_context():
            db.engine.execute('SELECT 1')
        print("✅ الاتصال بقاعدة البيانات ناجح")
        return True
    except Exception as e:
        print(f"❌ فشل الاتصال بقاعدة البيانات: {e}")
        return False

def check_file_permissions():
    """فحص صلاحيات الملفات"""
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        try:
            os.makedirs(upload_folder)
            print(f"✅ تم إنشاء مجلد الرفع: {upload_folder}")
        except Exception as e:
            print(f"❌ فشل إنشاء مجلد الرفع: {e}")
            return False
    else:
        print(f"✅ مجلد الرفع موجود: {upload_folder}")

    return True

def main():
    """الدالة الرئيسية للنشر"""
    print("🚀 بدء فحص النشر لـ Railway...")
    print("=" * 50)

    checks = [
        ("متغيرات البيئة", check_environment),
        ("قاعدة البيانات", check_database),
        ("صلاحيات الملفات", check_file_permissions),
    ]

    all_passed = True
    for check_name, check_func in checks:
        print(f"\n🔍 فحص: {check_name}")
        if not check_func():
            all_passed = False

    print("\n" + "=" * 50)
    if all_passed:
        print("✅ جميع الفحوصات نجحت! التطبيق جاهز للنشر")
        return 0
    else:
        print("❌ فشل بعض الفحوصات. يرجى إصلاح المشاكل قبل النشر")
        return 1

if __name__ == '__main__':
    sys.exit(main())