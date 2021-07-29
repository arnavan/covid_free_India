from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen, Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivy.lang.builder import Builder
from covid import Covid

covid_j = Covid(source="worldometers")

def myFunc(e):
    return e['confirmed']

def covid_data_by_recovering(e):
    return e['recovered']

def return_country_by_deaths(e):
    return e['deaths']



class Trends(MDScreen):
    covid_j_data = covid_j.get_data()
    covid_recovered = covid_j.get_data()
    covid_deaths = covid_j.get_data()
    covid_j_data.sort(key=myFunc, reverse=True)
    covid_recovered.sort(key=covid_data_by_recovering, reverse=True)
    covid_deaths.sort(key=return_country_by_deaths, reverse=True)
    def country(self, list, id):
        return str(list[id]['country'])

    def confirmed(self,list,id):
        return str(list[id]['confirmed'])

    def confirmednum(self,list,id):
        return int(list[id]['confirmed'])

    def deaths(self,list,id):
        return int(list[id]['deaths'])

    def recovered(self,list, id):
        return int(list[id]['recovered'])

class ContentNavigationDrawer(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color