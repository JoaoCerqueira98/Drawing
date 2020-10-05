import core, guizero

app= guizero.App(title="Drawing Machine 1.0")
text_foto = guizero.Text(app, text="Aperte o Botão para tirar a foto")
tirar_foto = guizero.PushButton(app,command=core.foto(),text="Tirar Foto")

app.display()