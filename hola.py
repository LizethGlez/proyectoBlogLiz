from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("template.html", nombre="Lizeth", bienvenida="Hola, y bienvenido a mi blog.", about="Sobre mi...")

@app.route("/librosJ")
def url_librosJ():
 	tipos = [
 		"El psicoanalísta",
 		"Jaque al psicoanalísta",
 		"Un final perfecto",
 		"La historia del loco"
 	]
 	return render_template("librosJ.html", tipos=tipos, nombre="Titulos")

if __name__=="__main__":
	app.run(debug=True)