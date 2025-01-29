from __future__ import annotations

import typing
import urwid


if typing.TYPE_CHECKING:

    from collections.abc import Iterable


#Core List For Program Menus
choices = "Profile Notes Settings".split()
curr_screen = 0

#Attr Maps for stylizing
large_font = urwid.AttrMap('large_font', 'default', {'font': ('default', 20)})


palette = [

    ("reversed", "standout", "")


]



#Main Menu Config
def menu(title: str, choices_: Iterable[str]) -> urwid.ListBox:

    body = [urwid.Text(title), urwid.Divider()]


    for c in choices_:

        button = urwid.Button(c)

        urwid.connect_signal(button, "click", add_screen, c)

        body.append(urwid.AttrMap(button, None, focus_map="reversed"))


    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


#Sub Menu Config
def item_chosen(choice: str) -> urwid.ListBox:
        
    body = [urwid.Text([choice, "\n"]), urwid.Divider()]


    #Menu Traversal

    # done = urwid.Button("Ok")

    # back = urwid.Button("Back")


    # urwid.connect_signal(done, "click", exit_program)


    # urwid.connect_signal(back, "click", back_screen)

    # #Add Items to body (display list)
    # body.append(urwid.AttrMap(done, None, focus_map="reversed"))
                
    # body.append(urwid.AttrMap(back, None, focus_map="reversed"))

    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def add_screen(choice: str, wildcard) -> None:

    global curr_screen
    screen_builder = urwid.Padding(item_chosen(choice), left=2, right=2)

    on_screen = urwid.Overlay(

        screen_builder,

        urwid.SolidFill("\N{MEDIUM SHADE}"),

        align=urwid.CENTER,

        width=(urwid.RELATIVE, 60),

        valign=urwid.MIDDLE,

        height=(urwid.RELATIVE, 60),

        min_width=20,

        min_height=9,

    )

    screen.append(on_screen)
    curr_screen += 1

def back_screen() -> None:
    curr_screen -= 1

#Default Actions
def exit_program(button: urwid.Button) -> None:

    raise urwid.ExitMainLoop()

def exit_on_press(key: str) -> None:
    
    if key in {"q", "Q"}:
        raise urwid.ExitMainLoop()






#Main Functions


main = urwid.Padding(menu("RADIX", choices), left=2, right=2)



top = urwid.Overlay(

    main,

    urwid.SolidFill("\N{MEDIUM SHADE}"),

    align=urwid.CENTER,

    width=(urwid.RELATIVE, 60),

    valign=urwid.MIDDLE,

    height=(urwid.RELATIVE, 60),

    min_width=20,

    min_height=9,

)

screen = [top]

temp = urwid.Padding(item_chosen("Test"), left=2, right=2),

test = urwid.Overlay(
    
    temp,

    urwid.SolidFill("\N{MEDIUM SHADE}"),

    align=urwid.CENTER,

    width=(urwid.RELATIVE, 60),

    valign=urwid.MIDDLE,

    height=(urwid.RELATIVE, 60),

    min_width=20,

    min_height=9,
)

screen.append(test)

curr_screen = 1
urwid.MainLoop(screen[curr_screen], palette=palette, unhandled_input=exit_on_press).run()