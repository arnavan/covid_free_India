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

covid = Covid(source="worldometers")
covid_data = covid.get_data()

def myFunc(e):
    return e['confirmed']


covid_data.sort(key=myFunc, reverse=True)
print(covid_data)


def country(id):
    return str(covid_data[id]['country'])


def confirmed(id):
    return str(covid_data[id]['confirmed'])

def new_cases(id):
    return str(covid_data[id]['new_cases'])


def active(id):
    return str(covid_data[id]['active'])


def deaths(id):
    return str(covid_data[id]['deaths'])


def new_deaths(id):
    return str(covid_data[id]['new_deaths'])


def critical(id):
    return str(covid_data[id]['critical'])


def recovered(id):
    return str(covid_data[id]['recovered'])

class Table(MDScreen):
    def on_enter(self, *args):
        data_tables = MDDataTable(
            size_hint=(1, 0.7),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            use_pagination=True,
            column_data=[
                ("Region", dp(30)),
                ("Confirmed Cases", dp(30)),
                ("New Cases", dp(30)),
                ("Deaths", dp(30)),
                ("New Deaths", dp(30)),
                ("Recovered", dp(30)),
                ("Active Cases", dp(30)),
                ("Critical Cases", dp(30))
            ],
            row_data=[
                (country(id), confirmed(id), new_cases(id), deaths(id), new_deaths(id), recovered(id), active(id),
                 critical(id))
                for id in range(0, len(covid_data))
            ],
        )
        data_tables.ids.container.add_widget(
            Widget(size_hint_y=None, height="5dp")
        )
        self.add_widget(data_tables)