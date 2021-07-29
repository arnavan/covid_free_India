from kivy.uix.screenmanager import Screen
import requests
from kivymd.uix.list import MDList, ThreeLineListItem
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDRoundFlatButton
from kivymd.uix.dialog import MDDialog
import time

class Centre(Screen):
    Dialog = None
    label = None
    button = None
    centres = None

    def remove_center(self, obj):
        if self.centres is not None:
            self.ids.layout.remove_widget(self.centres)
            self.centres = None
        if self.button is not None:
            self.ids.layout.remove_widget(self.button)
            self.button = None
        if self.label is not None:
            self.ids.layout.remove_widget(self.label)
            self.label = None

    def on_leave(self, *args):
        if self.centres is not None:
            self.ids.layout.remove_widget(self.centres)
            self.centres = None
        if self.button is not None:
            self.ids.layout.remove_widget(self.button)
            self.button = None
        if self.label is not None:
            self.ids.layout.remove_widget(self.label)

    def on_click(self):
        if self.ids.pincode.text == "":
            self.Dialog = MDDialog(
                title="Information is not correct",
                text="Hmm... It seems like your information is incorrect. Please try again",
                buttons=[MDRaisedButton(text='Close', on_release=self.close_dialog)]
            )
            self.Dialog.open()
        elif self.ids.date.text == "":
            self.Dialog = MDDialog(
                title="Information is not correct",
                text="Hmm... It seems like your information is incorrect. Please try again",
                buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
            )
            self.Dialog.open()
        elif self.ids.ac_lang.text == "":
            self.Dialog = MDDialog(
                title="Information is not correct",
                text="Hmm... It seems like your information is incorrect. Please try again",
                buttons=[MDRaisedButton(text='Close', on_release=self.close_dialog)]
            )
            self.Dialog.open()
        else:
            pincode = self.ids.pincode.text
            counter = 0
            date = self.ids.date.text
            URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(
                pincode, date)
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
            result = requests.get(URL, headers=header)
            response_json = result.json()
            data = response_json["sessions"]
            if self.label is None:
                self.label = MDLabel(
                    text="List Of Available Centers",
                    font_style="H4",
                    halign="center"
                )
                self.ids.layout.add_widget(self.label)

            self.centres = MDList()
            self.ids.layout.add_widget(self.centres)
            if self.button is None:
                self.button = MDRoundFlatButton(
                    text="Close", on_release=self.remove_center
                )
                self.ids.layout.add_widget(self.button)
            for each in data:
                if ((each["available_capacity"] > 0) & (each["min_age_limit"] == 18)):
                    counter += 1
                    self.centres.add_widget(
                        ThreeLineListItem(
                            text=str(each["name"]),
                            secondary_text=str(each["vaccine"]),
                            tertiary_text=str(each["available_capacity"])
                        )
                    )
                    print(each["name"])
                    print(each["vaccine"])
                    print(each["available_capacity"])
            if (counter == 0):
                self.Dialog = MDDialog(
                    title="No Available Centres on this day :(",
                    text="Sorry but there doesn't seems to be any available slots on this day",
                    buttons=[MDRaisedButton(text='Okay', on_release=self.close_dialog)]
                )
                self.ids.layout.remove_widget(self.centres)
                self.ids.layout.remove_widget(self.button)
                self.ids.layout.remove_widget(self.label)
                self.Dialog.open()
                print("No Available Slots")
                return False
        print(self.ids.pincode.text)
        print(self.ids.date.text)
        print(self.ids.ac_lang.text)
    def close_dialog(self, obj):
        self.Dialog.dismiss()