from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput

class Hp_adder(RelativeLayout):
    def __init__(self, **kwargs):
        self.hp = 0
        self.color = [255,255,255]
        super().__init__()        

    def take_hp(self):
        self.hp -= 1
        label = self.ids['theinput']
        label.text = str(self.hp)

    def add_hp(self):
        self.hp += 1
        label = self.ids['theinput']
        label.text = str(self.hp)

    def change_color(self,but_id):
        color_dict={'white': [1,1,1,1],
                    'red':[1,0,0,1],
                    'blue':[0,0,1,1],
                    'yellow':[1,1,0,1],
                    'green':[0,1,0,1],
                    'maroon':[1,0.5,0.4,1],
                    'purple':[0.49,0,1,1]}
        self.color = color_dict[but_id]
        mons_name = self.ids['mons_name']
        mons_name.foreground_color = self.color
        theinput = self.ids['theinput']
        theinput.color = self.color
        plus = self.ids['plus']
        plus.color = self.color
        minus = self.ids['minus']
        minus.color = self.color 
        
class Hp_label(Label):
    pass

class Hp_plus(Button):
    pass

class Hp_minus(Button):
    pass

class Button_box(BoxLayout):
    pass

class Monster_name(TextInput):
    color = [0,0,0,1]
    pass

class Main_Window(TabbedPanel):       
    def add_buttons(self, **args):
        hp_adder = Hp_adder()
        butbox = self.ids['thebuttonbox']
        butbox.add_widget(hp_adder)
    
class QN_layout(App):
    def build(self):

        return Main_Window()

if __name__=='__main__':
    QN_layout().run()
