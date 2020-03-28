from flask import Flask, render_template


app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
   return "Home Page"

# Routes to Render Something
@app.route('/')
def home():
  return render_template("home.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)

"""
class validar():
    def __init__(self):
        print("Validar contraseña...\n")
    def validar(self):
        self.passw = str(input("ingrese la contraseña: "))
        self.patron = r"^[A-Z][0-9][0-9][0-9][a-z][a-z][a-z][!@#$%^&*(),.¿!?:{}|<>]$"
        self.response = bool(re.search(self.patron, self.passw))
        if (self.response):
            print("La contraseña es correcta \n")
            self.sw = str(input("Desea continuar?[s/n]"))
            return self.sw
        else:
            print("Contraseña incorrecta \n")
            self.sw = str(input("Desea continuar?[s/n]"))
    app = validarPass() """