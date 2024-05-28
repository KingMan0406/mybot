import sqlite3

def create_table_and_insert_data():
    conn = sqlite3.connect('faq1.db')
    c = conn.cursor()
    
    c.execute('''
    CREATE TABLE IF NOT EXISTS faq1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_ru TEXT,
        answer_ru TEXT,
        question_kg TEXT,
        answer_kg TEXT
    )
    ''')
    
    faq_data = [
        ("Какие предметы нужно сдавать для поступления на специальность информационных технологий?", 
         "Обычно необходимо сдавать профильную математику и/или физику.", 
         "Маалыматтык технологиялар адистигине кирүү үчүн кандай предметтерден өтүш керек?", 
         "Адатта, сиз адистештирилген математика жана/же физиканы тапшырышыңыз керек."),
        ("Есть ли возможность обучения на дистанционной или заочной форме в вашем университете для студентов, выбравших информационные технологии?", 
         "У нас предусмотрена только очная форма обучения.", 
         "Сиздин университетте маалыматтык технологияларды тандаган студенттер үчүн дистанттык же сырттан окуу мүмкүнчүлүгү барбы?", 
         "Биз күндүзгү гана билим беребиз."),
        ("Каковы основные критерии для получения стипендии в вашем университете на специальность информационные технологии?", 
         "Стипендия выдается на основе суммирования основного балла и дополнительных баллов, которые могут быть получены за сдачу экзаменов по физике или математике.", 
         "Сиздин университетиңизде маалыматтык технологиялар адистигине стипендия алуунун негизги критерийлери кандай?", 
         "Стипендия физика же математика боюнча экзамендерди тапшыруу үчүн алынуучу негизги баллдын жана кошумча баллдардын суммасынын негизинде берилет."),
        ("Есть ли в вашем университете возможность пройти стажировку или практику в сфере информационных технологий?", 
         "Да, наш университет сотрудничает с различными компаниями, где студенты могут проходить стажировку и практику.", 
         "Сиздин университетиңизде маалыматтык технологиялар тармагында стажировкадан же практикадан өтүүгө мүмкүнчүлүк барбы?", 
         "Ооба, биздин университет студенттер практикадан жана практикадан өтө ала турган ар кандай компаниялар менен кызматташат."),
        ("Какие перспективы трудоустройства для выпускников специальности информационные технологии в вашем регионе и за рубежом?", 
         "Специалисты в области информационных технологий весьма востребованы как в нашем регионе, так и за рубежом, что создает хорошие перспективы трудоустройства для выпускников.", 
         "Сиздин аймакта жана чет өлкөлөрдө маалыматтык технологиялар боюнча бүтүрүүчүлөр үчүн жумушка орношуу кандай болот?", 
         "Маалыматтык технологиялар чөйрөсүндөгү адистерге биздин аймакта да, чет өлкөлөрдө да суроо-талап чоң, бул бүтүрүүчүлөр үчүн жакшы иш менен камсыз кылуу мүмкүнчүлүктөрүн түзөт."),
        ("Какие дополнительные возможности или программы предлагает ваш университет для студентов, изучающих информационные технологии?", 
         "Мы предлагаем различные дополнительные программы, такие как курсы повышения квалификации, мастер-классы от ведущих специалистов и участие в проектах с внешними компаниями.", 
         "Сиздин университет маалымат технологиялары боюнча студенттер үчүн кандай кошумча мүмкүнчүлүктөрдү же программаларды сунуштайт?", 
         "Биз ар кандай кошумча программаларды сунуштайбыз, мисалы, квалификацияны жогорулатуу курстары, алдыңкы эксперттердин мастер-класстары жана тышкы компаниялар менен долбоорлорго катышуу."),
        ("Каковы условия проживания для студентов вашего университета, изучающих информационные технологии?", 
         "У нас нет собственного общежития, но мы можем помочь студентам найти жилье вне кампуса.", 
         "Сиздин университетте маалымат технологиялары боюнча студенттер үчүн жашоо шарттары кандай?", 
         "Биздин өзүбүздүн резиденциябыз жок, бирок биз студенттерге кампустан тышкары турак жай табууга жардам бере алабыз."),
        ("Какие языковые требования существуют для поступления на направление информационные технологии?", 
         "Обычно для поступления на эту специальность не требуется сдача языковых экзаменов, но знание английского языка может быть полезным в работе с информацией и технологиями.", 
         "Маалыматтык технологиялар адистигине кирүү үчүн кандай тил талаптары бар?", 
         "Адатта бул адистикке кирүү үчүн тил экзамендерин тапшыруунун кереги жок, бирок англис тилин билүү маалымат жана технология менен иштөөдө пайдалуу болушу мүмкүн."),
        ("Каковы возможности для получения международного опыта или обучения за рубежом для студентов вашего университета, изучающих информационные технологии?", 
         "Наш университет имеет партнерские отношения с различными университетами за рубежом, что создает возможности для обмена студентами и участия в международных программах обмена.", 
         "Сиздин университетиңизде маалымат технологиялары боюнча студенттер үчүн эл аралык тажрыйба же чет өлкөдө окуу үчүн кандай мүмкүнчүлүктөр бар?", 
         "Биздин университет чет мамлекеттердин ар кандай университеттери менен өнөктөштүк байланышта болуп, студенттерди алмашууга жана эл аралык алмашуу программаларына катышууга мүмкүнчүлүк түзүүдө."),
        ("Какие карьерные возможности доступны для выпускников вашего университета, специализирующихся в области информационных технологий?", 
         "Выпускники нашего университета имеют возможность работать в различных компаниях в качестве программистов, системных аналитиков, разработчиков ПО и других профессиональных областях в сфере информационных технологий.", 
         "Сиздин университеттин маалыматтык технологиялар адистиги боюнча бүтүрүүчүлөрү үчүн кандай карьералык мүмкүнчүлүктөр бар?", 
         "Университетибиздин бүтүрүүчүлөрү ар кандай компанияларда программист, системалык аналитик, программалык камсыздоону иштеп чыгуучу жана башка маалымат технологиялары тармагында кесипкөй тармактарда иштөө мүмкүнчүлүгүнө ээ."),
        ("Предоставляется ли общежитие?", 
         "К сожалению, общежитие не предусмотрено. Возможность найти хорошую работу после окончания обучения в университете высока, так как специалисты в данной сфере востребованы.", 
         "Жатакана каралганбы?", 
         "Тилекке каршы, жатакана каралган эмес. Университетти аяктагандан кийин жакшы жумуш табуу мүмкүнчүлүгү жогору, анткени бул тармакта адистер талап кылынат."),
        ("Каковы возможности продолжения обучения после первого тура?", 
         "На третьем курсе будет конкурс, и прошедшие его смогут продолжить обучение в университете WHZ в Германии.", 
         "Биринчи турдан кийин окууну улантуу үчүн кандай мүмкүнчүлүктөр бар?", 
         "Үчүнчү курста сынак болуп, андан өткөндөр Германиядагы WHZ университетинде окуусун уланта алышат."),
        ("Есть ли возможности продолжения обучения переводом с другого вуза в ваш вуз?", 
         "Есть, необходимо предоставить табель успеваемости/транскрипт для расчёта академической разницы. Подходите в институт с документами.", 
         "Башка университеттен сиздин университетиңизге которулуп окууну улантууга мүмкүнчүлүктөр барбы?", 
         "Ооба, академиялык айырманы эсептөө үчүн сиз отчёттук картаны/транскриптти беришиңиз керек. Институтка документтер менен келгиле."),
        ("Какой проходной балл для поступления в ваш вуз?", 
         "Основной 110, предметный 60 и выше (математика или физика).", 
         "Сиздин университетке кирүү үчүн өтүү баллы кандай?", 
         "Негизги 110, предмет 60 жана андан жогору (математика же физика)."),
        ("Когда начнется первый тур?", 
         "Начало 1 тура еще не известно, но приблизительно 10 июля.", 
         "Биринчи тур качан башталат?", 
         "1-турдун башталышы азырынча белгисиз, бирок болжол менен 10-июль."),
        ("Сколько стоит обучение за один год?", 
         "Стоимость обучения 100 тыс. сом.", 
         "Бир жылдык окуу канча турат?", 
         "Окуу акысы 100 миң сом."),
        ("Какие документы нужны для поступления?", 
         "Сертификат ОРТ (110 и выше), аттестат об окончании средней школы, 2 копии паспорта, фото 3 * 4, 6 штук (с Ф.И.О на обратной стороне), приписное свидетельство (при предъявлении оригинала копия принимается).", 
         "Кабыл алуу үчүн кандай документтер керек?", 
         "ЖРТ сертификаты (110 жана андан жогору), орто билими тууралуу аттестат, паспорттун 2 көчүрмөсү, 3*4 сүрөт, 6 даана (арт жагында аты-жөнү толук жазылган), каттоодон өткөндүгү тууралуу күбөлүк (көчүрмөсү түп нускасы көрсөтүлгөндө кабыл алынат)."),
        ("Есть ли вступительные экзамены?", 
         "Вступительных экзаменов нет.", 
         "Кирүү экзамендери барбы?", 
         "Кирүү экзамендери жок."),
        ("Есть ли льготы?", 
         "На данный момент льгот нет.", 
         "Жеңилдиктер барбы?", 
         "Азыркы учурда жеңилдиктер жок."),
        ("Когда начинаются занятия?", 
         "1 сентября.", 
         "Сабактар качан башталат?", 
         "1-сентябрь."),
        ("Где будет проходить обучение?", 
         "Занятии будут офлайн в ВУЗе по адресу г. Бишкек ул. Тимирязева 74. 720010", 
         "Окуу кайда өтөт?", 
         "Бишкек ш. Тимирязева 74. 720010көчөсүндөгү университетте сабактар ​​оффлайн режиминде өтөт."),
        ("Возможен ли перевод в другие учебные заведения?", 
         "Возможно, необходимо будет сдать академическую разницу.", 
         "Башка окуу жайларына которулууга болобу?", 
         "Мүмкүн, академиялык айырманы тапшыруу керек.")
    ]
    
    c.executemany('''
    INSERT INTO faq1 (question_ru, answer_ru, question_kg, answer_kg)
    VALUES (?, ?, ?, ?)
    ''', faq_data)
    
    conn.commit()
    conn.close()

create_table_and_insert_data()