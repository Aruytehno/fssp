from xml.dom import minidom

# https://opendata.fssp.gov.ru
# https://opendata.fssp.gov.ru/files/fssp/db/files/00smev2018/opisanie_api_bdip_fssp_20190920.pdf


class Person:
    dateBirth = ''  # ДатаРождения
    dateEmployment = ''  # ДатаПриема
    position = ''  # Должность
    # ФИО
    surname = ''  # Фамилия
    name = ''  # Имя
    patronymic = ''  # Отчество

    region = ''  # Регион
    subdivision = ''  # Подразделение
    # ФИО изменённые
    surnameChange = ''  # Фамилия
    nameChange = ''  # Имя
    patronymicChange = ''  # Отчество
    # Паспорт
    passportSeries = ''  # ДокументСерия
    passportNumber = ''  # ДокументНомер
    issued = ''  # ДокументКемВыдан
    dateOfIssue = ''  # ДокументДатаВыдачи
    departmentCode = ''  # ДокументКодПодразделения


def parseXML():
    person = Person()
    xmldoc = minidom.parse('example.xml')
    itemlist = xmldoc.getElementsByTagName('Сотрудник')
    listPerson = []

    for item in itemlist:
        person.dateBirth = item.attributes['ДатаРождения'].value
        person.dateEmployment = item.attributes['ДатаПриема'].value
        person.position = item.attributes['Должность'].value
        fio = item.attributes['ФИО'].value.split(" ")
        if list(fio)[0]:
            if len(list(fio)) == 3:
                person.surname = fio[0]
                person.name = fio[1]
                person.patronymic = fio[2]
        person.region = item.attributes['Регион'].value
        person.subdivision = item.attributes['Подразделение'].value

        fioChange = item.attributes['ФИОизм'].value.split(" ")
        if list(fioChange)[0]:
            if len(list(fioChange)) == 3:
                person.surnameChange = fioChange[0]
                person.nameChange = fioChange[1]
                person.patronymicChange = fioChange[2]
        person.passportSeries = item.attributes['ДокументСерия'].value
        person.passportNumber = item.attributes['ДокументНомер'].value
        person.issued = item.attributes['ДокументКемВыдан'].value
        person.dateOfIssue = item.attributes['ДокументДатаВыдачи'].value
        person.departmentCode = item.attributes['ДокументКодПодразделения'].value
        listPerson.append(person)
    return listPerson


if __name__ == '__main__':
    listPerson = parseXML()
    print(str(len(listPerson)) + " strings in xml file")
    for person in listPerson:
        print(person.__dict__)