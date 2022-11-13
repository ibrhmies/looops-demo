# python random modülü

import random

# import komutu=> Modül çağırmaya yarar. 
# Örneğin yazacağınız programda belirtilen aralıkta rastgele tam sayı seçmeniz gerekiyor. 
# Bunun içinde "random" modülünü çağırmanız gerekiyor ve "randint" metodunu kullanmanız gerekiyor.

for i in range(10):
    print(random.random())

# random modülünün içinde random komutu 0 ve 1 arasında bize ondalık sayı üretecek

for i in range(10):
    print(random.uniform(10,30))

# random modülünün içinde uniform komutuyla alt ve üst sınır belirterek o sınır aralığında ondalık sayılar üretir



for i in range(10):
    print(random.randint(10,30))

# random modülünün içindeki randint komutuyla verdiğimiz iki sınır da dahil olmak üzere tam sayılar verecek bize rastgele üst sınır sadece randint komutunda dahildir.



for i in range(10):
    print(random.randrange(10,30,3))

# 10 dan başlayıp 30 a kadar 3 er 3 er artarak oluşan sayılardan rastgele seçilir


# random modülünün içindeki randrange komutuyla başlangıç be bitiş değerleri arasında istenilen sayı kadar artan değerlerden rastgele seçilir 
    

liste = ["pembe","mavi","mor","kırmızı"]

print(random.choice(liste))

# choice komutuylla oluşturduğumuz listeden rastgele bir eleman seçer choice kelime manası da seçmek tir.

liste = ["pembe","mavi","mor","kırmızı"]

random.shuffle(liste)

print(liste)

# shuffle komutu bize bir değer seçmez olan listenin elemanlarının yerini değiştirir.


liste = ["pembe","mavi","mor","kırmızı"]

print(random.sample(liste,2))

# sample komutu listeden kaç tane eleman seçileceğinin de girilmesini ister ve 
# yazdığın sayı kadar rastgele eleman seçer liste içinden



