import re

def check_password_strength(password):
    # مبرمج بواسطة Rateel - أداة فحص قوة كلمة المرور
    # تم رفع هذا الكود كبداية لمشروع الأمن السيبراني
    
    strength = 0
    remarks = ''
    
    # التحقق من طول كلمة المرور (المعيار الأمني الجديد 12 حرف)
    if len(password) >= 12:
        strength += 1
    
    # التحقق من وجود حروف صغيرة
    if re.search("[a-z]", password):
        strength += 1
        
    # التحقق من وجود حروف كبيرة
    if re.search("[A-Z]", password):
        strength += 1
        
    # التحقق من وجود أرقام
    if re.search("[0-9]", password):
        strength += 1
        
    # التحقق من وجود رموز خاصة
    if re.search("[@#$%^&+=!]", password):
        strength += 1

    # تحديد النتيجة النهائية
    if strength <= 2:
        remarks = "ضعيفة جداً - (خطر الاختراق عالي)"
    elif strength == 3:
        remarks = "متوسطة - (يفضل إضافة رموز أو أرقام)"
    elif strength == 4:
        remarks = "قوية - (آمنة)"
    elif strength == 5:
        remarks = "ممتازة - (معايير أمنية عالية)"
    
    return remarks

# تشغيل الأداة
print("--- أداة Rateel لفحص أمن كلمات المرور ---")
user_input = input("أدخلي كلمة مرور للاختبار: ")
result = check_password_strength(user_input)
print(f"النتيجة: {result}")
