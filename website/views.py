from flask import Blueprint, render_template, request
from .forms import CalculadoraResico


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def index():
    form = CalculadoraResico(csrf_enabled=False)
    isr_cargo = 0
    print(form.data)
    if request.method == "POST":
        periodo = request.form.get("periodo")
        ingreso = request.form.get("ingreso")
        retencion = request.form.get("retencion")
        provisionales = request.form.get("provisionales")
        calculo = int(form.calculo_isr(periodo, ingreso, retencion, provisionales))
        isr_cargo =  calculo if calculo>=0 else 0
    return render_template("index.html", template_form=form, isr=isr_cargo)
