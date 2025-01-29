from __future__ import annotations


import typing


import urwid





if typing.TYPE_CHECKING:

    from collections.abc import Iterable


#Core List For Program Menus
choices = "Profile Notes Settings".split()


#Attr Maps for stylizing
large_font = urwid.AttrMap('large_font', 'default', {'font': ('default', 20)})


#Main Menu Config
def menu(title: str, choices_: Iterable[str]) -> urwid.ListBox:

    body = [urwid.Text(title), urwid.Divider()]

    for c in choices_:

        button = urwid.Button(c)

        urwid.connect_signal(button, "click", item_chosen, c)

        body.append(urwid.AttrMap(button, None, focus_map="reversed"))


    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


#Default Sub Menu
def item_chosen(button: urwid.Button, choice: str) -> None:

    response = urwid.Text(["You chose ", choice, "\n"])

    done = urwid.Button("Ok")

    urwid.connect_signal(done, "click", exit_program)

    main.original_widget = urwid.Filler(

        urwid.Pile(

            [

                response,

                urwid.AttrMap(done, None, focus_map="reversed"),

            ]

        )

    )


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

urwid.MainLoop(top, palette=[("reversed", "standout", "")], unhandled_input=exit_on_press).run()