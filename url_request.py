# https://stackoverflow.com/questions/5607551/how-to-urlencode-a-querystring-in-python
import urllib
from urllib.request import urlopen
from urllib.parse import unquote

def main():
    url = "http://highload.kocherov.net/parser/api/info_api/?type=TYPE_SEARCH_FIZ&regionID=-1&lastName=%22%D0%A1%D0%BE%D0%B1%D0%B8%D1%82%D0%BD%D1%8E%D0%BA%22&firstName=%22%D0%AE%D1%80%D0%B8%D0%B9%22&patronymic=%22%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D0%B8%D1%87%22&dob=%2225.03.1994%22&key=b502e37a2313a9cf56f041b0324dd713&thread=10"

    print(unquote(url))
    html = urlopen(url).read()
    print(html)


if __name__ == "__main__":
    main()
