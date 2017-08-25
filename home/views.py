from django.shortcuts import render, render_to_response

class Person():
    def __init__(self):
        self.fullName = 'Остап-Сулейман-Берта-Мария-Бендер-бей'
        self.name = 'Остап Бендер'
        self.birthday = 'Родился в 1899—1900 году'
        self.hobby = 'Афёры и авантюры'
        self.study = 'Учился я в частной гимназии Илиади'
        self.work = ['У меня не мало выполненных проектов:',
                    'В Старгороде в один вечер сколотил подпольную организацию «Союз меча и орала»',
                    'Ради стула вдовы Грицацуевой женился на ней',
                    'В приволжском городке Васюки в роли международного гроссмейстера дал сеанс одновременной игры в шахматной секции',
                    'В Пятигорске успешно продавал билеты для входа в открытый для всех «Провал»',
                    'Вёл следствие по делу А. И. Корейко',
                    'и мн. др.']

def home(request):
    person = Person()
    return render_to_response('home.html', {'person': person, 'current_page': 'home'})

def study(request):
    person = Person()
    return render_to_response('study.html',  {'person': person, 'current_page': 'study'})

def work(request):
    person = Person()
    return render_to_response('work.html',  {'person': person, 'current_page': 'work'})

def quotes(request):
    person = Person()
    return render_to_response('quotes.html',  {'person': person, 'current_page': 'quotes'})