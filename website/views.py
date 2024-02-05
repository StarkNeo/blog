from flask import Blueprint, render_template, request
from .forms import CalculadoraResico


views = Blueprint("views", __name__)


@views.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@views.route("/facalculator", methods=["GET"])
def facalculator():
    if request.method == "POST":
        data= request.form
        print(data)
    return render_template("software/facalculator.html")


@views.route('/resicopf',methods=['GET'])
def resicopf():
    return render_template("articles/pfresico.html")

@views.route("/calcisresicopf", methods=["GET", "POST"])
def index():
    form = CalculadoraResico(csrf_enabled=False)
    isr_cargo = 0
    mensaje=[]
    provisionales = 0
    if request.method == "POST":
        data = dict(request.form)
        periodo = int(data.get("periodo"))
        ingreso = int(data.get("ingreso"))
        retencion = int(data.get("retencion"))
        provisionales = int('0') if data.get('provisionales') == None else int(data.get('provisionales'))
        calculo = form.calculo_isr(periodo, ingreso, retencion, provisionales)
        isr_cargo =  calculo if calculo >0 else 0
        mensaje =[periodo, ingreso, retencion, provisionales, isr_cargo] 
        
    return render_template("software/calcisresicopf.html", template_form=form, isr=isr_cargo, resultado=mensaje)
