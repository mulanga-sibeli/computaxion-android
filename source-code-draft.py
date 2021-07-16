from kivy.config import Config
Config.set("graphics","resizeable", True)
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.behaviors import RectangularElevationBehavior, RectangularRippleBehavior, BackgroundColorBehavior
from kivymd.font_definitions import theme_font_styles
from kivy.uix.scrollview import ScrollView
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem
from kivy.core.window import Window
from kivymd.uix.button import MDRectangleFlatButton, MDRectangleFlatIconButton, MDFlatButton, MDIconButton
import numpy as np
import ast
import string
import math



helper_string = '''
ScreenManager:
    OneWindow:
    TwoWindow:

<OneWindow>:
    name:'one'
    BoxLayout:
        spacing:20
        orientation:"vertical"
        pos_hint:{"center_x":.5,"center_y":.5725}
        size_hint:.9,.4
        Image:
            source:"brainlogo.png"
            pos_hint:{"center_x":.5,"center_y":.5}
            size_hint:1,.99
        MDRectangleFlatButton:
            pos_hint:{"center_x":.5,"center_y":.5}
            text:"Important Information"
            size_hint:.7,.35
            on_release:root.show_data0(obj="The next window contains a (+) button that you can use to open and close the drawer which contains more functionalities that the app offers.")
        MDRectangleFlatButton:
            text:"Continue"
            pos_hint:{"center_x":0.5}
            on_release:root.manager.current="two"
            size_hint:.7,.35
	
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
    solverows:solverows
    solvecols:solvecols
    inverserows:inverserows
    inversecols:inversecols
    multiplicationrows:multiplicationrows
    multiplicationcols:multiplicationcols
    addrows:addrows
    addcols:addcols
    solvestring:solvestring
    inversestring:inversestring
    multiplicationstring:multiplicationstring
    addstring:addstring
    rankrows:rankrows
    rankcols:rankcols
    rankstring:rankstring
    determinantrows:determinantrows
    determinantcols:determinantcols
    determinantstring:determinantstring
    bee:bee
    vecsolvestring:vecsolvestring
    vecdotstring:vecdotstring
    vecprojectionstring:vecprojectionstring
    vecmagnitudestring:vecmagnitudestring
    vecnormstring:vecnormstring
    vecdirectionstring:vecdirectionstring
    vecbetweenstring:vecbetweenstring
    screen_manager:screen_manager
    NavigationLayout:
        
        ScreenManager:
            id:screen_manager
            Screen:
                name:"screen4"
                BoxLayout:
                    orientation:"vertical"
                    MDTabs:
                        size_hint:1,1
                        pos_hint:{"center_x":.5}
                        size:"32dp","32dp"    
                        id:tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        Tab:
                            id:tabs
                            text:"solving matrices"  
                            BoxLayout:
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(8)
                                size_hint:.8,.8
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"A in Ax=B                                "
                                    halign:"center"
                                    multiline:True
                                    id:solvestring
                                    pos_hint:{"center_x":.5,"center_y":.8} 
                                    size_hint:1,.7
                                GridLayout:
                                    size_hint:1,.15
                                    rows:1
                                    cols:2
                                    spacing:100
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Rows                             "
                                        id:solverows
                                        size_hint:1,.2
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Columns                              "
                                        id:solvecols
                                        size_hint:1,.2
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"B in Ax=B                                "
                                    id:bee
                                    pos_hint:{"center_x":.5}
                                    size:"120sp","30sp"
                                    halign:"center"
                                    size_hint:1,.2
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    icon:"braille"
                                    halign:"center"
                                    size_hint:1,.1                                                                                                            
                                    text_style:"Button"
                                    text:"CALCULATE"
                                    on_release:root.solve()
                                    pos_hint:{"center_x":.5}
                                MDFlatButton:
                                    icon:"braille"
                                    halign:"center"
                                    pos_hint:{"center_x":.5}
                                    text:"CLEAR"
                                    text_color:(1,1,1,1)
                                    size_hint:1,.1                                                                                                          
                                    text_style:"Button"
                                    on_release:root.solveclear()
                                    md_bg_color:app.theme_cls.primary_color
                                MDFlatButton:
                                    text:"INFO"
                                    halign:"center"
                                    pos_hint:{"center_x":.5}
                                    text_style:"Button"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    size_hint:1,.1
                                    on_release:root.show_data1(obj=True)
                        Tab:
                            id:tabs
                            text:"products"
                            BoxLayout:
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(10)
                                size_hint:.8,.8
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Input matrix                             "
                                    pos_hint:{"center_x":.5,"center_y":.8}
                                    halign:"center"
                                    size_hint:1,.8
                                    multiline:True
                                    id:multiplicationstring
                                GridLayout:
                                    cols:2
                                    rows:1
                                    size_hint:1,.1875
                                    spacing:100
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Rows                             "
                                        id:multiplicationrows
                                        size_hint:1,.12
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Columns                             "
                                        id:multiplicationcols
                                        size_hint:1,.12
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    pos_hint:{"center_x":.5}
                                    text:"LOAD"
                                    icon:"braille"
                                    size_hint:1,.1
                                    on_release:root.multiplicationload()
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    icon:"braille"
                                    pos_hint:{"center_x":.5}
                                    halign:"center"                                                                                                            
                                    text_style:"Button"
                                    text:"CALCULATE"
                                    on_release:root.mul()
                                    size_hint:1,.1  
                                MDFlatButton:
                                    size_hint:1,.1   
                                    icon:"braille"
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"CLEAR"      
                                    text_color:(1,1,1,1)
                                    md_bg_color:app.theme_cls.primary_color                                                                                                     
                                    text_style:"Button"
                                    on_release:root.multiplicationclear()
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    text:"INFO"
                                    halign:"center"
                                    pos_hint:{"center_x":.5}
                                    text_style:"Button"
                                    size_hint:1,.1
                                    on_release:root.show_data2(obj=True)
                        Tab:
                            id:tabs
                            text:"add"
                            BoxLayout:
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(10)
                                size_hint:.8,.8
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Input matrix                             "
                                    pos_hint:{"center_x":.5,"center_y":.8}
                                    halign:"center"
                                    size_hint:1,.8
                                    multiline:True
                                    id:addstring
                                GridLayout:
                                    cols:2
                                    rows:1
                                    spacing:100
                                    size_hint:1,.1875
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Rows                             "
                                        size_hint:1,.12
                                        id:addrows
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Columns                              "
                                        id:addcols
                                        size_hint:1,.12
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    size_hint:1,.1
                                    text:"LOAD"
                                    pos_hint:{"center_x":.5}
                                    on_release:root.addload()
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    size_hint:1,.1                                                                                                          
                                    text_style:"Button"
                                    text:"CALCULATE"
                                    on_release:root.add()
                                MDFlatButton:
                                    icon:"braille"
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"CLEAR"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    size_hint:1,.1                                                                                                           
                                    text_style:"Button"      
                                    on_release:root.addclear()
                                MDFlatButton:
                                    text:"INFO"
                                    halign:"center"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    pos_hint:{"center_x":.5}
                                    text_style:"Button"
                                    size_hint:1,.1
                                    on_release:root.show_data2(obj=True)
                        Tab:
                            id:tabs
                            text:"inverses"
                            BoxLayout:
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(10)
                                size_hint:.8,.8
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Input matrix                             "
                                    pos_hint:{"center_x":.5,"center_y":.8}
                                    halign:"center"
                                    size_hint:1,.8
                                    multiline:True
                                    id:inversestring
                                GridLayout:
                                    cols:2
                                    rows:1
                                    spacing:100
                                    size_hint:1,.1875
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Rows                             "
                                        id:inverserows
                                        size_hint:1,.12
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Columns                              "
                                        id:inversecols
                                        size_hint:1,.12
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    icon:"braille"
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    size_hint:1,.1                                                                                                           
                                    text_style:"Button"
                                    text:"CALCULATE"
                                    on_release:root.inv()
                                MDFlatButton:
                                    icon:"braille"
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"CLEAR"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    size_hint:1,.1                                                                                                          
                                    text_style:"Button" 
                                    on_release:root.inverseclear()
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    text:"INFO"
                                    halign:"center"
                                    pos_hint:{"center_x":.5}
                                    text_style:"Button"
                                    size_hint:1,.1
                                    on_release:root.show_data3(obj=True)
                        Tab:
                            id:tabs
                            text:"determinant"
                            BoxLayout:
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(10)
                                size_hint:.8,.8
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Input matrix                             "
                                    pos_hint:{"center_x":.5,"center_y":.8}
                                    halign:"center"
                                    size_hint:1,.8
                                    multiline:True
                                    id:determinantstring
                                GridLayout:
                                    cols:2
                                    rows:1
                                    spacing:100
                                    size_hint:1,.1875
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Rows                             "
                                        id:determinantrows
                                        size_hint:1,.12
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Columns                              "
                                        id:determinantcols
                                        size_hint:1,.12
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    size_hint:1,.1                                                                                                           
                                    text_style:"Button"
                                    text:"CALCULATE"
                                    on_release:root.det()
                                MDFlatButton:
                                    icon:"braille"
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"CLEAR"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    size_hint:1,.1                                                                                                           
                                    text_style:"Button"
                                    on_release:root.determinantclear()
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    text:"INFO"
                                    halign:"center"
                                    pos_hint:{"center_x":.5}
                                    text_style:"Button"
                                    size_hint:1,.1
                                    on_release:root.show_data3(obj=True)
                        Tab:
                            id:tabs
                            text:"rank"
                            BoxLayout:
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(10)
                                size_hint:.8,.8
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Input matrix                             "
                                    pos_hint:{"center_x":.5,"center_y":.8}
                                    halign:"center"
                                    size_hint:1,.8
                                    multiline:True
                                    id:rankstring
                                GridLayout:
                                    cols:2
                                    rows:1
                                    spacing:100
                                    size_hint:1,.1875
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Rows                             "
                                        id:rankrows
                                        size_hint:1,.12
                                    MDTextField:
                                        mode:"rectangle"
                                        hint_text:"Columns                              "
                                        id:rankcols
                                        size_hint:1,.12
                                MDFlatButton:
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    size_hint:1,.1                                                                                                         
                                    text_style:"Button"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    text:"CALCULATE"
                                    on_release:root.ran()
                                MDFlatButton:
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"CLEAR"
                                    text_color:(1,1,1,1)
                                    md_bg_color:app.theme_cls.primary_color
                                    size_hint:1,.1                                                                                                           
                                    text_style:"Button"
                                    on_release:root.rankclear()    
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    text:"INFO"
                                    halign:"center"
                                    pos_hint:{"center_x":.5}
                                    text_style:"Button"
                                    size_hint:1,.1
                                    on_release:root.show_data3(obj=True)
            Screen:
                name:"screen1"
                BoxLayout:
                    size_hint:.65,.65
                    pos_hint:{"center_x":.5,"center_y":.6}
                    orientation:"vertical"
                    spacing:dp(20)
                    padding:dp(20)
                    MDTextField:
                        mode:"rectangle"
                        id:inbase
                        hint_text:"Input's base                             "
                        md_bg_color:app.theme_cls.primary_color
                        size_hint:.8,.2
                        pos_hint:{"center_x":.5}
                    MDTextField:
                        mode:"rectangle"
                        id:outbase
                        hint_text:"Output's base                                "
                        md_bg_color:app.theme_cls.primary_color
                        size_hint:.8,.2
                        pos_hint:{"center_x":.5}
                    MDTextField:
                        id:value
                        hint_text:"Value                                "
                        mode:"rectangle"
                        md_bg_color:app.theme_cls.primary_color
                        size_hint:.8,.2
                        pos_hint:{"center_x":.5}
                    MDFlatButton:
                        md_bg_color:app.theme_cls.primary_color
                        text_color:(1,1,1,1)
                        icon:"braille"
                        halign:"center"                                                                                                          
                        text_style:"Button"
                        text:"CONVERT"
                        on_release:root.converter()
                        pos_hint:{"center_x":.5}
                        size_hint:.8,.1
                    MDFlatButton:
                        md_bg_color:app.theme_cls.primary_color
                        text_color:(1,1,1,1)
                        icon:"braille"
                        halign:"center"
                        text:"CLEAR"                                                                                                           
                        text_style:"Button"
                        on_release:root.clearOne()
                        pos_hint:{"center_x":.5} 
                        size_hint:.8,.1  
                    MDFlatButton:
                        md_bg_color:app.theme_cls.primary_color
                        text_color:(1,1,1,1)
                        halign:"center"
                        text_style:"Button"
                        text:"INFO"
                        pos_hint:{"center_x":.5}
                        on_release:root.show_data(obj="Restriction: Input base and Output base should both be less than 37.")
                        size_hint:.8,.1      
                             
            Screen:
                name:"screen2"
                BoxLayout:
                    orientation:"vertical"
                    MDTabs:
                        size_hint:1,1
                        pos_hint:{"center_x":.5}
                        size:"10dp","10dp"
                       
                        id:tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        Tab:
                            id:tabs
                            text:"twos"           
                            BoxLayout:
                                size_hint:.7,.7
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(20)
                                padding:dp(20)
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Value                                "
                                    md_bg_color:app.theme_cls.primary_color
                                    id:entry
                                    size_hint:.8,.23
                                    pos_hint:{"center_x":.5}
                                MDTextField:
                                    hint_text:"Input's base                             "
                                    mode:"rectangle"
                                    md_bg_color:app.theme_cls.primary_color
                                    id:pop1
                                    size_hint:.8,.23
                                    pos_hint:{"center_x":.5}
                                MDTextField:
                                    hint_text:"Bits                             "
                                    mode:"rectangle"
                                    md_bg_color:app.theme_cls.primary_color
                                    id:entry1
                                    size_hint:.8,.23
                                    pos_hint:{"center_x":.5}
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    icon:"braille"
                                    text_color:(1,1,1,1)
                                    halign:"center"                                                                                                        
                                    text_style:"Button"
                                    text:"CALCULATE"
                                    on_release:root.Twos()
                                    pos_hint:{"center_x":.5}
                                    size_hint:.8,.15
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    icon:"braille"
                                    halign:"center"
                                    text:"CLEAR"                                                                                                        
                                    text_style:"Button"
                                    pos_hint:{"center_x":.5}
                                    on_release:root.clearTwoTwos()
                                    size_hint:.8,.15
                                MDFlatButton:
                                    text_color:(1,1,1,1)
                                    md_bg_color:app.theme_cls.primary_color
                                    text:"INFO"
                                    halign:"center"
                                    text_style:"Button"
                                    pos_hint:{"center_x":.5,"center_y":.5}
                                    on_release:root.show_data(obj="Input can be of any base below 37, the outcome will be representation in twos complement.")
                                    size_hint:.8,.15                
                        Tab:
                            id:tabs
                            text:"tens"
                            BoxLayout:
                                size_hint:.6,.6
                                pos_hint:{"center_x":.5,"center_y":.64}
                                orientation:"vertical"
                                spacing:dp(25)
                                MDTextField:
                                    hint_text:"Value                                "
                                    mode:"rectangle"
                                    md_bg_color:app.theme_cls.primary_color
                                    id:tensvalue
                                    size_hint:.8,.2
                                    pos_hint:{"center_x":.5}
                                MDTextField:
                                    hint_text:"Input's base                             "
                                    mode:"rectangle"
                                    md_bg_color:app.theme_cls.primary_color
                                    id:tensinbase
                                    size_hint:.8,.2
                                    pos_hint:{"center_x":.5}
                                MDFlatButton:
                                    icon:"braille"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    pos_hint:{"center_x":.5}
                                    halign:"center"                                                                                                        
                                    text_style:"Button"
                                    text:"CALCULATE"
                                    on_release:root.Tens()
                                    size_hint:.8,.1
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    icon:"braille"
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"CLEAR"                                                                                                          
                                    text_style:"Button"  
                                    on_release:root.clearTwoTens()
                                    size_hint:.8,.1
                                MDFlatButton:
                                    text:"INFO"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    halign:"center"
                                    text_style:"Button"
                                    pos_hint:{"center_x":.5}
                                    on_release:root.show_data(obj="Input can be of any base below 37, the outcome will be representation in tens complement.")
                                    size_hint:.8,.1         
            Screen:
                name:"screen3"
                BoxLayout:
                    size_hint:.8,.8
                    pos_hint:{"center_x":.5,"center_y":.5875}
                    orientation:"vertical"
                    spacing:dp(20)
                    padding:dp(35)
                    MDTextField:
                        hint_text:"Character                                "
                        md_bg_color:app.theme_cls.primary_color
                        mode:"rectangle"
                        id:asciivalue
                        pos_hint:{"center_x":.5}
			            size_hint:.8,.2
                    MDRectangleFlatButton:
                        text:"BIN"
                        on_press:root.conv(2)
                        pos_hint:{"center_x":.5}
			            size_hint:.8,.15
                    MDRectangleFlatButton:
                        text:"OCT"
                        on_press:root.conv(8)
                        pos_hint:{"center_x":.5}
                        size_hint:.8,.15
                    MDRectangleFlatButton:
			            size_hint:.8,.15
                        text:"DEC"
                        on_press:root.conv(10)
                        pos_hint:{"center_x":.5}
                    MDRectangleFlatButton:
                        text:"HEX"
                        on_press:root.conv(16)
                        pos_hint:{"center_x":.5}
			            size_hint:.8,.15
                    MDFlatButton:
                        pos_hint:{"center_x":.5}
                        halign:"center" 
                        text:"CLEAR"
                        text_style:"Button"   
                        icon:"braille"
                        on_release:root.clearThree()
			            size_hint:.8,.15
                        text_color:(1,1,1,1)
                        md_bg_color:app.theme_cls.primary_color
                    MDFlatButton:
                        md_bg_color:app.theme_cls.primary_color
                        text:"INFO"
                        halign:"center"
                        text_style:"Button"
                        text_color:(1,1,1,1)
			            size_hint:.8,.15
                        pos_hint:{"center_x":.5}
                        on_release:root.show_data(obj="Input is a character in the ASCII character set (for characters 0-127), then press one of the four available bases to see the character's representation in those bases.")
                          
            
            Screen:
                name:"screen5"
                BoxLayout:
                    orientation:"vertical"
                    MDTabs:
                        size_hint:1,1
                        pos_hint:{"center_x":.5}
                        size:"32dp","32dp"

                        id:tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        Tab:
                            id:tabs
                            text:"general" 
                            BoxLayout:
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(10)
                                size_hint:.8,.8          
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Input vector                             "
                                    pos_hint:{"center_x":.5,"center_y":.8}
                                    halign:"center"
                                    size_hint:1,.8
                                    multiline:True
                                    id:vecsolvestring
                                MDTextField:
                                    mode:"rectangle"
                                    halighn:"center"
                                    md_bg_color:app.theme_cls.primary_color
                                    hint_text:"Magnitude                                "
                                    id:vecmagnitudestring
                                    size_hint:1,.1875
                                MDTextField:
                                    mode:"rectangle"
                                    halighn:"center"
                                    md_bg_color:app.theme_cls.primary_color
                                    hint_text:"Normalized                               "
                                    id:vecnormstring
                                    size_hint:1,.1875
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    size_hint:1,.12                                                                                                            
                                    text_style:"Button"
                                    text:"CALCULATE"
                                    on_release:root.vecsolve()
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"CLEAR"
                                    size_hint:1,.12                                                                                                           
                                    text_style:"Button"
                                    on_release:root.vecsolveclear()
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    text:"INFO"
                                    halign:"center"
                                    pos_hint:{"center_x":.5}
                                    text_style:"Button"
                                    size_hint:1,.12
                                    on_release:root.show_data4(obj=True)
                        Tab:
                            id:tabs
                            text:"projections"
                            BoxLayout:
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(10)
                                size_hint:.8,.8
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Input vector                             "
                                    pos_hint:{"center_x":.5,"center_y":.8}
                                    halign:"center"
                                    size_hint:1,.65
                                    multiline:True
                                    id:vecprojectionstring
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    text:"LOAD"
                                    icon:"braille"
                                    pos_hint:{"center_x":.5}
                                    size_hint:1,.1
                                    on_release:root.vecprojectionload()
                                MDFlatButton:
                                    icon:"braille"
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    size_hint:1,.1
                                    text_color:(1,1,1,1)
                                    md_bg_color:app.theme_cls.primary_color                                                                                                            
                                    text_style:"Button"
                                    text:"CALCULATE"
                                    on_release:root.vecprojectionsolve()
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"CLEAR"
                                    size_hint:1,.1                                                                                                           
                                    text_style:"Button"
                                    on_release:root.vecprojectionclear()
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    text:"INFO"
                                    halign:"center"
                                    pos_hint:{"center_x":.5}
                                    text_style:"Button"
                                    size_hint:1,.1
                                    on_release:root.show_data5(obj=True)
                        Tab:
                            id:tabs
                            text:"dot-products"
                            BoxLayout:
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(10)
                                size_hint:.8,.8
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Input vector                             "
                                    pos_hint:{"center_x":.5,"center_y":.8}
                                    halign:"center"
                                    size_hint:1,.65
                                    multiline:True
                                    id:vecdotstring
                                MDFlatButton:
                                    text:"LOAD"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    size_hint:1,.1
                                    pos_hint:{"center_x":.5}
                                    on_release:root.vecdotload()
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    size_hint:1,.1                                                                                                            
                                    text_style:"Button"
                                    text:"CALCULATE"
                                    on_release:root.dotsolve()
                                MDFlatButton:
                                    text_color:(1,1,1,1)
                                    md_bg_color:app.theme_cls.primary_color
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"CLEAR"
                                    size_hint:1,.1                                                                                                           
                                    text_style:"Button"   
                                    on_release:root.vecdotclear() 
                                MDFlatButton:
                                    text:"INFO"
                                    halign:"center"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    pos_hint:{"center_x":.5}
                                    text_style:"Button"
                                    size_hint:1,.1
                                    on_release:root.show_data5(obj=True)  
                        Tab:
                            id:tabs
                            text:"2d-direction"
                            BoxLayout:
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(10)
                                size_hint:.8,.8  
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Input vector                             "
                                    pos_hint:{"center_x":.5,"center_y":.8}
                                    halign:"center"
                                    size_hint:1,.65
                                    multiline:True
                                    id:vecdirectionstring
                                MDFlatButton:
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    size_hint:1,.1                                                                                                        
                                    text_style:"Button"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    text:"CALCULATE"
                                    on_release:root.vecdirection()
                                MDFlatButton:
                                    text_color:(1,1,1,1)
                                    md_bg_color:app.theme_cls.primary_color
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"CLEAR"
                                    size_hint:1,.1                                                                                                           
                                    text_style:"Button"
                                    on_release:root.vecdirectionclear()
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    text:"INFO"
                                    halign:"center"
                                    pos_hint:{"center_x":.5}
                                    text_style:"Button"
                                    size_hint:1,.1
                                    on_release:root.show_data4(obj=True)  
                        Tab:
                            id:tabs
                            text:"angle betweeen 2d"
                            BoxLayout:
                                pos_hint:{"center_x":.5,"center_y":.6}
                                orientation:"vertical"
                                spacing:dp(10)
                                size_hint:.8,.8   
                                MDTextField:
                                    mode:"rectangle"
                                    hint_text:"Input vector                             "
                                    pos_hint:{"center_x":.5,"center_y":.8}
                                    halign:"center"
                                    size_hint:1,.65
                                    multiline:True
                                    id:vecbetweenstring
                                MDFlatButton:
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    text:"LOAD"
                                    icon:"braille"
                                    size_hint:1,.1
                                    pos_hint:{"center_x":.5}
                                    on_release:root.vecbetweenload()
                                MDFlatButton:
                                    text_color:(1,1,1,1)
                                    md_bg_color:app.theme_cls.primary_color
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    size_hint:1,.1                                                                                                            
                                    text_style:"Button"
                                    text:"CALCULATE"
                                    on_release:root.vecbetween()
                                MDFlatButton:
                                    icon:"braille"
                                    pos_hint:{"center_x":.5}
                                    halign:"center"
                                    text:"CLEAR"
                                    md_bg_color:app.theme_cls.primary_color
                                    text_color:(1,1,1,1)
                                    size_hint:1,.1                                                                                                           
                                    text_style:"Button"
                                    on_release:root.vecbetweenclear()
                                MDFlatButton:
                                    text_color:(1,1,1,1)
                                    md_bg_color:app.theme_cls.primary_color
                                    text:"INFO"
                                    halign:"center"
                                    pos_hint:{"center_x":.5}
                                    text_style:"Button"
                                    size_hint:1,.1
                                    on_release:root.show_data5(obj=True) 
        MDNavigationDrawer:
            id:nav_drawer
            orientation:"vertical"
            BoxLayout:
                orientation:"vertical"
                size_hint:.8,.8
                padding:10
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text:"Matrices"  
                            text_color:app.theme_cls.primary_color 
                            on_release:nav_drawer.toggle_nav_drawer()
                            on_press:screen_manager.current="screen4"
                        OneLineListItem:
                            text:"Vectors"  
                            text_color:app.theme_cls.primary_color 
                            on_release:nav_drawer.toggle_nav_drawer()
                            on_press:screen_manager.current="screen5"
                        OneLineListItem:
                            text:"Bases"  
                            text_color:app.theme_cls.primary_color 
                            on_release:nav_drawer.toggle_nav_drawer()
                            on_press:screen_manager.current="screen1"
                        OneLineListItem:
                            text:"Complements"  
                            text_color:app.theme_cls.primary_color 
                            on_release:nav_drawer.toggle_nav_drawer()
                            on_press:screen_manager.current="screen2"
                        OneLineListItem:
                            text:"Ascii"  
                            text_color:app.theme_cls.primary_color 
                            on_release:nav_drawer.toggle_nav_drawer()
                            on_press:screen_manager.current="screen3"
                        OneLineListItem:
                            text:"GENERAL GUIDE"  
                            text_color:app.theme_cls.primary_color 
                            on_press:root.show_data(obj="Each of the available applications have a guide when you open them (INFO). Use the guide to find out how you can use the application. While working with matrices, vectors and complements, swipe across the screen to move to other applications under those topics.")
        
    BoxLayout:
        orientation:"horizontal"
        MDFlatButton:
            text_color:(1,1,1,1)
	        text_style:"Button"
            md_bg_color:app.theme_cls.primary_color
            on_press:nav_drawer.toggle_nav_drawer()
            text:"+"
	        halign:"center"
            size_hint:.018475,.04275
         


<Tab>:
    MDLabel:
        md_bg_color:app.theme_cls.primary_color
        halign:"center"
        id:label
        font_size:0
'''

class OneWindow(Screen):
    
    def show_data0(self,obj):
        self.dialog = MDDialog(text=obj, size_hint=(.5,.1725), buttons=[MDFlatButton(text="Got it!", on_release=self.close_dialog)])
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

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
        1==1

def b2t(value,base):
    try:
        switch = 0
        add = 0
        basebat = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}
        for i1 in range(len(str(value))):
            if str(value)[i1]!='.':
                if str(value)[i1] in basebat:
                    if basebat[str(value)[i1]] >=base and str(value)[i1]!='.':
                        return 'error'
                else:
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
        return str(add)
    except:
        1==1
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
        1==1

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
        1==1

def t2b(value,base): 
    try:
        value = float(value)    
        llistrep = []
        llist = []
        if str(value)[0]=='0':
            while value!=0 or rep(llistrep)==False:
                value = round(value * base,6)
                llist.append(outer(str(value)[:str(value).find(".")],base))
                llistrep.append(outer(str(value)[:str(value).find('.')],base))
                value = float(str(value).replace(str(value)[:str(value).find('.')],"0",1))
                if value==0 or rep(llistrep)==True or len(llist)>18:
                    break
        out = "0."
        for value in llist:
            out+=str(value)
        return out
    except:
        1==1

def evaluator(value):
    try:
        for i in range(len(value)):
            if value[i]=='+' or value[i]=='-' or value[i]=='/' or value[i]=='*':
                return str(eval(value))
        return str(value)
    except:
        1==1

def fraction(value):
    try:
        for i in range(len(value)):
            if value[i]=='.' and i!=0 and i!=len(value):
                return True
        return False
    except:
        1==1

def reader(string,rows,cols):
    try:
        if string[-1]!=']' and string[0]!='[':
            return 0
        elif int(rows)<10 and int(cols)<10:
            string = string.replace(",",'\t')
            string = string.replace("[","")
            string = string.replace("]","")
            a = np.fromstring(string, sep='\t').reshape(int(rows), int(cols))
            return a
        else:
            return 1
    except:
        return 0

import ast
def reader0(string):
    try:
        if string[-1]!=']' and string[0]!='[':
            return 0
        string = ast.literal_eval(string)
        return np.array(string)
    except:
        return 0

def appender(array0,array1):
    try:
        array0 = str(array0)
        array1 = str(array1)
        array0 = array0.replace(" ",",")
        array1 = array1.replace(" ",",")
        array0 = ast.literal_eval(array0)
        array1 = ast.literal_eval(array1)
        j = 0
        for i in range(len(array1)):
            if j<=len(array0):
                array0[j].append(array1[i])
            else:
                break
            j+=1
        return np.array(array0)
    except:
        1==1

def director2(a,b):
        import math
        try:
            angle = 0
            if a==0 and b==0:
                angle = 0
            elif a==0 or b==0:
                if a==0:
                    if b>0:
                        angle = 90
                    else:
                        angle = 270
                else:
                    if a>0:
                        angle = 0
                    else:
                        angle = 180
            else:
                value = b/a
                angle = math.degrees(math.atan(value))
                if a>0 and b>0:
                    if 0<angle<90:
                        angle = math.degrees(math.atan(value))
                    else:
                        if angle<0:
                            while angle<=0:
                                angle+=45
                        
                        elif angle>90:
                            while angle>=90:
                                angle-=45
                        
                if a<0 and b>0:
                    if 90<angle<180:
                        angle = math.degrees(math.atan(value))
                    else:
                        if angle<90:
                            while angle<=90:
                                angle+=45
                     
                        elif angle>180:
                            while angle>=180:
                                angle-=45
                     
                if a<0 and b<0:
                    if 180<angle<270:
                        angle = math.degrees(math.atan(value))
                    else:
                        if angle<180:
                            while angle<=180:
                                angle+=45
                        elif angle>270:
                            while angle>=270:
                                angle -= 45
                if a>0 and b<0:
                    if 270<angle<360:
                        angle = math.degrees(math.atan(value))
                    else:
                        if angle<270:
                            while angle<=270:
                                angle+=45
                        elif angle>360:
                            while angle>=360:
                                angle-=45
            return str(angle)
        except:
            1==1

def quantify(normlist):
    try:
        sumsqrd = 0
        for value in normlist:
            sumsqrd+=((value)**2)
        mag = sumsqrd**0.5
        return str(mag)+" units"
    except:
        1==1

def normer(normlist):
    try:
        sumsqrd = 0
        for value in normlist:
            sumsqrd+=((value)**2)
        mag = sumsqrd**0.5
        outstring="["
        for i in range(len(normlist)):
            if i<len(normlist)-1:
                outstring=outstring+str((normlist[i])/mag)+","
            else:
                outstring=outstring+str((normlist[i])/mag)+"]"     
        return outstring
    except:
        1==1   

def readout(a,cols):
    try:
        count = cols
        out = "["
        for i in range(len(a)):
            if i==len(a)-1:
                out+="x"+str(cols-count+1)+"= "+str(a[i])+"]"
            else:
                out+="x"+str(cols-count+1)+"= "+str(a[i])+"  "
            count=count-1
        return out    
    except:
        1==1    


multiplicationstrings = []
addstrings = []
addstringsrowscols = []
multiplicationstringsrowscols = []
veccrossstrings=[]
vecdotstrings=[]
vecprojectionstrings=[]
vecbetweenstrings=[]

class TwoWindow(Screen):
    haha = ObjectProperty(None)
    entry = ObjectProperty(None)
    entry1 = ObjectProperty(None)
    pop1 = ObjectProperty(None)
    inbase = ObjectProperty(None)
    outbase = ObjectProperty(None)
    value = ObjectProperty(None)
    tensvalue = ObjectProperty(None)
    tensinbase = ObjectProperty(None)
    asciivalue = ObjectProperty(None)
    solverows=ObjectProperty(None)
    solvecols=ObjectProperty(None)
    solvestring=ObjectProperty(None)
    inverserows=ObjectProperty(None)
    inversecols=ObjectProperty(None)
    inversestring=ObjectProperty(None)
    multiplicationrows=ObjectProperty(None)
    multiplicationcols=ObjectProperty(None)
    multiplicationstring=ObjectProperty(None)
    addrows=ObjectProperty(None)
    addcols=ObjectProperty(None)
    addstring=ObjectProperty(None)
    dotrows=ObjectProperty(None)
    dotcols=ObjectProperty(None)
    dotstring=ObjectProperty(None)
    scalarrows=ObjectProperty(None)
    scalarcols=ObjectProperty(None)
    scalarstring=ObjectProperty(None)
    determinantstring=ObjectProperty(None)
    determinantrows=ObjectProperty(None)
    determinantcols=ObjectProperty(None)
    rankcols=ObjectProperty(None)
    rankrows=ObjectProperty(None)
    rankstring=ObjectProperty(None)
    bee = ObjectProperty(None)
    vecsolvestring=ObjectProperty(None)
    veccrossstring=ObjectProperty(None)
    vecdotstring=ObjectProperty(None)
    vecprojectionstring=ObjectProperty(None)
    vecnormstring=ObjectProperty(None)
    vecmagnitudestring=ObjectProperty(None)
    vecdirectionstring=ObjectProperty(None)
    vecbetweenstring=ObjectProperty(None)
    screen_manager=ObjectProperty(None)

    def clearOne(self):
        self.inbase.text = ""
        self.outbase.text = ""
        self.value.text = ""

    def clearTwoTwos(self):
        self.entry.text = ""
        self.entry1.text = ""
        self.pop1.text = ""
    
    def clearTwoTens(self):
        self.tensvalue.text = ""
        self.tensinbase.text = ""

    def clearThree(self):
        self.asciivalue.text = ""

    def solveclear(self):
        self.solverows.text=''
        self.solvecols.text=''
        self.solvestring.text=''
        self.bee.text=""

    def inverseclear(self):
        self.inverserows.text=''
        self.inversecols.text=''
        self.inversestring.text=''

    def multiplicationclear(self):
        global multiplicationstrings
        self.multiplicationrows.text=''
        self.multiplicationcols.text=''
        self.multiplicationstring.text=''
        multiplicationstrings = []

    def addclear(self):
        global addstrings
        self.addrows.text=''
        self.addcols.text=''
        self.addstring.text=''
        addstrings=[]
        
    def determinantclear(self):
        self.determinantstring.text=""
        self.determinantrows.text=""
        self.determinantcols.text=""
    
    def rankclear(self):
        self.rankrows.text=""
        self.rankcols.text=""
        self.rankstring.text=""

    def vecsolveclear(self):
        self.vecsolvestring.text=""
        self.vecnormstring.text=""
        self.vecmagnitudestring.text=""

    def vecprojectionclear(self):
        global vecprojectionstrings
        self.vecprojectionstring.text=""
        vecprojectionstrings=[]

    def veccrossclear(self):
        global veccrossstrings
        self.veccrossstring.text=""
        veccrossstrings=[]
    
    def vecdotclear(self):
        global vecdotstrings
        self.vecdotstring.text=""
        vecdotstrings=[]

    def vecdirectionclear(self):
        self.vecdirectionstring.text=""

    def vecbetweenclear(self):
        global vecbetweenstrings
        self.vecbetweenstring.text=""
        vecbetweenstrings=[]

    def multiplicationload(self):
        global multiplicationstrings
        try:
            if str(reader(self.multiplicationstring.text,self.multiplicationrows.text,self.multiplicationcols.text))=='0':
                self.multiplicationstring.text="Matrix could not be read, clear this using backspace and load another matrix."
            elif str(reader(self.multiplicationstring.text,self.multiplicationrows.text,self.multiplicationcols.text))=="1":
                self.multiplicationstring.text="Limited to 9 by 9 matrices, clear this using backspace and load another matrix."
            elif len(multiplicationstrings)>=2:
                self.multiplicationstring.text="You have already added 2 matrices."
            elif len(multiplicationstrings)<2 and str(reader(self.multiplicationstring.text,self.multiplicationrows.text,self.multiplicationcols.text))!='0' and str(reader(self.multiplicationstring.text,self.multiplicationrows.text,self.multiplicationcols.text))!="1":
                multiplicationstrings.append(self.multiplicationstring.text)
                multiplicationstringsrowscols.append(self.multiplicationrows.text)
                multiplicationstringsrowscols.append(self.multiplicationcols.text)
                self.multiplicationstring.text =""
                self.multiplicationcols.text=""
                self.multiplicationrows.text=""
        except:
            1==1
      
    
    def addload(self):
        global addstrings
        try:
            if str(reader(self.addstring.text,self.addrows.text,self.addcols.text))=="0":
                self.addstring.text="Matrix could not be read, clear this using backspace and load another matrix."
                return 0
            elif str(reader(self.addstring.text,self.addrows.text,self.addcols.text))=="1":
                self.addstring.text="Limited to 9 by 9 matrices, clear this using backspace and load another matrix."
                return 0
            elif len(addstrings)>=2:
                self.addstring.text="You have already added 2 matrices."
                return 0
            elif len(addstrings)<2 and str(reader(self.addstring.text,self.addrows.text,self.addcols.text))!='0' and str(reader(self.addstring.text,self.addrows.text,self.addcols.text))!="1":
                addstrings.append(self.addstring.text)
                addstringsrowscols.append(self.addrows.text)
                addstringsrowscols.append(self.addcols.text)
                self.addcols.text=""
                self.addrows.text=""
                self.addstring.text=""
                return 0
        except:
            1==1

    def veccrossload(self):
        global veccrossstrings
        try:
            if len(veccrossstrings)<2 and str(reader0(self.veccrossstring.text))!='0':
                veccrossstrings.append(self.veccrossstring.text)
                self.veccrossstring.text=""
            elif str(reader0(self.veccrossstring.text))=='0':
                self.veccrossstring.text="Vector could not be read, clear this using backspace and load another vector."
            elif len(veccrossstrings)>=2:
                self.veccrossstring.text="You have already added 2 vectors."
        except:
            1==1

    def vecprojectionload(self):
        global vecprojectionstrings
        try:
            if len(vecprojectionstrings)<2 and str(reader0(self.vecprojectionstring.text))!='0':
                vecprojectionstrings.append(self.vecprojectionstring.text)
                self.vecprojectionstring.text=""
            elif str(reader0(self.vecprojectionstring.text))=='0':
                self.vecprojectionstring.text="Vector could not be read, clear this using backspace and load another vector."
            elif len(vecprojectionstrings)>=2:
                self.vecprojectionstring.text="You have already added 2 vectors."
        except:
            1==1
        

    def vecdotload(self):
        global vecdotstrings
        try:
            if len(vecdotstrings)<2 and str(reader0(self.vecdotstring.text))!='0':
                vecdotstrings.append(self.vecdotstring.text)
                self.vecdotstring.text=""
            elif str(reader0(self.vecdotstring.text))=='0':
                self.vecdotstring.text="Vector could not be read, clear this using backspace and load another vector."
            elif len(vecdotstrings)>=2:
                self.vecdotstring.text="You have already added 2 vectors."
        except:
            1==1

    def vecbetweenload(self):
        global vecbetweenstrings
        try:
            if len(vecbetweenstrings)<2 and str(reader0(self.vecbetweenstring.text))!='0':
                vecbetweenstrings.append(self.vecbetweenstring.text)
                self.vecbetweenstring.text=""
            elif str(reader0(self.vecbetweenstring.text))=='0':
                self.vecbetweenstring.text="Vector could not be read, clear this using backspace and load another vector."
            elif len(vecbetweenstrings)>=2:
                self.vecbetweenstring.text="You have already added 2 vectors."
        except:
            1==1
        
    def converter(self):
        try:
            if int(self.inbase.text)<37 and int(self.outbase.text)<37:
                oct2 = ''
                oct1 = ''
                alfabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                inbase = self.inbase
                value = self.value
                outbase = self.outbase
                value.text = evaluator(value.text)
                if fraction(value.text)==True: 
                    if value.text[0] == "0":
                        oct2 = value.text
                        oct22 = 0
                        oct22 = b2t(oct2,int(inbase.text))
                        if oct22=="error":
                            self.value.text = "This value is not a base {} value.".format(inbase.text)
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
                        if oct22=="error":
                            self.value.text = "This value is not a base {} value.".format(inbase.text)
                        else:
                            if int(outbase.text)!=10:
                                oct1 = t2b(oct22,int(outbase.text))
                            else:
                                oct1 = oct22
                if int(inbase.text)!=-1:
                    for i in range(len(value.text)):
                        try:
                            apps = int(value.text[i],int(inbase.text))
                        except:
                            self.value.text = "This value is not a base {} value.".format(inbase.text)
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
                        self.value.text = str(''.join(digits))+oct1[1:]
            else:
                self.value.text="Input base and output base should both be less than 37." 
        except:
            1==1
    
    def Twos(self):
        try:
            if int(self.pop1.text)<37:
                apps=0
                for i in range(len(self.entry.text)):
                    try:
                        if self.entry.text[i]!='-':
                            apps = int(self.entry.text[i],int(self.pop1.text))
                    except:
                        self.entry.text = "This value is not a base {} value.".format(self.pop1.text)
                        return 0
                apps1 = int(self.entry.text,int(self.pop1.text))
                if apps1>(2**(int(self.entry1.text)-1))-1 or apps1<-2**(int(self.entry1.text)-1):
                    self.entry.text="Input requires greater bits."
                    return 0

                bits = self.entry1.text 
                outbase = 2
                pop = int(self.entry.text,int(self.pop1.text))
                value = 2**(int(bits))-(abs(pop))
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
            else:
                self.entry.text="Input base should be less than 37."
        except:
            1==1

    def Tens(self):
        try:
            if int(self.tensinbase.text)<37:
                inbase = self.tensinbase
                entry = self.tensvalue
                num = len(self.entry.text)
                for i in range(len(entry.text)):
                    try:
                        if self.tensvalue.text[i]!='-':
                            apps = int(entry.text[i],int(inbase.text))
                    except:
                        self.tensvalue.text = "This value is not a base {} value.".format(inbase.text)
                        return 0
                entry.text = str(int(entry.text,int(inbase.text)))
                num = len(entry.text)
                if int(entry.text)<0:
                    self.tensvalue.text = str((10**(num-1))-abs(int(entry.text)))
                elif int(entry.text)>0:
                    self.tensvalue.text = str((10**(num))-abs(int(entry.text)))
            else:
                self.tensvalue.text="Input base should be less than 37."
        except:
            1==1

    
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
                    if self.asciivalue.text == "" and outbase == "":
                        self.asciivalue.text="No base or value given."
                    elif self.asciivalue.text =="":
                        self.asciivalue.text = "I am empty."
                    elif outbase =="":
                        self.asciivalue.text="I am empty."
                

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
                    if self.asciivalue.text == "" and outbase== "":
                        self.asciivalue.text="No base or value given."
                    elif self.asciivalue.text =="":
                        self.asciivalue.text = "I am empty."
                    elif outbase =="":
                        self.asciivalue.text="I am empty."

        except:
            1==1

    def inv(self):
        try:
            if str((reader(self.inversestring.text,int(self.inverserows.text),int(self.inversecols.text))))=="0":
                self.inversestring.text="Matrix could not be read."
            elif str((reader(self.inversestring.text,int(self.inverserows.text),int(self.inversecols.text))))=="1":
                self.inversestring.text="Limited to 9 by 9 matrices."
            elif self.inversecols.text!=self.inverserows.text:
                self.inversestring.text="Non-square matrices do not have inverses."
            elif np.linalg.det(reader(self.inversestring.text,int(self.inverserows.text),int(self.inversecols.text)))==0:
                self.inversestring.text="Singular matrices do not have inverses."
            else: 
                self.inversestring.text = str(np.linalg.inv(reader(self.inversestring.text,int(self.inverserows.text),int(self.inversecols.text))))
        except:
            1==1

    def mul(self):
        global multiplicationstrings    
        try:
            if len(multiplicationstrings)==2:
                if multiplicationstringsrowscols[1]==multiplicationstringsrowscols[2]:
                    if int(multiplicationstringsrowscols[0])<10 and int(multiplicationstringsrowscols[1])<10 and int(multiplicationstringsrowscols[2])<10 and int(multiplicationstringsrowscols[3])<10:
                        out1 = reader(multiplicationstrings[0],multiplicationstringsrowscols[0],multiplicationstringsrowscols[1])
                        out2 = reader(multiplicationstrings[1],multiplicationstringsrowscols[2],multiplicationstringsrowscols[3])
                        self.multiplicationstring.text = str(np.matmul(out1,out2))
                        multiplicationstrings=[]
                    else:
                        self.multiplicationstring.text = "Limited to 9 by 9 matrices, clear this using the clear button and retry with two new matrices."
                else:
                    self.multiplicationstring.text = "These matrices are not multiplicable, clear this using the clear button and retry with two new matrices."
            else:
                self.multiplicationstring.text="You have not loaded two matrices, clear this using backspace and load another matrix."
        except:
            1==1
        

    def add(self):
        global addstrings
        try:
            if len(addstrings)==2:
                if (addstringsrowscols[0])==(addstringsrowscols[2]) and (addstringsrowscols[1])==(addstringsrowscols[3]):
                    if int(addstringsrowscols[0])<10 and int(addstringsrowscols[1])<10 and int(addstringsrowscols[2])<10 and int(addstringsrowscols[3])<10:
                        out1 = reader(addstrings[0],addstringsrowscols[0],addstringsrowscols[1])
                        out2 = reader(addstrings[1],addstringsrowscols[2],addstringsrowscols[3])
                        self.addstring.text = str(np.add(out1,out2))
                        addstrings=[]
                    else:
                        self.addstring.text = "Limited to 9 by 9 matrices, clear this using the clear button and retry with two new matrices."
                else:
                    self.addstring.text = "These matrices can't be added, clear this using the clear button and retry with two new matrices."
            else:
                self.addstring.text="You have not loaded two matrices, clear this using backspace and load another matrix."
        except:
            1==1
        

    def ran(self):
        try:
            if str((reader(self.rankstring.text,self.rankrows.text,self.rankcols.text)))=="0":
                self.rankstring.text="Matrix could not be read, clear this using the clear button and retry with a new matrix."
            elif str((reader(self.rankstring.text,self.rankrows.text,self.rankcols.text)))=="1":
                self.rankstring.text="Limited to 9 by 9 matrices, clear this using the clear button and retry with a new matrix."
            else:
                self.rankstring.text = str(np.linalg.matrix_rank(reader(self.rankstring.text,self.rankrows.text,self.rankcols.text)))
        except:
            1==1
    def det(self):
        try:
            if  str((reader(self.determinantstring.text,self.determinantrows.text,self.determinantcols.text))) == '0':
                self.determinantstring.text="Matrix could not be read, clear this using the clear button and retry with a new matrix."
            elif str((reader(self.determinantstring.text,self.determinantrows.text,self.determinantcols.text))) == "1":
                self.determinantstring.text="Limited to 9 by 9 matrices, clear this using the clear button and retry with a new matrix."
            elif self.determinantrows.text!=self.determinantcols.text:
                self.determinantstring.text="Determinants are not defined for non-square matrices, clear this using the clear button and retry with a new matrix."
            else:
                self.determinantstring.text = str(np.linalg.det(reader(self.determinantstring.text,self.determinantrows.text,self.determinantcols.text))) 
        except:
            1==1
    
    def solve(self):
        try:
            if str(reader(self.solvestring.text,self.solverows.text,self.solvecols.text))=="0":
                self.solvestring.text="Matrix could not be read, clear this using the clear button and retry with a new matrix."
            elif str(reader(self.solvestring.text,self.solverows.text,self.solvecols.text))=="1":
                self.solvestring.text="Limited to 9 by 9 matrices, clear this using the clear button and retry with a new matrix."
            else:
                A = reader(self.solvestring.text,self.solverows.text,self.solvecols.text)
                b = reader0(self.bee.text)
                if str(reader0(self.bee.text))=="0":
                    self.solvestring.text="B could not be read, clear this using the clear button and retry with a new A and B."
                    return 0
                A1 = appender(A,b)
                if np.linalg.matrix_rank(A1) == np.linalg.matrix_rank(A):
                    if np.linalg.matrix_rank(A)!=int(self.solvecols.text):
                        self.solvestring.text = "Infinite solutions."
                    else:
                        try:
                            self.solvestring.text = str(readout(np.linalg.solve(A, b),int(self.solvecols.text)))
                        except:
                            self.solvestring.text = str(readout(np.linalg.lstsq(A, b)[0],int(self.solvecols.text)))
                else:
                    self.solvestring.text="No solution."
        except:
            1==1

    def vecprojectionsolve(self):
        global vecprojectionstrings
        try:
            scalarproj = 0
            scalarproj1 = 0
            vectorproj = "["
            magn = 0
            if len(vecprojectionstrings)==2:
                if len(reader0(vecprojectionstrings[0]))!=len(reader0(vecprojectionstrings[1])):
                    self.vecprojectionstring.text = "Some values do not have their correspondants, clear this using the clear button and retry with two new vectors."
                    vecprojectionstrings=[]
                else:
                    out = 0
                    for i in range(0,len(reader0(vecprojectionstrings[0]))):
                        out += ((reader0(vecprojectionstrings[0])[i])*(reader0(vecprojectionstrings[1])[i]))
                    self.vecprojectionstring.text = str(out)
                    for value in reader0(vecprojectionstrings[0]):
                        magn = magn + value**2
                    magn = magn**0.5
                    scalarproj = out/magn
                    scalarproj1 = out/(magn**2)
                    for i in range(len(reader0(vecprojectionstrings[0]))):
                        if i==len(reader0(vecprojectionstrings[0]))-1:
                            vectorproj+=str((reader0(vecprojectionstrings[0]))[i]*scalarproj1)
                        else:
                            vectorproj=vectorproj+str((reader0(vecprojectionstrings[0])[i])*scalarproj1)+", "
                    vectorproj+=']'
                    self.vecprojectionstring.text="Scalar projection of {} onto {}:\n{}\nVector projection {} onto {}:\n{}\n".format(vecprojectionstrings[1],vecprojectionstrings[0],str(scalarproj),vecprojectionstrings[1],vecprojectionstrings[0],str(vectorproj)) 
                    vecprojectionstrings=[]
            else:
                self.vecprojectionstring.text="You have not added two vectors, clear this using backspace and load another vector."
        except:
            1==1
        
    def dotsolve(self):
        global vecdotstrings
        try:
            if len(vecdotstrings)==2:
                if len(reader0(vecdotstrings[0]))!=len(reader0(vecdotstrings[1])):
                    self.vecdotstring.text= "Some values do not have their correspondants, clear this using the clear button and retry with two new vectors."
                else:
                    out=0
                    for i in range(len(reader0(vecdotstrings[0]))):
                        out = out + ((reader0(vecdotstrings[0]))[i])*((reader0(vecdotstrings[0]))[i])
                    self.vecdotstring.text="Dot product:\n{}".format(out)
                    vecdotstrings=[]
            else:
                self.vecdotstring.text="You have not added two vectors, clear this using backspace and load another vector."
        except:
            1==1
        

    def vecsolve(self):
        try:
            if str(reader0(self.vecsolvestring.text))!="0":
                out0 = quantify(reader0(self.vecsolvestring.text))
                out1 = normer(reader0(self.vecsolvestring.text))
                self.vecmagnitudestring.text=out0
                self.vecnormstring.text=out1
            else:
                self.vecsolvestring.text="Vector could not be read, clear this using the clear button and retry with a new vector."
        except:
            1==1

    def vecdirection(self):
        try:
            if str(reader0(self.vecdirectionstring.text))!='0':
                if len(reader0(self.vecdirectionstring.text))==2:
                    self.vecdirectionstring.text=str(director2((reader0(self.vecdirectionstring.text))[0],(reader0(self.vecdirectionstring.text))[1]))+" degrees"
                else:
                    self.vecdirectionstring.text="Vector should be 2 dimensional, clear this using the clear button and retry with a new vector."  
            else:
                self.vecdirectionstring.text="Vector could not be read, clear this using the clear button and retry with a new vector." 
        except:
            1==1
        
    def vecbetween(self):
        global vecbetweenstrings
        try:
            if len(vecbetweenstrings)==2:
                if len(reader0(vecbetweenstrings[0]))==2 and len(reader0(vecbetweenstrings[1]))==2:
                    self.vecbetweenstring.text= str(abs(float(director2((reader0(vecbetweenstrings[0]))[0],(reader0(vecbetweenstrings[0]))[1]))-float(director2((reader0(vecbetweenstrings[1]))[0],(reader0(vecbetweenstrings[1]))[1]))))+" degrees"
                    vecbetweenstrings=[]
                else:
                    self.vecbetweenstring.text="Vectors should be 2 dimensional, clear this using the clear button and retry with two new vectors."
            else:
                self.vecbetweenstring.text="You have not added two vectors, clear this using backspace and load another vector."
        except:
            1==1

    def show_data(self,obj):
        self.dialog = MDDialog(text=obj, size_hint=(.5,.1725), buttons=[MDFlatButton(text="Got it!", on_release=self.close_dialog)])
        self.dialog.open()

    def show_data1(self,obj):
        self.dialog = MDDialog(text="Enter [A] and its entries in form\n\n[a(11), a(12)]\n[a(21), a(22)]\n\nLimited to a(99).\n\nEnter the number of rows and columns. Write [B] transposed i.e if B is\n\nb1\nb2\n\nWrite it as [b1,b2]. Always use the enter button (new line button) to move onto next row.", size_hint=(.5,.2), buttons=[MDFlatButton(text="Got it!", on_release=self.close_dialog)])
        self.dialog.open()

    def show_data2(self,obj):
        self.dialog = MDDialog(text="Enter matrix and its entries in form\n\n[a(11), a(12)]\n[a(21), a(22)]\n\nLimited to a(99).\n\nEnter the number of rows and columns then load matrix into register. Repeat this process for the second matrix and press calculate once you have loaded two matrices. Always use the enter button (new line button) to move onto next row.", size_hint=(.5,.2), buttons=[MDFlatButton(text="Got it!", on_release=self.close_dialog)])
        self.dialog.open()
    
    def show_data3(self,obj):
        self.dialog = MDDialog(text="Enter matrix and its entries in form\n\n[a(11), a(12)]\n[a(21), a(22)]\n\nLimited to a(99).\n\nEnter the number of rows and columns then press calculate to see results. Always use the enter button (new line button) to move onto next row.", size_hint=(.5,.2), buttons=[MDFlatButton(text="Got it!", on_release=self.close_dialog)])
        self.dialog.open()

    def show_data4(self,obj):
        self.dialog = MDDialog(text="Enter vector components in form [x1,x2] i.e if vector is in form\n\nx1\nx2\n\nWrite it as [x1,x2] then press calculate to see results.", size_hint=(.5,.2), buttons=[MDFlatButton(text="Got it!", on_release=self.close_dialog)])
        self.dialog.open()

    def show_data5(self,obj):
        self.dialog = MDDialog(text="Enter vector components in form [x1,x2] i.e if vector is in form\n\nx1\nx2\n\nWrite it as [x1,x2] then load vector into register. Repeat this process for the second vector and press calculate once you have loaded two vectors.", size_hint=(.5,.2), buttons=[MDFlatButton(text="Got it!", on_release=self.close_dialog)])
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

    def tshikirini(self, screen, *args):
        self.ids.screen_manager.current = screen
        self.ids.nav_drawer.toggle_nav_drawer()

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab'''

class WindowManager(ScreenManager):
    pass

sm = ScreenManager()
sm.add_widget(OneWindow(name = "one"))
sm.add_widget(TwoWindow(name = "two"))


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Orange"
        self.help_str = Builder.load_string(helper_string)
        screen.add_widget(self.help_str)
        self.title = "computaxion"
        self.theme_cls.theme_style = "Dark"
        return screen
        
    def on_start(self):
        try:
            self.help_str.get_screen("two").ids.tabs.add_widget(Tab())
            self.help_str.get_screen("two").ids.tabs.add_widget(Tab())
        except:
            1==1

    def on_tab_switch(self,instance_tabs,instance_tab,instance_tab_label,tab_text):
        try:
            '''Called when switching tabs.

            :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
            :param instance_tab: <__main__.Tab object>;
            :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
            :param tab_text: text or name icon of tab;
            '''
            instance_tab.ids.label.text = tab_text
        except:
            1==1

MainApp().run()
