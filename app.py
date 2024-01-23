from forms import CalculadoraResico
from flask import Flask, render_template, request
import locale

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

@app.template_filter('currency')
def currency(amount):
    locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
    return locale.currency(amount)

@app.route('/', methods=['GET','POST'])
def index():
    form = CalculadoraResico(csrf_enabled=False)
    isr_cargo=0
    print(form.data)
    isr_cargo = int(form.calculo_isr(form.data.get('periodo'),form.data.get('ingreso'),form.data.get('retencion'),form.data.get('provisionales')))
        #if form.validate_on_submit():
     #   calculo = int(form.calculo_isr(form.data.get('periodo'),form.data.get('ingreso'),form.data.get('retencion')),form.data.get('provisionales'))
      #  isr_cargo = calculo if calculo >= 0 else 0        
    return render_template("index.html",template_form=form, isr=isr_cargo)


app.run(host = "localhost",port=5000, debug=True)
