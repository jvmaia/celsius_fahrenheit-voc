import android
from android.widget import Button, LinearLayout, TextView, EditText
from android.view import Gravity

class ButtonClick(implements=android.view.View[OnClickListener]):
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def onClick(self, view: android.view.View) -> void:
        self.callback(*self.args, **self.kwargs)

class MainApp:
    def __init__(self):
        self._activity = android.PythonActivity.setListener(self)

    def onCreate(self):
        vlayout = LinearLayout(self._activity)
        vlayout.setOrientation(LinearLayout.VERTICAL)

        self.entry = EditText(self._activity)
        self.entry.setInputType(0x00000002 | 0x00002000 | 0x00001000)
        self.entry.setGravity(Gravity.CENTER)
        vlayout.addView(self.entry)

        hlayout = LinearLayout(self._activity)
        hlayout.setOrientation(LinearLayout.HORIZONTAL)
        hlayout.setGravity(Gravity.CENTER)

        self.convert_to_fahrenheit = Button(self._activity)
        self.convert_to_fahrenheit.setOnClickListener(ButtonClick(self.to_fahrenheit))
        self.convert_to_fahrenheit.setText('To Fahrenheit')
        hlayout.addView(self.convert_to_fahrenheit)

        self.convert_to_celsius = Button(self._activity)
        self.convert_to_celsius.setOnClickListener(ButtonClick(self.to_celsius))
        self.convert_to_celsius.setText('To Celsius')
        hlayout.addView(self.convert_to_celsius)

        vlayout.addView(hlayout)

        self.result = TextView(self._activity)
        self.result.setTextSize(26)
        self.result.setText('Convert units')
        self.result.setGravity(Gravity.CENTER)
        vlayout.addView(self.result)

        self._activity.setContentView(vlayout)

    def to_celsius(self):
        fahrenheit = str(self.entry.getText())
        if len(fahrenheit) == 0:
            self.result.setText('Please enter a valid number!')
            return
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit-32.0) / 1.8
        self.result.setText('Celsius: %.2f'%(celsius))

    def to_fahrenheit(self):
        celsius = str(self.entry.getText())
        if len(celsius) == 0:
            self.result.setText('Please enter a valid number!')
            return
        celsius = float(celsius)
        fahrenheit = celsius * 1.8 + 32.0
        self.result.setText('Fahrenheit: %.2f'%(fahrenheit))

def main():
    MainApp()
