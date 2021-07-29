from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd_extensions.akivymd.uix.charts import AKBarChart
from Screens.Trends.table import Table
from Screens.Trends.Covid_Trends import Trends
from Screens.CovidChecker.main import CovidChecker
from Screens.Center.main import Centre

class CovidWarriors(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Covid Warriors"

    def on_start(self):
        sm.current = 'trends'
        print(sm.current)
    def build(self):
        screen = Builder.load_file('main.kv')
        return screen

if __name__ == "__main__":
    sm = ScreenManager()
    sm.add_widget(Trends(name="trends"))
    sm.add_widget(CovidChecker(name="checker"))
    sm.add_widget(Centre(name="centre"))
    sm.add_widget(Table(name="table"))
    CovidWarriors().run()