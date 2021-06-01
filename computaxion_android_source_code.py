from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.behaviors import RectangularElevationBehavior, RectangularRippleBehavior, BackgroundColorBehavior
from kivymd.font_definitions import theme_font_styles
from kivy.uix.scrollview import ScrollView
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.uix.popup import Popup
from kivymd.uix.button import MDRectangleFlatButton, MDRectangleFlatIconButton, MDFlatButton, MDIconButton
import ttg
import numpy as np
from kivy.uix.textinput import TextInput
from tabulate import tabulate
import boolean

Window.size = (800,700)
Window.minimum_width, Window.minimum_height = Window.size

helper_string = '''

ScreenManager:
    TwoWindow:

<TwoWindow>:
    name:"two"
    value:value
    inbase:inbase
    outbase:outbase
    entry:entry
    entry1:entry1
    pop1:pop1
    tensvalue:tensvalue
    tensinbase:tensinbase
    asciivalue:asciivalue
    nav_drawer:nav_drawer
    variablestring:variablestring
    formulastring:formulastring
    runlengthstring:runlengthstring
    simplifier_text : simplifier_text
    NavigationLayout: 
        ScreenManager:
            id:screen_manager
            Screen:
                name:"screen3"
                BoxLayout:
                    size_hint:.8,.7
                    pos_hint:{"center_x":.5,"center_y":.4875}
                    orientation:"vertical"
                    spacing:dp(20)
                    padding:dp(35)
                    MDFlatButton:
                        pos_hint:{"center_x":.5}
                        text:"Info"
                        text_color:(1,1,1,1)
                        halign:"center"
                        size_hint:.2,.07
                        md_bg_color:app.theme_cls.primary_color
                        on_release:root.show_data(obj="Input is a character in the ASCII character set, then press one of the four available bases to see the character's representation in those bases.")
                    MDTextField:
                        size_hint:.95,.1
                        hint_text:"Input        "
                        md_bg_color:app.theme_cls.primary_color
                        mode:"rectangle"
                        id:asciivalue
                        pos_hint:{"center_x":.5}
                    MDRectangleFlatButton:
                        size_hint:.8,.1
                        pos_hint:{"center_x":.5}
                        text:"bin"
                        on_release:root.conv(2)
                    MDRectangleFlatButton:
                        size_hint:.8,.1
                        text:"oct"
                        on_release:root.conv(8)
                        pos_hint:{"center_x":.5}
                    MDRectangleFlatButton:
                        size_hint:.8,.1
                        text:"dec"
                        on_release:root.conv(10)
                        pos_hint:{"center_x":.5}
                    MDRectangleFlatButton:
                        size_hint:.8,.1
                        text:"hex"
                        on_release:root.conv(16)
                        pos_hint:{"center_x":.5}
                    MDFlatButton:
                        pos_hint:{"center_x":.5}
                        halign:"center"
                        text:"Clear"
                        md_bg_color:app.theme_cls.primary_color
                        size_hint:.2,.07
                        text_color:(1,1,1,1)
                        on_release:root.clearThree()
            Screen:
                name:"screen1"
                BoxLayout:
                    size_hint:.65,.5
                    pos_hint:{"center_x":.5,"center_y":.6}
                    orientation:"vertical"
                    spacing:dp(20)
                    padding:dp(20)
                    MDFlatButton:
                        pos_hint:{"center_x":.5}
                        text:"Info"
                        size_hint:.2,.1
                        text_color:(1,1,1,1)
                        md_bg_color:app.theme_cls.primary_color
                        on_release:root.show_data(obj="Enter the input's base, desired output base and the value to be converted. Input base and output base should both be less than 37. Press convert to see result.")
                    MDTextField:
                        mode:"rectangle"
                        id:inbase
                        hint_text:"Input base       "
                        size_hint:.8,.14
                        pos_hint:{"center_x":.5}
                        md_bg_color:app.theme_cls.primary_color
                    MDTextField:
                        mode:"rectangle"
                        id:outbase
                        size_hint:.8,.14
                        hint_text:"Output base      "
                        pos_hint:{"center_x":.5}
                        md_bg_color:app.theme_cls.primary_color
                    MDTextField:
                        id:value
                        hint_text:"Value        "
                        mode:"rectangle"
                        size_hint:.8,.14
                        pos_hint:{"center_x":.5}
                        md_bg_color:app.theme_cls.primary_color
                    MDFlatButton:
                        pos_hint:{"center_x":.5}
                        halign:"center"                                                                                                            
                        text:"Convert"
                        size_hint:.2,.1
                        text_color:(1,1,1,1)
                        md_bg_color:app.theme_cls.primary_color    
                        on_release:root.converter()
                    MDFlatButton:
                        pos_hint:{"center_x":.5}
                        halign:"center"
                        text:"Clear"
                        size_hint:.2,.1    
                        text_color:(1,1,1,1)              
                        md_bg_color:app.theme_cls.primary_color                                                                                         
                        on_release:root.clearOne()             
            Screen:
                name:"screen2"
                BoxLayout:
                    orientation:"vertical"
                    MDTabs:
                        size_hint:.7,.7
                        pos_hint:{"center_x":.5}
                        size:"32dp","32dp"
                        md_bg_color:app.theme_cls.primary_color
                        id:tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        Tab:
                            id:tabs
                            text:"twos"           
                            BoxLayout:
                                size_hint:.8,.5
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(20)
                                padding:dp(20)
                                MDFlatButton:
                                    pos_hint:{"center_x":.5}
                                    size_hint:
                                    text:"Info"
                                    text_color:(1,1,1,1)
                                    md_bg_color:app.theme_cls.primary_color    
                                    size_hint:.2,.1                            
                                    on_release:root.show_data(obj="Enter the input's base (<37), the value to be converted and the number of bits to be used. Press calcualte to see results.")
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Value        "
                                    md_bg_color:app.theme_cls.primary_color
                                    id:entry
                                    pos_hint:{"center_x":.5}
                                    size_hint:.8,.15
                                MDTextField:
                                    hint_text:"Input base       "
                                    mode:"rectangle"
                                    md_bg_color:app.theme_cls.primary_color
                                    id:pop1
                                    pos_hint:{"center_x":.5}
                                    size_hint:.8,.15
                                MDTextField:
                                    hint_text:"Bits         "
                                    mode:"rectangle"
                                    md_bg_color:app.theme_cls.primary_color
                                    id:entry1
                                    pos_hint:{"center_x":.5}
                                    size_hint:.8,.15
                                MDFlatButton:
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    size_hint:.2,.1                                                                                                            
                                    text_color:(1,1,1,1)
                                    text:"Calculate"
                                    on_release:root.Twos()
                                    md_bg_color:app.theme_cls.primary_color
                                MDFlatButton:
                                    pos_hint:{"center_x":.5}
                                    text:"Clear"
                                    size_hint:.2,.1                                                                                                          
                                    text_color:(1,1,1,1)
                                    md_bg_color:app.theme_cls.primary_color
                                    on_release:root.clearTwoTwos()
                        Tab:
                            id:tabs
                            text:"tens"
                            BoxLayout:
                                size_hint:.8,.5
                                pos_hint:{"center_x":.5,"center_y":.64}
                                orientation:"vertical"
                                spacing:dp(25)
                                padding:dp(25)
                                MDFlatButton:
                                    pos_hint:{"center_x":.5}
                                    icon:"information"
                                    halign:"center"
                                    size_hint:.2,.1
                                    md_bg_color:app.theme_cls.primary_color
                                    text:"Info"
                                    text_color:(1,1,1,1) 
                                    on_release:root.show_data(obj="Enter the input's base (<37) and the value to be converted. Press calculate to see results.")
                                MDTextField:
                                    hint_text:"Value        "
                                    mode:"rectangle"
                                    md_bg_color:app.theme_cls.primary_color
                                    id:tensvalue
                                    size_hint:.8,.15
                                    pos_hint:{"center_x":.5}
                                MDTextField:
                                    hint_text:"Input base       "
                                    mode:"rectangle"
                                    size_hint:.8,.15
                                    md_bg_color:app.theme_cls.primary_color
                                    id:tensinbase
                                    pos_hint:{"center_x":.5}
                                MDFlatButton:
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    size_hint:.2,.1                                                                                                            
                                    text_color:(1,1,1,1)
                                    text:"Calculate"
                                    on_release:root.Tens()
                                    md_bg_color:app.theme_cls.primary_color
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"Clear"
                                    size_hint:.2,.1                                                                                                          
                                    text_color:(1,1,1,1)  
                                    on_release:root.clearTwoTens()          
                            
            Screen:
                name:"screen4"
                BoxLayout:
                    size_hint:.7,.5
                    pos_hint:{"center_x":.5,"center_y":.6}
                    orientation:"vertical"
                    spacing:dp(20)
                    padding:dp(20)
                    MDFlatButton:
                        pos_hint:{"center_x":.5}
                        halign:"center"
                        md_bg_color:app.theme_cls.primary_color
                        size_hint:.2,.07
                        text:"Info"
                        text_color:(1,1,1,1) 
                        on_release:root.show_truths_information(obj=True)
                    MDTextField:
                        hint_text:"Variables    "
                        mode:"rectangle"
                        id:variablestring
                        pos_hint:{"center_x":.5}
                        size_hint:.8,.1
                    MDTextField:
                        hint_text:"Formulas     "
                        mode:"rectangle"
                        id:formulastring
                        pos_hint:{"center_x":.5}
                        size_hint:.8,.1
                    MDFlatButton:
                        text:"Generate"
                        pos_hint:{"center_x":.5}
                        size_hint:.2,.07
                        text_color:(1,1,1,1)
                        md_bg_color:app.theme_cls.primary_color
                        on_press:root.truthtables_solve()
                        on_release:root.show_truths(obj=True)
                    MDFlatButton:
                        md_bg_color:app.theme_cls.primary_color
                        text:"Clear"
                        icon:"braille"
                        size_hint:.2,.07
                        text_color:(1,1,1,1)
                        pos_hint:{"center_x":.5}
                        on_release:root.truthtables_clear()
            Screen:
                name:"screen5"
                BoxLayout:
                    size_hint:.7,.4
                    pos_hint:{"center_x":.5,"center_y":.6}
                    orientation:"vertical"
                    spacing:dp(20)
                    padding:dp(20)
                    MDFlatButton:
                        pos_hint:{"center_x":.5}
                        text:"Info"
                        halign:"center"
                        size_hint:.2,.07
                        md_bg_color:app.theme_cls.primary_color
                        text_color:(1,1,1,1) 
                        on_release:root.show_data(obj="Input string in the text input field and press encode to see results.")
                    MDTextField:
                        id:runlengthstring
                        mode:"rectangle"
                        size_hint:.8,.1
                        pos_hint:{"center_x":.5}
                        md_bg_color:app.theme_cls.primary_color
                        hint_text:"String to be encoded                                     "
                    MDFlatButton:
                        text:"Encode"
                        text_color:(1,1,1,1)
                        pos_hint:{"center_x":.5}
                        size_hint:.2,.07
                        md_bg_color:app.theme_cls.primary_color
                        on_release:root.run_length()
                    MDFlatButton:
                        text:"Clear"
                        icon:"braille"
                        text_color:(1,1,1,1)
                        pos_hint:{"center_x":.5}
                        size_hint:.2,.07
                        md_bg_color:app.theme_cls.primary_color
                        on_release:root.runlength_clear()
            
            Screen:                
                name:"screen7"
                BoxLayout:
                    size_hint:.7,.4
                    pos_hint:{"center_x":.5,"center_y":.6}
                    orientation:"vertical"
                    spacing:dp(20)
                    padding:dp(20)
                    MDFlatButton:
                        pos_hint:{"center_x":.5}
                        halign:"center"
                        size_hint:.2,.07
                        text:"Info"
                        text_color:(1,1,1,1) 
                        md_bg_color:app.theme_cls.primary_color
                        on_release:root.show_boolean(obj=True)
                    MDTextField:
                        pos_hint:{"center_x":.5}
                        mode:"rectangle"
                        hint_text:"Expression                   "
                        id:simplifier_text
                        size_hint:.8,.1
                    MDFlatButton:
                        text:"Simplify"
                        text_color:(1,1,1,1)
                        pos_hint:{"center_x":.5}
                        size_hint:.2,.07
                        md_bg_color:app.theme_cls.primary_color
                        on_release:root.simplifier()
                    MDFlatButton:
                        text:"Clear"
                        text_color:(1,1,1,1)
                        md_bg_color:app.theme_cls.primary_color
                        pos_hint:{"center_x":.5}
                        size_hint:.2,.07
                        on_release:root.simplify_clear()

        MDNavigationDrawer:
            id:nav_drawer
            orientation:"vertical"
            BoxLayout:  
                pos_hint:{"center_x":.5,"center_y":.3}
                orientation:"vertical"
                spacing:dp(20)
                padding:dp(30)
                size_hint:.8,.8
                ScrollView:
                    MDList:
                        OneLineListItem:
                            on_release:nav_drawer.toggle_nav_drawer()
                            on_press:screen_manager.current="screen3"           
                            text:"ASCII"
                        OneLineListItem:
                            on_press:screen_manager.current="screen1"
                            on_release:nav_drawer.toggle_nav_drawer()
                            text:"Bases"
                        OneLineListItem:
                            on_release:nav_drawer.toggle_nav_drawer()
                            on_press:screen_manager.current="screen7"           
                            text:"Boolean Simplifier"
                        OneLineListItem:
                            on_release:nav_drawer.toggle_nav_drawer()
                            on_press:screen_manager.current="screen2"
                            text:"Complements"
                        OneLineListItem:
                            on_release:nav_drawer.toggle_nav_drawer()
                            on_press:screen_manager.current="screen5"           
                            text:"Runlength Encoding"
                        OneLineListItem:
                            on_release:nav_drawer.toggle_nav_drawer()
                            on_press:screen_manager.current="screen4"           
                            text:"Truth Tables"
                        OneLineListItem:
                            on_release:nav_drawer.toggle_nav_drawer()
                            on_press:root.show_data(obj="Each of the available applications have a specific guide when you open them (i). Use the guide to see how you can use the application.")
                            text:"General guide"
                   
    BoxLayout:
        orientation:"horizontal"
        MDFlatButton:
            text_color:(1,1,1,1)
            text_style:"Button"
            md_bg_color:app.theme_cls.primary_color
            on_release:nav_drawer.toggle_nav_drawer()
            #on_press:root.nav_drawer_manager(1)
            text:"+"
	        halign:"center"
            size_hint:.018475,.02875    
<Tab>:
    MDLabel:
        md_bg_color:app.theme_cls.primary_color
        halign:"center"
        id:label
        font_size:0

<Popup>:
    MDLabel:
        text:"Guide"

<Content>:
    textfield:textfield
    orientation:"vertical"
    MDTextField:
        id:textfield

'''
import numpy as np

def seperator(evaland):
    try:
        evaland = evaland[:-1]
        evaland = evaland[1:]
        evaland = evaland.split(",")
        return evaland
    except:
        return

def alfer(charr,base):
    try:
        out = 0
        llist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        if charr in llist:
            out = int(charr,base)
            out = float(out)
        else:
            out = float(charr)
        return out
    except:
        return

def b2t(value,base):
    neg  = False
    try:
        switch = 0
        add = 0
        basebat = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}
        if str(value)[0]=="-":
            neg = True
            value = float(str(value)[1::])
        for i1 in range(len(str(value))):
            if str(value)[i1]!='.':
                if str(value)[i1] in basebat:
                    if basebat[str(value)[i1]] >=base and str(value)[i1]!='.':
                        return 'error'
                else:
                    if i1==0 and str(value)[i1]=="-":
                        neg=True
                        continue
                    if float(str(value)[i1]) >= base and str(value)[i1]!='.':
                        return 'error'  
        len1 = len(str(value)[:(str(value).find('.'))])
        for i in range(0,len(str(value))):
            if str(value)[i] == '.':
                switch = 1
                len1 = 0
                continue
            if switch==0:
                len1-=1
                add=add+float(alfer((str(value)[i]),base))*(base**len1)
            if switch==1:
                len1-=1
                add=add+float(alfer((str(value)[i]),base))*(base**len1)
        if neg==False:
            return str(add)
        else:
            return "-"+str(add)
    except:
        return

def rep(llist):
    try:
        out = ''
        outlist = []
        i = -1
        for string in llist:
            out+=str(string)
        while i == -1 and len(out)>5:
            i = (out+out).find(out,1,-1)
            if i!=-1:
                return True
            out=out[1:]
        return False
    except:
        return

def outer(charr,base):
    try:
        mapper = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}
        if float(charr)>=10:
            for value in mapper:
                if float(charr) == int(value,base):
                    return value
        else:
            return int(charr)
    except:
        return

def t2b(value,base): 
    neg = False
    try:
        value = float(value)    
        llistrep = []
        llist = []
        if str(value)[0] == '0' or str(value)[0] == "-":
            if str(value)[0] == "-":
                value = float(str(value)[1::])
                neg = True
            while value != 0 or rep(llistrep) == False:
                value = round(value * base,6)
                llist.append(outer(str(value)[:str(value).find(".")],base))
                llistrep.append(outer(str(value)[:str(value).find('.')],base))
                value = float(str(value).replace(str(value)[:str(value).find('.')],"0",1))
                if value==0 or rep(llistrep)==True or len(llist)>18:
                    break
        out = "0."
        for value in llist:
            out+=str(value)
        if neg==False:
            return out
        elif neg==True:
            return "-"+out
    except:
        return

def evaluator(value):
    try:
        for i in range(len(value)):
            if (value[i]=='+' or value[i]=='-' or value[i]=='/' or value[i]=='*') and i!=0 and i!=len(value)-1:
                return str(eval(value))
        return str(value)
    except:
        return

def fraction(value):
    try:
        for i in range(len(value)):
            if value[i]=='.' and i!=0 and i!=len(value):
                return True
        return False
    except:
        return          

multiplicationstrings = []
addstrings = []
addstringsrowscols = []
multiplicationstringsrowscols = []
veccrossstrings=[]
vecdotstrings=[]
vecprojectionstrings=[]
vecbetweenstrings=[]
nav_drawer1_open = False
nav_drawer_open = False
variablestrings = []
formulastrings = []
truths = ""

def make_table(table,list_1,list_2):
    try:
        table = table.replace("    ","      ")
        table = table.replace("-"," ")
        table = table.replace("+"," ")
        table = table.replace("|"," ")
        return table
    except:
        return

class Widgets(Widget):
    pass

class TwoWindow(Screen):
    entry = ObjectProperty(None)
    entry1 = ObjectProperty(None)
    pop1 = ObjectProperty(None)
    inbase = ObjectProperty(None)
    outbase = ObjectProperty(None)
    value = ObjectProperty(None)
    tensvalue = ObjectProperty(None)
    tensinbase = ObjectProperty(None)
    asciivalue = ObjectProperty(None)
    nav_drawer =  ObjectProperty(None)
    nav_drawer1 = ObjectProperty(None)
    formulastring = ObjectProperty(None)
    variablestring = ObjectProperty(None)
    runlengthstring = ObjectProperty(None)
    simplifier_text = ObjectProperty(None)

    def nav_drawer_manager(self,order):
        global nav_drawer_open
        global nav_drawer1_open
        if order == 1:
            nav_drawer_open = True
            if nav_drawer1_open == True:
                self.nav_drawer1.toggle_nav_drawer()
                nav_drawer1_open = False
        elif order == 2:
            nav_drawer1_open = True

    def clearOne(self):
        self.inbase.text = ""
        self.outbase.text = ""
        self.value.text = ""

    def runlength_clear(self):
        self.runlengthstring.text = ""

    def clearTwoTwos(self):
        self.entry.text = ""
        self.entry1.text = ""
        self.pop1.text = ""
    
    def clearTwoTens(self):
        self.tensvalue.text = ""
        self.tensinbase.text = ""

    def clearThree(self):
        self.asciivalue.text = ""

    def variablestrings_load(self):
        global variablestrings
        variablestrings.append(self.variablestring.text)
    
    def formulastrings_load(self):
        global formulastrings
        formulastrings.append(self.formulastring.text)

    def truthtables_clear(self):
        self.variablestring.text=""
        self.formulastring.text=""

    def simplify_clear(self):
        self.simplifier_text.text = ""
        
    def converter(self):
        try:
            neg = False
            oct2 = ''
            oct1 = ''
            alfabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            inbase = self.inbase
            value = self.value
            outbase = self.outbase
            value.text = evaluator(value.text)
            if fraction(value.text)==True: 
                if value.text[0] == "0" or value.text[0] == "-":
                    oct2 = value.text
                    oct22 = 0
                    oct22 = b2t(oct2,int(inbase.text))
                    if oct22[0]=="-":
                        neg=True
                    if oct22=="error":
                        self.value.text = "This value is not a base {} value".format(inbase.text)
                        return 1
                    else:
                        if int(outbase.text)==10:
                            self.value.text = oct22
                            oct1 = oct22
                            return 1
                        else:
                            oct1 = t2b(oct22,int(outbase.text))
                            self.value.text = oct1
                            return 1 
                else:
                    oct2 = (value.text).replace((value.text)[:(value.text).find(".")],"0",1)
                    oct22 = b2t(oct2,int(inbase.text))
                    value.text = (value.text)[:(value.text).find(".")]  
                    if oct22[0]=="-":
                        neg=True                  
                    if oct22=="error":
                        self.value.text = "This value is not a base {} value".format(inbase.text)
                    else:
                        if int(outbase.text)!=10:
                            oct1 = t2b(oct22,int(outbase.text))
                        else:
                            oct1 = oct22
            if int(inbase.text)!=-1:
                for i in range(len(value.text)):
                    try:
                        if i == 0 and value.text[i] == "-":
                            neg = True
                            pass
                        else:
                            apps = int(value.text[i],int(inbase.text))
                    except:
                        self.value.text = "This value is not a base {} value".format(inbase.text)
                        return 0
            
                if  int(outbase.text) == 10:
                    out = int(value.text,int(inbase.text))
                    self.value.text = str(out)+oct1[1:]
                else:
                    import string
                    digs = string.digits + string.ascii_uppercase
                    value = int(value.text,int(inbase.text))
                    inbase = 10
                    outbase = int(outbase.text)
                    if value < 0:
                        sign = -1
                    if value == 0:
                        return digs[0]
                    else:
                        sign = 1
                    value*= sign
                    digits = []

                    while value:
                        digits.append(digs[int(value % outbase)])
                        value = int(value / outbase)
                    if sign < 0:
                        digits.append('-')
                    digits.reverse()
                    if neg==True:
                        self.value.text = "-"+str(''.join(digits))+oct1[1:]
                    else:    
                        self.value.text = str(''.join(digits))+oct1[1:]
        except:
            return

    
    def Twos(self):
        neg = False
        try:
            apps=0
            for i in range(len(self.entry.text)):
                try:
                    if self.entry.text[i]!='-':
                        apps = int(self.entry.text[i],int(self.pop1.text))
                except:
                    self.entry.text = "This value is not a base {} value".format(self.pop1.text)
                    return 0
            apps1 = int(self.entry.text,int(self.pop1.text))
            
            if apps1>(2**(int(self.entry1.text)-1))-1 or apps1<-2**(int(self.entry1.text)-1):
                self.entry.text="Input requires greater bits"
                return 0

            bits = self.entry1.text 
            outbase = 2
            pop = int(self.entry.text,int(self.pop1.text))
            if self.entry.text[0]=="-":
                value = 2**(int(bits))-(abs(pop))
            else:
                value = abs(pop)
            import string
            digs = string.digits + string.ascii_uppercase
            if value < 0:
                sign = -1
            elif value == 0:
                return digs[0]
            else:
                sign = 1

            value*= sign
            digits = []

            while value:
                digits.append(digs[int(value % outbase)])
                value = int(value / outbase)
            if sign < 0:
                digits.append('-')
            digits.reverse()
            out = str(''.join(digits))
            ad = ''
            if len(out)<int(bits):
                for i in range(int(bits)-len(out)):
                    ad = ad + '0'
                out = ad + out
                self.entry.text = out
            elif len(out)==int(bits):
                self.entry.text = out
        except:
            return

    def Tens(self):
        try:
            inbase = self.tensinbase
            entry = self.tensvalue
            num = len(self.entry.text)
            for i in range(len(entry.text)):
                try:
                    if self.tensvalue.text[i]!='-':
                        apps = int(entry.text[i],int(inbase.text))
                except:
                    self.tensvalue.text = "This value is not a base {} value".format(inbase.text)
                    return 0
            entry.text = str(int(entry.text,int(inbase.text)))
            num = len(entry.text)
            if int(entry.text)<0:
                self.tensvalue.text = str((10**(num-1))-abs(int(entry.text)))
            elif int(entry.text)>0:
                self.tensvalue.text = str((10**(num))-abs(int(entry.text)))
        except:
            return

    
    asciiDICT = {'NULL':0,'SOH':1,'STX':2,'ETX':3,'EQT':4,'ENQ':5,'ACK':6,'BEL':7,'BS':8,'TAB':9,'LF':10,'VT':11,'FF':12,'CR':13,'SO':14,'SI':15,'DLE':16,'DC1':17,'DC2':18,'DC3':19,'DC4':20,'NAK':21,'SYN':22,'ETB':23,'CAN':24,'EM':25,'SUB':26,'ESC':27,'FS':28,'GS':29,'RS':30,'US':31,'Space':32,'DEL':127}
    def conv(self,outbase):
        try:
            if self.asciivalue.text == "NULL":
                self.asciivalue.text = '0000'
            elif self.asciivalue.text in self.asciiDICT:
                value = self.asciiDICT[self.asciivalue.text]
                try:
                    import string
                    digs = string.digits + string.ascii_uppercase
                    if value < 0:
                        sign = -1
                    elif value == 0:
                        return digs[0]
                    else:
                        sign = 1

                    value*= sign
                    digits = []

                    while value:
                        digits.append(digs[int(value % outbase)])
                        value = int(value / outbase)
                    if sign < 0:
                        digits.append('-')
                    digits.reverse()
                    self.asciivalue.text = str(''.join(digits))
                except:
                    return

            else:
                try:
                    value = ord(self.asciivalue.text)
                    import string
                    digs = string.digits + string.ascii_uppercase
                    if value < 0:
                        sign = -1
                    elif value == 0:
                        return digs[0]
                    else:
                        sign = 1

                    value*= sign
                    digits = []

                    while value:
                        digits.append(digs[int(value % outbase)])
                        value = int(value / outbase)
                    if sign < 0:
                        digits.append('-')
                    digits.reverse()
                    self.asciivalue.text = str(''.join(digits))
                except:
                    return

        except:
            return

    def truthtables_solve(self):
        try:
            global truths
            if self.variablestring.text == "" or self.formulastring.text=="":
                return
            list_2 = seperator(self.formulastring.text)
            list_1 = seperator(self.variablestring.text)
            truths = ttg.Truths(list_1,list_2)
        except:
            return

    def show_truths(self,obj):
        try:
            global truths
            list_2 = seperator(self.formulastring.text)
            list_1 = seperator(self.variablestring.text)
            if self.variablestring.text == "" or self.formulastring.text== "":
                return
            truths1 = make_table(str(truths),list_1,list_2)
            self.dialog = MDDialog(text=truths1,size_hint=(0.99,0.99), buttons=[MDFlatButton(text="Close", on_release=self.close_dialog)])
            self.dialog.open()
        except:
            return

    def show_truths_information(self,obj):
        self.dialog = MDDialog(text="An example of how variables should be entered:\n\n[a, b, ... ]\n\nAn example of how formulas should be entered:\n\n[~a and b, a or b, a or ( a xor b), (~a and b) => (a or b), ... ]\n\nUse:\n\n~ for not\n=> for implies\n= for biconditional implications\nnand for nand\nxor for xor\nnor for nor\nor for or\nand for and\n\nConsider using parantheses to specify precedence.", size_hint=(.8,.8), buttons=[MDFlatButton(text="Close", on_release=self.close_dialog)])
        self.dialog.open()
    
    def run_length(self):
        try:
            i = 0
            if self.runlengthstring.text == "":
                return
            string = self.runlengthstring.text
            while i<len(string)-1:
                char = string[i]
                count = 1
                next_char = string[i+1]
                repeated_string = char 
                j = i + 1
                while next_char == char:
                    count = count + 1
                    repeated_string+=char
                    j+=1
                    if j > len(string)-1:
                        break
                    next_char = string[j]
                if count>=3:
                    string = string.replace(repeated_string,"*"+str(count)+char,1)
                    i = j - (count-3)
                else:
                    i = i + len(repeated_string) 
                repeated_string = ""
            if self.runlengthstring.text == string:
                self.runlengthstring.text="String is already at its smallest"
            else:
                self.runlengthstring.text = string
        except:
            return

    def simplifier(self):
        try:
            algebra = boolean.BooleanAlgebra()
            self.simplifier_text.text = str(algebra.parse(self.simplifier_text.text).simplify())
        except:
            expr = self.simplifier_text.text
            if self.simplifier_text.text == "":
                return
            if ("nand" or "NAND" or "Nand" in expr) or ("nor" or "Nor" or "NOR" in expr) or ("xor" or "Xor" or "XOR" in expr or "xnor"):
                TwoWindow.show_boolean(self,obj=True)
        return

    def show_data(self,obj):
        self.dialog = MDDialog(text=obj, size_hint=(.5,.9), buttons=[MDFlatButton(text="Close", on_release=self.close_dialog)])
        self.dialog.open()

    def show_boolean(self,obj):
        self.dialog = MDDialog(text="Enter the boolean expression (e.g a or a and b) in the text field. Then press simplify to see results.\n\nHere you can use:\n~ for not\n& for and\n| for or\n\nIf you have an xor, a nand or a nor:\n\nExpress them in terms of and, or and not gates.\na nor b = ~a and ~b (de morgan)\na nand b = ~a or ~b (de morgan)\na xor b = a and ~b or ~a and b", size_hint=(.5,.9), buttons=[MDFlatButton(text="Close", on_release=self.close_dialog)])
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()
    
class Tab(FloatLayout, MDTabsBase):
    pass

class WindowManager(ScreenManager):
    pass

sm = ScreenManager()
sm.add_widget(TwoWindow(name = "two"))

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Orange"
        self.help_str = Builder.load_string(helper_string)
        screen.add_widget(self.help_str)
        self.title = "Computaxion"
        self.theme_cls.theme_style = "Dark"
        return screen
        
    def on_start(self):
        self.help_str.get_screen("two").ids.tabs.add_widget(Tab())
        self.help_str.get_screen("two").ids.tabs.add_widget(Tab())

    def on_tab_switch(self,instance_tabs,instance_tab,instance_tab_label,tab_text):
        instance_tab.ids.label.text = tab_text

MainApp().run()