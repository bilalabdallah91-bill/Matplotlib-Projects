from matplotlib import pyplot as plt

# استخدام النمط الجميل كما في الشاشة
plt.style.use('ggplot')

# الأعمار (محور السينات X)
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# متوسط الرواتب لجميع المطورين (الأعمدة الرمادية)
dev_y = [
    38496,
    42000,
    46752,
    49320,
    53200,
    56000,
    62316,
    64928,
    67317,
    68748,
    73752,
]

# متوسط الرواتب لمطوري بايثون (الأعمدة الزرقاء)
py_dev_y = [
    45372,
    48876,
    53850,
    57287,
    63016,
    65998,
    70003,
    70000,
    71496,
    75370,
    83640,
]

# متوسط الرواتب لمطوري جافاسكريبت (الأعمدة البرتقالية/الصفراء)
js_dev_y = [
    37810,
    43515,
    46823,
    49293,
    53437,
    56373,
    62375,
    66674,
    68745,
    68746,
    74583,
]

# عرض الأعمدة الثلاثة بجانب بعضها البعض بحساب العرض (width) لكي لا تتقاطع
import numpy as np

x_indexes = np.arange(len(ages_x))
width = 0.25  # عرض العمود الواحد

# رسم الأعمدة
plt.bar(
    x_indexes - width, dev_y, width=width, color='#444444', label='All Devs'
)
plt.bar(
    x_indexes, py_dev_y, width=width, color='#008fd5', label='Python'
)
plt.bar(
    x_indexes + width, js_dev_y, width=width, color='#e5ae38', label='JavaScript'
)

# تعديل محور السينات لإظهار الأعمار الصحيحة مكان الأرقام
plt.xticks(ticks=x_indexes, labels=ages_x)

# عناوين الرسم البياني والمحاور
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

# تفعيل المفتاح (Legend) وإظهار الرسم
plt.legend()
plt.tight_layout()
plt.show()