import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int):
    new_text = text[start:]
    pnct = ['.', ',', '?', '!', ':', ';']
    while size > 0:

        try:
            if new_text[size-1] in pnct and new_text[size-2] in pnct:
                size -= 3
            elif new_text[size-1] in pnct:
                return new_text[:size], len(new_text[:size])

            else:
                size -= 1
        except Exception:
            size = len(new_text)






    # while end_point >= 0:
    #     if size >= len(new_text):
    #         end_point = len(new_text)
    #         if new_text[end_point-1] in pnct:
    #             return new_text[:end_point], len(new_text[:end_point])
    #     end_point -= 1

        # elif size < len(new_text):
        #     if new_text[size] in pnct and new_text[size+1] in pnct:
        #        i = size

        # if size < len(new_text):
        #     if new_text[end_point] in pnct and new_text[end_point+1] in pnct:
        #         end_point -= 1
        # elif new_text[end_point-1] in pnct:
        #     return new_text[:end_point], len(new_text[:end_point])
        # else:
        #     end_point -= 1
    # for char in new_text:
    #     if new_text[size] in pnct and new_text[size+1] in pnct:


text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'

print(*_get_part_text(text, 0, 54), sep='\n')

# text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'

# print(*_get_part_text(text, 22, 145), sep='\n')

# text = '''Будет ласковый дождь
#    В гостиной говорящие часы настойчиво пели:тик-так, семь часов, семь утра, вставать пора! -словно боясь, что их никто не послушает. Объятый утренней тишиной дом был пуст. Часы продолжали тикать и твердили, твердили свое в пустоту:девять минут восьмого, к завтраку все готово, девять минут восьмого!
#    На кухне печь сипло вздохнула и исторгла из своего жаркого чрева восемь безупречно поджаренных тостов, четыре глазуньи, шестнадцать ломтиков бекона, две чашки кофе и два стакана холодного молока.
#    - Сегодня в городе Эллендейле, штат Калифорния, четвертое августа две тысячи двадцать шестого года, - произнес другой голос, с потолка кухни. Он повторил число трижды, чтобы получше запомнили. - Сегодня день рождения мистера Фезерстоуна. Годовщина свадьбы Тилиты. Подошел срок страхового взноса, пора платить за воду, газ, свет.
#    Где то в стенах щелкали реле, перед электрическими глазами скользили ленты памятки.
#    Восемь одна, тик-так, восемь одна, в школу пора, на работу пора, живо, живо, восемь одна!Но не хлопали двери, и не слышалось мягкой поступи резиновых каблуков по коврам.
#    На улице шел дождь. Метеокоробка на наружной двери тихо пела: «Дождик, дождик целый день, плащ, галоши ты надень…» Дождь гулко барабанил по крыше пустого дома.
#    Во дворе зазвонил гараж, поднимая дверь, за которой стояла готовая к выезду автомашина… Минута, другая - дверь опустилась на место.
#    В восемь тридцать яичница сморщилась, а тосты стали каменными. Алюминиевая лопаточка сбросила их в раковину, оттуда струя горячей воды увлекла их в металлическую горловину, которая все растворяла и отправляла через канализацию в далекое море. Грязные тарелки нырнули в горячую мойку и вынырнули из нее, сверкая сухим блеском.
#    Девять пятнадцать, -пропели часы, -пора уборкой заняться.
#    Из нор в стене высыпали крохотные роботы-мыши. Во всех помещениях кишели маленькие суетливые уборщики из металла и резины Они стукались о кресла, вертели своими щетинистыми роликами, ерошили ковровый ворс, тихо высасывая скрытые пылинки. Затем исчезли, словно неведомые пришельцы, юркнули в свои убежища Их розовые электрические глазки потухли. Дом был чист.
#    Десять часов.Выглянуло солнце, тесня завесу дождя. Дом стоял одиноко среди развалин и пепла. Во всем городе он один уцелел. Ночами разрушенный город излучал радиоактивное сияние, видное на много миль вокруг.
#    Десять пятнадцать.Распылители в саду извергли золотистые фонтаны, наполнив ласковый утренний воздух волнами сверкающих водяных бусинок. Вода струилась по оконным стеклам, стекала по обугленной западной стене, на которой белая краска начисто выгорела. Вся западная стена была черной, кроме пяти небольших клочков. Вот краска обозначила фигуру мужчины, катящего травяную косилку. А вот, точно на фотографии, женщина нагнулась за цветком. Дальше - еще силуэты, выжженные на дереве в одно титаническое мгновение…Мальчишка вскинул вверх руки, над ним застыл контур подброшенного мяча, напротив мальчишки - девочка, ее руки подняты, ловят мяч, который так и не опустился.
#    Только пять пятен краски - мужчина, женщина, дети, мяч. Все остальное - тонкий слой древесного угля.
#    Тихий дождь из распылителя наполнил сад падающими искрами света…
#    Как надежно оберегал дом свой покой вплоть до этого дня! Как бдительно он спрашивал: «Кто там? Пароль?» И, не получая нужного ответа от одиноких лис и жалобно мяукающих котов, затворял окна и опускал шторы с одержимостью старой девы. Самосохранение, граничащее с психозом, - если у механизмов может быть паранойя.
#    Этот дом вздрагивал от каждого звука. Стоило воробью задеть окно крылом, как тотчас громко щелкала штора и перепуганная птица летела прочь. Никто - даже воробей - несмел прикасаться к дому!
#    Дом был алтарем с десятью тысячами священнослужителей и прислужников, больших и маленьких, они служили и прислуживали, и хором пели славу. Но боги исчезли, и ритуалпродолжался без смысла и без толку.
#    Двенадцать.
#    У парадного крыльца заскулил продрогнувший пес.
#    Дверь сразу узнала собачий голос и отворилась. Пес, некогда здоровенный, сытый, а теперь кожа да кости, весь в парше, вбежал в дом, печатая грязные следы. За ним суетились сердитые мыши - сердитые, что их потревожили, что надо снова убирать!
#    Ведь стоило малейшей пылинке проникнуть внутрь сквозь щель под дверью, как стенные панели мигом приподнимались, и оттуда выскакивали металлические уборщики. Дерзновенный клочок бумаги, пылинка или волосок исчезали в стенах, пойманные крохотными стальными челюстями. Оттуда по трубам мусор спускался в подвал, в гудящее чрево мусоросжигателя, который злобным Ваалом притаился в темном углу.
#    Пес побежал наверх, истерически лая перед каждой дверью, пока не понял - как это уже давно понял дом, - что никого нет, есть только мертвая тишина.
#    Он принюхался и поскреб кухонную дверь, потом лег возле нее, продолжая нюхать. Там, за дверью, плита пекла блины, от которых по всему дому шел сытный дух и заманчивыйзапах кленовой патоки.
#    Собачья пасть наполнилась пеной, в глазах вспыхнуло пламя. Пес вскочил, заметался, кусая себя за хвост, бешено завертелся и сдох. Почти час пролежал он в гостиной.
#    Два часа, -пропел голос.
#    Учуяв наконец едва приметный запах разложения, из нор с жужжанием выпорхнули полчища мышей, легко и стремительно, словно сухие листья, гонимые электрическим веером.
#    Два пятнадцать.
#    Пес исчез.
#    Мусорная печь в подвале внезапно засветилась пламенем, и через дымоход вихрем промчался сноп искр.
#    Два тридцать пять.
#    Из стен внутреннего дворика выскочили карточные столы. Игральные карты, мелькая очками, разлетелись по местам. На дубовом прилавке появились коктейли и сэндвичи сяйцом. Заиграла музыка.
#    Но столы хранили молчание, и никто не брал карт.
#    В четыре часа столы сложились, словно огромные бабочки, и вновь ушли в стены.'''

# print(*_get_part_text(text, 5501, 780), sep='\n')
