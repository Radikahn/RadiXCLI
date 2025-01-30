from __future__ import print_function, absolute_import, division
import urwid


def show_or_exit(key):

    if key == "esc":
        raise urwid.ExitMainLoop()
        
    

def name_changed(w, x):
    header.set_text('Hello % s!' % x)

def save_data(text: str):
    file = open("radix_paths.txt", "w")
    file.write(text)
    file.close()


if __name__ == '__main__':
    name_edit = urwid.Edit("Name: ")
    header = urwid.Text('Fill your details')
    enter_button = urwid.Button("Enter")
    widget = urwid.Pile([
        urwid.Padding(header, 'center', width=('relative', 6)),
        name_edit,
        urwid.Edit('Address: '),
        enter_button
    ])
    urwid.connect_signal(name_edit, 'change', name_changed)
    urwid.connect_signal(enter_button, 'click', save_data("hello_"))

    widget = urwid.Filler(widget, 'top')
    loop = urwid.MainLoop(widget, unhandled_input=show_or_exit)
    loop.run()