input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("" + convertToText(base) + " elevado a " + convertToText(expoente), 1, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Normal)
    for (let index = 0; index < expoente; index++) {
        potencia += base * base
    }
    kitronik_VIEW128x64.show(potencia, 2, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Big)
})
input.onButtonPressed(Button.A, function () {
    base += 1
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("" + convertToText(base) + " elevado a " + convertToText(expoente), 1, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Normal)
    kitronik_VIEW128x64.show(potencia, 2, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Big)
    for (let index = 0; index < expoente; index++) {
        potencia += base * base
    }
})
input.onButtonPressed(Button.AB, function () {
    expoente = 0
    base = 0
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("" + convertToText(base) + " elevado a " + convertToText(expoente), 1, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Normal)
    for (let index = 0; index < expoente; index++) {
        potencia += base * base
    }
    kitronik_VIEW128x64.show(potencia, 2, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Big)
})
input.onButtonPressed(Button.B, function () {
    expoente += 1
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("" + convertToText(base) + " elevado a " + convertToText(expoente), 1, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Normal)
    kitronik_VIEW128x64.show(potencia, 2, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Big)
    for (let index = 0; index < expoente; index++) {
        potencia += base * base
    }
})
let base = 0
let potencia = 0
let expoente = 0
kitronik_VIEW128x64.show("OLED 03", 2, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Big)
kitronik_VIEW128x64.show("Potencia", 3, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Big)
basic.pause(2000)
kitronik_VIEW128x64.clear()
for (let index = 0; index < expoente; index++) {
    potencia += base * base
}
kitronik_VIEW128x64.show("" + convertToText(base) + " elevado a " + convertToText(expoente), 1, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Normal)
