from logging import disable
import requests
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.text import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

#Global variables acting as cookies
screenx = float(Config.get('graphics', 'width'))
screeny = float(Config.get('graphics', 'height'))

userid = ["userid"]
password = ["password"]

course = []
user = []

iuser = ["iuser"]
ipass = ["ipass"]
ilevel = ["ilevel"]

cname = ["cname"]
cteacher = ["cteacher"]
cyear = ["cyear"]



#DOM Root
root = FloatLayout() 

#Components
def button(i, j, text, press):

    def function(event):
        press()

    button = Button()
    button.text = text
    button.pos = (i, j)
    button.size = (100, 30)
    button.background_color = (255, 1, 1, 1)
    button.bind(on_press = function) 
    return button

def label(i, j, text):
    label = Label()
    label.font_size = '18sp'
    label.pos = (i, j)
    label.text = text
    return label

def banner_and_background(Screen):
    with Screen.canvas:
        Color(0.4, 0.4, 0.4, 0.3)
        Rectangle(pos=root.pos, size=(screenx, screeny))
        Color(0.2, 0.2, 0.2, 0.7)
        Rectangle(pos=(150,500), size=(500, 100))
    label = Label()
    label.font_size = '36sp'
    label.pos = (350, 500)
    label.text = "AttenBuddy-Desktop"
    Screen.add_widget(label)

def textinput(i, j, var):
    textinput = TextInput()
    textinput.pos = (i, j)
    textinput.font_size = '16sp'
    textinput.size = (150, 30)

    def function(instance, value):
        var[0] = value

    textinput.bind(text = function)
    return textinput

def BadgeC(teacher, name, y):

    mail = BoxLayout(orientation='horizontal')
    mail.size_hint = (1, None)

    label = Button(disabled=True)
    mess = Button(disabled=True)
    year = Button(disabled=True)

    label.text =  teacher
    mess.text =  name
    year.text = y

    mess.color = (0,0,0, 1)
    mess.background_color = (255,255,255, 255)
    year.color = (0,0,0, 1)
    year.background_color = (255,255,255, 255)
    label.background_color = (1,1,255, 1) 

    mess.size_hint = (6, 1)
    year.size_hint= (1, 1)
    label.size_hint = (2, 1)

    mail.add_widget(label)
    mail.add_widget(mess)
    mail.add_widget(year)
    
    return mail

def BadgeU(teacher, name, y):

    mail = BoxLayout(orientation='horizontal')
    mail.size_hint = (1, None)

    label = Button(disabled=True)
    mess = Button(disabled=True)
    year = Button(disabled=True)

    label.text =  teacher
    mess.text =  name
    year.text = y

    mess.color = (0,0,0, 1)
    mess.background_color = (255,255,255, 255)
    year.color = (0,0,0, 1)
    year.background_color = (255,255,255, 255)
    label.background_color = (1,1,255, 1) 

    mess.size_hint = (5, 1)
    year.size_hint= (4, 1)
    label.size_hint = (3, 1)

    mail.add_widget(label)
    mail.add_widget(mess)
    mail.add_widget(year)
    
    return mail
    
def scrollgridC(Screen,components,pos, size):
    grid = GridLayout(cols=1, size_hint_y=None)
    grid.bind(minimum_height=grid.setter('height'))
   
    for i in components:
        grid.add_widget(BadgeC(i['teacher'], i['name'], i['year']))

    scroll = ScrollView(size_hint=(1, None), pos=pos, size=size)
    scroll.do_scroll_y = True
    scroll.do_scroll_x = False
    scroll.add_widget(grid)
    return scroll

def scrollgridU(Screen,components,pos, size):
    grid = GridLayout(cols=1, size_hint_y=None)
    grid.bind(minimum_height=grid.setter('height'))
   
    for i in components:
        grid.add_widget(BadgeU(i['level'], i['userid'], i['password']))

    scroll = ScrollView(size_hint=(1, None), pos=pos, size=size)
    scroll.do_scroll_y = True
    scroll.do_scroll_x = False
    scroll.add_widget(grid)
    return scroll

def AddU():
        data = {
            'userid': iuser[0],
            'password': ipass[0],
            'level': ilevel[0],
        }

        url  = "https://attenbuddy.herokuapp.com/add_student"
        if(ilevel[0] == "teacher"):
             url  = "https://attenbuddy.herokuapp.com/add_teacher"

        res = requests.post(url = url,data=data).json()
        root.clear_widgets()
        root.add_widget(User())

def DeleteU():
        data = {
            'userid': iuser[0],
            'password': ipass[0],
            'level': ilevel[0],
        }

        url  = "https://attenbuddy.herokuapp.com/delete_student"
        if(ilevel[0] == "teacher"):
             url  = "https://attenbuddy.herokuapp.com/delete_teacher"

        res = requests.post(url = url,data=data).json()
        root.clear_widgets()
        root.add_widget(User())

def User():
    User = Widget()
    banner_and_background(User)
    with User.canvas:
        Color(0.3, 0.3, 0.3, 0.9)
        Rectangle(pos=(40,70), size=(400, 400))
        Color(0.3, 0.3, 0.3, 0.9)
        Rectangle(pos=(510,150), size=(250, 320))
        Color(0.2, 0.2, 0.2, 1)
        Rectangle(pos=(600,150), size=(160, 320))
        Color(0.3, 0.3, 0.3, 0.9)

    User.add_widget(label(525, 390, "UserId"))
    User.add_widget(label(535, 310, "Password"))
    User.add_widget(label(520, 230, "Level"))
    User.add_widget(textinput(550, 390, iuser))
    User.add_widget(textinput(550, 310, ipass))
    User.add_widget(textinput(550, 230, ilevel))
    User.add_widget(button(530, 170, "Add", AddU))
    User.add_widget(button(640, 170, "Delete", DeleteU)) 

    def fun1(event):
        root.clear_widgets()
        root.add_widget(Index()) 
    b1 = Button()
    b1.text = "Back"
    b1.font_size = "16sp"
    b1.size = (100, 40)
    b1.pos = (690, 10)
    b1.background_color = (255, 1, 1, 1)
    b1.bind(on_press = fun1) 
    User.add_widget(b1)

    res = requests.get(url = "https://attenbuddy.herokuapp.com/getteacher").json()
    user = res['data']
    res = requests.get(url = "https://attenbuddy.herokuapp.com/getstudent").json()
    user = user +  res['data']
    User.add_widget(scrollgridU(Index, user, pos=(40, 70), size=(400, 400)))
    return User

def AddC():
        data = {
            'course': cname[0],
            'teacher': cteacher[0],
            'year': cyear[0],
        }
        res = requests.post(url = "https://attenbuddy.herokuapp.com/add_course",data=data).json()
        root.clear_widgets()
        root.add_widget(Course())

def DeleteC():
        data = {
            'course': cname[0],
            'teacher': cteacher[0],
            'year': cyear[0],
        }
        res = requests.post(url = "https://attenbuddy.herokuapp.com/delete_course",data=data).json()
        root.clear_widgets()
        root.add_widget(Course())

def Course():
    Course = Widget()
    banner_and_background(Course)
    with Course.canvas:
        Color(0.3, 0.3, 0.3, 0.9)
        Rectangle(pos=(40,70), size=(400, 400))
        Color(0.3, 0.3, 0.3, 0.9)
        Rectangle(pos=(510,150), size=(250, 320))
        Color(0.2, 0.2, 0.2, 1)
        Rectangle(pos=(600,150), size=(160, 320))
        Color(0.3, 0.3, 0.3, 0.9)


    Course.add_widget(label(525, 390, "Name"))
    Course.add_widget(label(530, 310, "Teacher"))
    Course.add_widget(label(520, 230, "Year"))
    Course.add_widget(textinput(550, 390, cname))
    Course.add_widget(textinput(550, 310, cteacher))
    Course.add_widget(textinput(550, 230, cyear))
    Course.add_widget(button(530, 170, "Add", AddC))
    Course.add_widget(button(640, 170, "Delete", DeleteC))
    

    def fun1(event):
        root.clear_widgets()
        root.add_widget(Index()) 
    b1 = Button()
    b1.text = "Back"
    b1.font_size = "16sp"
    b1.size = (100, 40)
    b1.pos = (690, 10)
    b1.background_color = (255, 1, 1, 1)
    b1.bind(on_press = fun1) 
    Course.add_widget(b1)

    res = requests.get(url = "https://attenbuddy.herokuapp.com/getcourse").json()
    course = res['data']
    Course.add_widget(scrollgridC(Index, course, pos=(40, 70), size=(400, 400)))
    return Course

def Index():
    Index = Widget()
    banner_and_background(Index)

    def fun1(event):
        root.clear_widgets()
        root.add_widget(User())
    
    b1 = Button()
    b1.text = "User"
    b1.font_size = "28sp"
    b1.size = (200, 200)
    b1.pos = (200, 200)
    b1.background_color = (255, 1, 1, 1)
    b1.bind(on_press = fun1) 
    Index.add_widget(b1)

    def fun2(event):
        root.clear_widgets()
        root.add_widget(Course())

    b2 = Button()
    b2.text = "Course"
    b2.font_size = "28sp"
    b2.size = (200, 200)
    b2.pos = (400, 200)
    b2.background_color = (255, 1, 1, 1)
    b2.bind(on_press = fun2) 
    Index.add_widget(b2)


    return Index

def Login():
    data = {'userid':userid[0], 'password': password[0]}
    res = requests.post(url = "https://attenbuddy.herokuapp.com/isauth",data=data).json()
    if(res['success'] == "True" and res['data']['level'] == "admin"):
        root.clear_widgets()
        root.add_widget(Index())
    else:
        root.clear_widgets()
        root.add_widget(Account())
    
def Account():
    Account = Widget()
    banner_and_background(Account)
    with Account.canvas:
        Color(0.3, 0.3, 0.3, 0.9)
        Rectangle(pos=(60,150), size=(250, 320))
        Color(0.2, 0.2, 0.2, 1)
        Rectangle(pos=(150,150), size=(160, 320))
        Color(0.3, 0.3, 0.3, 0.9)


    Account.add_widget(label(50, 400, "Userid"))
    Account.add_widget(label(65, 320, "Password"))
    Account.add_widget(textinput(80, 400, userid))
    Account.add_widget(textinput(80, 320, password))
    Account.add_widget(button(180, 250, "Login", Login))

    return Account

root.add_widget(Account())

class App(App):
    def build(self):
        return root

if __name__ == "__main__":
    App().run()
