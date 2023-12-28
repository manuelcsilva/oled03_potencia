def on_logo_pressed():
    global potencia
    kitronik_VIEW128x64.clear()
    potencia = base ** expoente
    kitronik_VIEW128x64.show(potencia,
        2,
        kitronik_VIEW128x64.ShowAlign.CENTRE,
        kitronik_VIEW128x64.FontSelection.BIG)
    for index in range(expoente):
        potencia += base * base
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    global base, potencia
    base += 1
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("" + convert_to_text(base) + " elevado a " + convert_to_text(expoente),
        1,
        kitronik_VIEW128x64.ShowAlign.CENTRE,
        kitronik_VIEW128x64.FontSelection.NORMAL)
    kitronik_VIEW128x64.show(potencia,
        2,
        kitronik_VIEW128x64.ShowAlign.CENTRE,
        kitronik_VIEW128x64.FontSelection.BIG)
    potencia = base ** expoente
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global expoente, base, potencia
    expoente = 0
    base = 0
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("" + convert_to_text(base) + " elevado a " + convert_to_text(expoente),
        1,
        kitronik_VIEW128x64.ShowAlign.CENTRE,
        kitronik_VIEW128x64.FontSelection.NORMAL)
    potencia = base ** expoente
    kitronik_VIEW128x64.show(potencia,
        2,
        kitronik_VIEW128x64.ShowAlign.CENTRE,
        kitronik_VIEW128x64.FontSelection.BIG)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global expoente, potencia
    expoente += 1
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("" + convert_to_text(base) + " elevado a " + convert_to_text(expoente),
        1,
        kitronik_VIEW128x64.ShowAlign.CENTRE,
        kitronik_VIEW128x64.FontSelection.NORMAL)
    kitronik_VIEW128x64.show(potencia,
        2,
        kitronik_VIEW128x64.ShowAlign.CENTRE,
        kitronik_VIEW128x64.FontSelection.BIG)
    potencia = base ** expoente
input.on_button_pressed(Button.B, on_button_pressed_b)

expoente = 0
base = 0
potencia = 0
kitronik_VIEW128x64.show("OLED 03",
    2,
    kitronik_VIEW128x64.ShowAlign.CENTRE,
    kitronik_VIEW128x64.FontSelection.BIG)
kitronik_VIEW128x64.show("Potencia",
    3,
    kitronik_VIEW128x64.ShowAlign.CENTRE,
    kitronik_VIEW128x64.FontSelection.BIG)
basic.pause(2000)
kitronik_VIEW128x64.clear()
potencia = base ** expoente
kitronik_VIEW128x64.show("" + convert_to_text(base) + " elevado a " + convert_to_text(expoente),
    1,
    kitronik_VIEW128x64.ShowAlign.CENTRE,
    kitronik_VIEW128x64.FontSelection.NORMAL)