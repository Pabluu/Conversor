#! -*- coding: utf-8 -*-

# CONFIG
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemeManager
from kivy.uix.modalview import ModalView
from kivymd.filemanager import MDFileManager
from kivymd.toast import toast
from os.path import expanduser
from threading import Thread
import convert

HOME = expanduser('~')


class Manager(ScreenManager):
    pass


class Init(Screen):
    pass


class Main(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Red'
    title = "HQ's TO PDF"

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.manager_open = False
        self.manager = None

    def build(self):
        return Init()

    def file_manager_open(self):
        if not self.manager:
            self.manager = ModalView(size_hint=(1, 1), auto_dismiss=False)
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager,
                select_path=self.select_path,
                search='all',
                ext=['.*'])
            self.manager.add_widget(self.file_manager)
            self.file_manager.show(HOME)
        self.manager_open = True
        self.manager.open()

    def select_path(self, path):
        """It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;

        """

        self.exit_manager()
        toast(path)
        Thread(target=convert.Converter, args=[path]).start()

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager.dismiss()
        self.manager_open = False

    def events(self, instance, keyboard, keycode, text, modifiers):
        """Called when buttons are pressed on the mobile device.."""

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


Main().run()
