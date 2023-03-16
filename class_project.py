

class Project:
    def __init__(self, num, title, day, month, year, lang, qty_line):
        self.num = num
        self.title = title
        self.day = day
        self.month = month
        self.year = year
        self.lang = lang
        self.qty_line = qty_line

    def __str__(self):
        fecha = str(self.day) + "-" + str(self.month) + "-" + str(self.year)
        langs = languajes(self.lang)
        r = ""
        r += '{:<20}'.format(" Project ID: " + str(self.num))
        r += '{:<20}'.format(" Title: " + self.title)
        r += '{:<20}'.format(" Date: " + fecha)
        r += '{:<23}'.format(" Language: " + langs)
        r += '{:<20}'.format(" Quantity Lines: " + str(self.qty_line))
        return r


def languajes(i):
    languages = "Python", "Java", "C++", "Javascript", "Shell", "HTML", "Ruby", "Swift", "C#", "VB", "Go"
    return languages[i]
