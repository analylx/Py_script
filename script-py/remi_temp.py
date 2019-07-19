import remi.gui as gui
from remi import start, App


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=800, height=400)
        self.lb_version = gui.Label('Version:')
        self.lb_tc = gui.Label('Traffic Class:')
        self.lb_fl = gui.Label('Flow Label:')
        self.lb_pl = gui.Label('Payload Length:')
        self.lb_nh = gui.Label('Next Header:')
        self.lb_sa = gui.Label('Source Address:')
        self.lb_da = gui.Label('Destination Address:')

        self.txt = gui.TextInput(width=200, height=30, margin='10px')

        self.bt_send = gui.Button('Send')
        self.bt_defaut_value = gui.Button('default value')
        self.bt_reset = gui.Button('reset value')

        # setting the listener for the onclick event of the button
        self.bt_send.onclick.connect(self.on_button_pressed)
        self.bt_defaut_value.onclick.connect(self.on_button_pressed2)

        # appending a widget to another, the first argument is a string key
        horizontalContainer = gui.Widget(width='100%', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, margin='0px', style={'display': 'block', 'overflow': 'auto'})
        subContainerLeft = gui.Widget(width=540, margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})
        subContainerLeft.append([self.lb_version,self.lb_tc,self.lb_fl,self.lb_pl,self.lb_nh,self.lb_sa,self.lb_da])
        subContainerRight = gui.Widget(width=540, margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})
        subContainerRight.append([self.bt_send,self.bt_defaut_value,self.bt_reset])
        horizontalContainer.append([subContainerLeft,subContainerRight])
        container.append([horizontalContainer])

        container.append(self.txt)
        container.append(self.bt_send)
        container.append(self.bt_defaut_value)
        container.append(self.bt_reset)

        # returning the root widget
        return container

    # listener function
    def on_button_pressed(self, widget):
        self.lb_version.set_text('Button pressed!')
        self.bt_send.set_text('Hi!')

    def on_button_pressed2(self, widget):
        self.lb_version.set_text('Button 222 pressed!')
        self.bt_send.set_text('22222!')


# starts the web server
start(MyApp)
