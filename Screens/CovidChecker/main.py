from kivy.uix.screenmanager import Screen
import pickle

from kivymd.uix.label import MDLabel


class CovidChecker(Screen):
    file = open('model.pkl', 'rb')
    clf = pickle.load(file)
    file.close()
    def on_click(self):
        global pain, runnyNose, diffBreath
        fever = int(self.ids.temp.text)
        age = int(self.ids.age.text)
        if self.ids.body_pain_0.active:
            pain = 0
        elif self.ids.body_pain_1.active:
            pain = 1
        if self.ids.yes_runny.active:
            runnyNose = 1
        elif self.ids.no_runny.active:
            runnyNose = 0
        if self.ids.no_difficulty.active:
            diffBreath = -1
        elif self.ids.little_difficulty.active:
            diffBreath = 0
        elif self.ids.severe_difficulty.active:
            diffBreath = 1
        inputFeatures = [fever, pain, age, runnyNose, diffBreath]
        infProb = self.clf.predict_proba([inputFeatures])[0][1]
        label = MDLabel(
            text=f"Covid Probability:- {round(infProb * 100)} %",
            font_style="H3",
            halign="center"
        )
        self.ids.layout.add_widget(label)