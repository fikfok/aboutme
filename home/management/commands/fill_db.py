from django.core.management.base import BaseCommand, CommandError
from home.models import Cities, Personages, Work, Quotes
from datetime import date

class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        # c = Cities.objects.all()
        # c.delete()
        #
        # p = Personages.objects.all()
        # p.delete()
        #
        # w = Work.objects.all()
        # w.delete()
        #
        # q = Quotes.objects.all()
        # q.delete()

        cities = [
            {"cityName": "Старгород",
             "description": """С таким названием города в нашей стране никогда не существовало. Зато он существовал в произведениях Н.Лескова и В.Лихачева. Ну и соответственно Ильфа и Петрова. 
Версий о прообразе существует несколько. Основная говорит о том, что Старгород это Старобельск. Дочь Ильфа — Александра Ильинична — писала, что в образе Старгорода (именовавшегося в рукописи Барановском или Барановом) просматриваются «кое-какие одесские реалии»""",
             "photo": "img/Stargorod.jpg"
             },
            {"cityName": "Москва",
             "description": """Знакомство с советской столицей начинается с небольшого лирического очерка о девяти вокзалах, через которые в Москву ежедневно входят тридцать тысяч приезжих.
Исследователи отмечают, что повествование Ильфа и Петрова о «воротах города» не во всём совпадает с публикациями других авторов, писавших о Москве времён НЭПа: к примеру, журналист Л. Кириллов в июльском номере журнала «Огонёк» (1927) сообщал о миллионе пассажиров, прибывающих в столицу на короткое время или «на постоянное жительство»: «Поближе к вокзалам, в узких, кривых уличках и переулках, гнездятся подслеповатые гостиницы, номера и глухие, зловонные и зловещие норы. По Рязанке маленькими артельками приезжает много крестьян на работу»""",
             "photo": "img/Moscow.jpg"
             },
            {"cityName": "По пути в Васюки",
             "description": """По данным Одесского и Фельдмана, описание вымышленного населённого пункта («…отсюда отправляются лесные материалы, смола, лыко, рогожи») совпадает со справочной информацией о городе Ветлуге, включённой в книгу «Поволжье, природа, быт, хозяйство» (Ленинград, 1926)""",
             "photo": "img/Vasuki.jpg"},
            {"cityName": "Пятигорск",
             "description": """В Пятигорске финансовые проблемы вынуждают Остапа прибегнуть к очередной махинации: приобретя на последние деньги квитанционную книжку, великий комбинатор отправляется к Провалу. 
Рассуждения великого комбинатора о том, что бесплатный вход в местную достопримечательность — это «позорное пятно на репутации города», являются имитацией шаблонных текстов, присущих высмеиваемым в прессе лозунгам — таким, как «Смыть с себя позорное пятно, догнать и перегнать выполнение плана» («Огонёк», 1930, 20 ноября).
Элемент пародии замечен и в стремлении героя разделить туристов на группы: предлагая скидку студентам и увеличивая стоимость билетов для тех, кто не состоит в профсоюзе, Бендер демонстрирует механизм развития советской системы «иерархий и привилегий»""",
             "photo": "img/Proval.jpg"},
            {"cityName": "Ялта",
             "description": """В Ялту Бендер и Воробьянинов отправляются после чтения газетной заметки, сообщающей об осенних гастролях театра Колумба в Крыму. В главе, повествующей о заключительном этапе их странствий, обыгрывание литературных мотивов соединено с описанием реальных происшествий. Так, сцена прибытия парохода «Пестель», встречаемого выстроившимися на набережной экипажами и праздной публикой, перекликается с эпизодом из чеховской «Дамы с собачкой».""",
             "photo": "img/Yalta.jpg"}
        ]
        for item in cities:
            item = Cities(**item)
            item.save()

        personages = [
            {"firstName": "Авессалом", "secondName": "Владимирович Изнурёнков"},
            {"firstName": "вдова", "secondName": "Грицацуева"},
            {"firstName": "инженер", "secondName": "Щукин"},
            {"firstName": "Ипполит", "secondName": "Воробьянинов"},
            {"firstName": "монтёр", "secondName": "Мечников"},
            {"firstName": "Никифор", "secondName": "Ляпис-Трубецкой"},
            {"firstName": "Остап", "secondName": "Бендер"},
            {"firstName": "Отец", "secondName": "Фёдор"},
            {"firstName": "редактор газеты", "secondName": "«Станок»"},
            {"firstName": "режиссёр театра", "secondName": "«Колумб»"},
            {"firstName": "Сторож", "secondName": "Октябрского вокзала"},
            {"firstName": "Элочка", "secondName": "Людоедочка"},
        ]
        for item in personages:
            item = Personages(**item)
            item.save()

        cityStaryiGorod = Cities.objects.get(cityName='Старгород')
        cityMoscow = Cities.objects.get(cityName='Москва')
        cityVasuki = Cities.objects.get(cityName='По пути в Васюки')
        cityPyatigorsk = Cities.objects.get(cityName='Пятигорск')
        cityYalta = Cities.objects.get(cityName='Ялта')

        perAvessalom = Personages.objects.get(firstName='Авессалом', secondName='Владимирович Изнурёнков')
        perGritsatsyeva = Personages.objects.get(firstName='вдова', secondName='Грицацуева')
        perShykin = Personages.objects.get(firstName='инженер', secondName='Щукин')
        perIppolit = Personages.objects.get(firstName='Ипполит', secondName='Воробьянинов')
        perMechnikov = Personages.objects.get(firstName='монтёр', secondName='Мечников')
        perLyapis = Personages.objects.get(firstName='Никифор', secondName='Ляпис-Трубецкой')
        perOstap = Personages.objects.get(firstName='Остап', secondName='Бендер')
        perFedor = Personages.objects.get(firstName='Отец', secondName='Фёдор')
        perEditor = Personages.objects.get(firstName='редактор газеты', secondName='«Станок»')
        perDirector = Personages.objects.get(firstName='режиссёр театра', secondName='«Колумб»')
        perGuard = Personages.objects.get(firstName='Сторож', secondName='Октябрского вокзала')
        perElochka = Personages.objects.get(firstName='Элочка', secondName='Людоедочка')

        works = [
            {"chairNumber": "1", "cityName": cityStaryiGorod,
             "description": "Особняк, ныне «2-й дом соцобеса». Стул был продан отцу Фёдору, Воробьянинов на улице сталкивается с ним и в драке стул ломается.",
             "personages": [perIppolit, perFedor], "result": "False"
             },
            {"chairNumber": "2", "cityName": cityStaryiGorod,
             "description": "После свадьбы на вдове Грицацуевой в первую же брачную ночь уходит от неё прихватив стул.",
             "personages": [perGritsatsyeva, perIppolit, perOstap], "result": "False"
             },
            {"chairNumber": "3", "cityName": cityMoscow,
             "description": "Бендре у Элочки-людоедочки, жены инженера Щукина, меняет стул на ситечко, украденное у мадам Грицацуевой.",
             "personages": [perOstap, perElochka], "result": "False"
             },
            {"chairNumber": "4", "cityName": cityMoscow,
             "description": "Инженер Щукин отдаёт стул Бендеру в благодарность за то, что он открыл захлопнувшуюся дверь.",
             "personages": [perShykin, perOstap], "result": "False"
            },
            {"chairNumber": "5", "cityName": cityMoscow,
             "description": "Бендер, выдав себя за судебного исполнителя, забирает стул за долги у рифмоплёта Авессалома Владимировича Изнурёнкова",
             "personages": [perAvessalom, perOstap], "result": "False"
            },
            {"chairNumber": "6", "cityName": cityMoscow,
             "description": "Бендер находит стул в кабинете редактора газеты «Станок»",
             "personages": [perOstap, perEditor], "result": "False"
            },
            {"chairNumber": "7", "cityName": cityMoscow,
             "description": "Остап проникает в комнату Никифора Ляписа-Трубецкого и вскрывает стул.",
             "personages": [perLyapis, perOstap], "result": "False"
            },
            {"chairNumber": "8", "cityName": cityVasuki,
             "description": "Бендер крадёт стул на пароходе «Скрябин» из каюты режиссёра.",
             "personages": [perIppolit, perOstap, perDirector], "result": "False"
            },
            {"chairNumber": "9", "cityName": cityPyatigorsk,
             "description": "Остап вступает в сговор с монтёр Мечниковым для кражи стула театра «Колумб». Первый стул.",
             "personages": [perIppolit, perMechnikov, perOstap], "result": "False"
            },
            {"chairNumber": "10", "cityName": cityPyatigorsk,
             "description": "Остап вступает в сговор с монтёр Мечниковым для кражи стула театра «Колумб». Второй стул.",
             "personages": [perIppolit, perMechnikov, perOstap], "result": "False"
            },
            {"chairNumber": "11", "cityName": cityYalta,
             "description": "Бендер и Воробьянинов похищают стул в театре Колумба после спектакля.",
             "personages": [perIppolit, perOstap], "result": "False"
            },
            {"chairNumber": "12", "cityName": cityMoscow,
             "description": "Товарный двор Октябрьского вокзала. Сторож случайно находит драгоценности.",
             "personages": [perGuard], "result": "True"
            }
        ]

        workModelsArray = [Work() for i in range(12)]
        for i, work in enumerate(workModelsArray):
            for key, val in works[i].items():
                if key != 'personages':
                    setattr(work, key, works[i][key])
            work.save()

        # Для many-to-many требуется чтобы у записи уже был сгенерирован идентификатор,
        # т.е. запись необходимо предварительно сохранить в БД
        # Во втором цикле идёт генерация many-to-many связей
        for i, work in enumerate(workModelsArray):
            setattr(work, 'personages', works[i]['personages'])
            work.save()

        quotes = [
            {"title": "Ну что, отец, невесты в вашем городе есть",
             "link": "<iframe width=\"491\" height=\"276\" src=\"https://www.youtube.com/embed/s713ZJ9Xmoc?start=12&end=18\" frameborder=\"0\" allowfullscreen></iframe>"
            },
            {"title": "Отец русской демократии",
             "link": "<iframe width=\"491\" height=\"276\" src=\"https://www.youtube.com/embed/s713ZJ9Xmoc?start=151&end=158\" frameborder=\"0\" allowfullscreen></iframe>"
            },
            {"title": "Киса, я давно хотел вас спросить",
             "link": "<iframe width=\"491\" height=\"276\" src=\"https://www.youtube.com/embed/s713ZJ9Xmoc?start=379&end=394\" frameborder=\"0\" allowfullscreen></iframe>"
            },
            {"title": "Утром деньги, вечером стулья",
             "link": "<iframe width=\"491\" height=\"276\" src=\"https://www.youtube.com/embed/s713ZJ9Xmoc?start=475&end=480\" frameborder=\"0\" allowfullscreen></iframe>"
            }
        ]
        for item in quotes:
            item = Quotes(**item)
            item.save()