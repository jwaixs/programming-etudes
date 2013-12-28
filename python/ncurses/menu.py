#!/usr/bin/env python

# Based on http://stackoverflow.com/questions/14200721/how-to-create-a-menu-and-submenus-in-python-curses

import curses
from curses import panel

class Menu(object):
    def __init__(self, items, stdscreen):
        self.window = stdscreen.subwin(0, 0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items
        self.items.append(('exit', 'exit'))

    def navigate(self, n):
        self.position += n
        self.position = self.position % len(self.items)

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL
                msg = '%d. %s' % (index, item[0])
                self.window.addstr(index + 1, 1, msg, mode)            

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.items[self.position][0] == 'exit':
                    break
                else:
                    self.items[self.position][1]()
            elif key == curses.KEY_UP:
                self.navigate(-1)
            elif key == curses.KEY_DOWN:
                self.navigate(1)

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

class InfoPanel(object):
    def __init__(self, items, stdscreen):
        self.window = stdscreen.subwin(70, 70, 10, 10)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.items = items

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            index = 1
            for subject, info in self.items:
                msg = '%s: %s' % (subject, info)
                self.window.addstr(index, 1, msg, curses.A_NORMAL)
                index += 1

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                break

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

class MyTestApp(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        sub_menu_items = [
            ('beep this', curses.beep),
            ('beep that', curses.beep)
        ]
        submenu = Menu(sub_menu_items, self.screen)

        info_panel_items = [
            ('Name', 'Info test panel.'),
            ('Subject', 'Programming etudes.'),
            ('Comments', 'Doing info panel programming stuff with ncurses.'),
            ('Test', 'Let\'s test what will happen if the text in this column gets too large. Will ncurses be able to wrap the text around here or will it just display one big sentence? I have no idea, yet... It just displays the full text.'),
        ]
        infopanel = InfoPanel(info_panel_items, self.screen)

        main_menu_items = [
            ('beep', curses.beep),
            ('flash', curses.flash),
            ('submenu', submenu.display),
            ('infopanel', infopanel.display),
        ]
        main_menu = Menu(main_menu_items, self.screen)
        main_menu.display()

if __name__ == '__main__':
    curses.wrapper(MyTestApp)
