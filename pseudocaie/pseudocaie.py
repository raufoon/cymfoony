from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder

# Define Kivy language string with custom styling
kv_string = '''
<CustomLabelButton>:
    font_size: '20sp'
    background_color: 0, 0.7, 0.3, 1
    size_hint: 0.5, 0.2
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
'''

# Create a custom button class
class CustomLabelButton(Button):
    pass

# Load the Kivy language string and register the custom button class
Builder.load_string(kv_string)
#Builder.load_file("style.kv")  # Alternatively, you can put styling in a separate file

# Create the Kivy App
class MyApp(App):
    def build(self):
        return CustomLabelButton(text='Click me!')

if __name__ == '__main__':
    MyApp().run()
