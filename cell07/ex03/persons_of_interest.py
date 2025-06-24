#!/usr/bin/env python3

def famous_births(dic_l):
    # แปลง dict เป็น list ของ tuples (key, info)
    items = list(dic_l.items())
    # เรียงตามปีเกิด (cast เป็น int เพื่อเรียงตัวเลข)
    items_sorted = sorted(items, key=lambda x: int(x[1]['date_of_birth']))
    for key, info in items_sorted:
        print(f"{info['name']} is a great scientist born in {info['date_of_birth']}.")


women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
