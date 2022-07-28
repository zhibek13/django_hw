from django.db import shop, db
from shop.models import Item, Purchase
from django.utils import timezone

if __name__ == '__main__':
    with shop.shop_context():
        db.create_all()
        i = Item(name='Pen', price=100)
        i2 = Item(name='Book', price=50)
        i3 = Item(name='Notebook', price=40)
        i4 = Item(name='Bottle', price=300)
        i5 = Item(name='Mirror', price=90)
        i.save()
        i.purchase_set.create(name='Zhibek Kasymbekova', age=21, data_purchase=timezone.now())
        i.purchase_set.create(name='Ali Bayev', age=22, data_purchase=timezone.now())
        i.purchase_set.create(name='Talgat Abd', age=32, data_purchase=timezone.now())
        i.purchase_set.create(name='Eva AAlieva', age=32, data_purchase=timezone.now())
        i.purchase_set.create(name='Aslan Kapov', age=20, data_purchase=timezone.now())
        i.purchase_set.create(name='Adilet Kaniev', age=25, data_purchase=timezone.now())
        i.purchase_set.create(name='Almaz Azamatov', age=18, data_purchase=timezone.now())
        i.purchase_set.create(name='Alan Syrgak', age=9, data_purchase=timezone.now())
        i.purchase_set.create(name='Bermet Tariel', age=30, data_purchase=timezone.now())
        i.purchase_set.create(name='Diana Baygazieva', age=31, data_purchase=timezone.now())