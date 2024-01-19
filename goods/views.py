from django.shortcuts import render

# Create your views here.

def catalog(request):
    context = {
        'title':'Главная - Каталог',
       "goods":[
        {'image': 'deps/images/goods/01-sborka-el-shitov.jpg',
         'name': 'Модульный щит всборе',
         'description': 'Модульный щчит всборе автоматика, защита управления.',
         'price': 775.00},

         {'image': 'deps/images/goods/bolshoj-obzor-shchita-umnogo-doma-2.jpg',
         'name': 'Большой модульный щит всборе',
         'description': 'Большой модульный щит, с дополнительной секцией.',
         'price': 990.00},

         {'image': 'deps/images/goods/розетки.jpg',
         'name': 'Розетки для дома',
         'description': 'Розетки',
         'price': 100.00},

         {'image': 'deps/images/goods/legrand-smart-home-iphones-ru.jpg',
         'name': 'Розетки для умного дома',
         'description': 'Розетки для умного дома',
         'price': 120.00},

         {'image': 'deps/images/goods/legrand-smart-home-iphones-ru-6.jpg',
         'name': 'Выключатели для умного дома',
         'description': 'Выключатели для умного дома белые.',
         'price': 120.00},

         {'image': 'deps/images/goods/CHernye-vyklyuchateli-Xiaomi.jpg',
         'name': 'Выключатели для умного дома черные',
         'description': 'Выключатели Умный дом!',
         'price': 130.00},

         {'image': 'deps/images/goods/1-2.jpg',
         'name': 'Люстры для умного дома.',
         'description': 'Люстры с поддержкой Алисы, Google, II.',
         'price': 230.00},

         {'image': 'deps/images/goods/thumb600_84494700-1703668221.jpg',
         'name': 'Люстра Премиум Люкс.',
         'description': 'Люстра LUX',
         'price': 2300.00},

         {'image': 'deps/images/goods/1695853-1024x683.jpg',
         'name': 'Оборудование для умного дома',
         'description': 'Доп Оборудование для умного дома',
         'price': 139.00},

         {'image': 'deps/images/goods/Xiaomi_smarthome.jpg',
         'name': 'Оборудование для умного дома с дополнением',
         'description': 'Оборудование для умного дома с дополнением.',
         'price': 100.00},

         {'image': 'deps/images/goods/dremel-payalnik.jpg',
         'name': 'Инструменты',
         'description': 'Инструменты для монтажных работ.',
         'price': 200.00},

         {'image': 'deps/images/goods/IMG_1023-e1438459686607.jpg',
         'name': 'Инструменты',
         'description': 'Чемодан с инструментами.',
         'price': 510.00},
        ]

    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')