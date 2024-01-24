from flask import Blueprint, render_template, request
from .forms import CalculadoraResico


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def index():
    form = CalculadoraResico(csrf_enabled=False)
    isr_cargo = 0
    mensaje=[]
    if request.method == "POST":
        data = dict(request.form)
        periodo = int(data.get("periodo"))
        ingreso = int(data.get("ingreso"))
        retencion = int(data.get("retencion"))
        provisionales = int(data.get('provisionales')) if type(data.get('provisionales')) == 'str' else 0
        calculo = form.calculo_isr(periodo, ingreso, retencion, provisionales)
        isr_cargo =  calculo if calculo >0 else 0
        mensaje =[periodo, ingreso, retencion, provisionales, isr_cargo] 
        
    return render_template("index.html", template_form=form, isr=isr_cargo, resultado=mensaje)
