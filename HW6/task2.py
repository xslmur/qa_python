
# QA Automation Python 14.03.2023
# Karpynska Karolina
# ДЗ 6. АРІ на базі гугл таблиці
# 1. створити АРІ на базі гугл таблиці, містить поля
#   "назва товару",
#   "опис товару",
#   "ціна" (інтова чи флоат),
#   "залишок" (інтовий чи флоат),
#   "містить глютен" (булеве тру чи фолс (виставляєте прапорцем).
#   заповнити мінімум 10 позицій. дані мають бути отримати по зовнішньому ключу "goods" (not "data")
#
# 2. за допомогою requests завантажити створені дані. порахувати вартість всіх товарів та товарів без глютена.

#table: https://docs.google.com/spreadsheets/d/1-_N1TLlb4IeVUGg_UcopTQrmKm7pHEzNz-f5v75qpWg/edit#gid=0
#api url: https://script.google.com/macros/s/AKfycbwSiLV7zDQ-OfgH-LcyHSlh8B8yj9CWwPSpU71tbG2-7Ut-C40qMKdHpSAP-pwdSgcr/exec

import requests

api_url =  'https://script.google.com/macros/s/AKfycbwSiLV7zDQ-OfgH-LcyHSlh8B8yj9CWwPSpU71tbG2-7Ut-C40qMKdHpSAP-pwdSgcr/exec'
goods = requests.get(api_url).json()['goods']
#print(goods)

goods_cost = 0
goods_gluten_free_cost = 0

for item in goods:
    item_cost = item.get('price', 0) * item.get('stock', 0)
    goods_cost += item_cost
    if item.get('gluten') == False:
        goods_gluten_free_cost += item_cost

print('total cost:', goods_cost)
print('gluten-free cost:', goods_gluten_free_cost)
