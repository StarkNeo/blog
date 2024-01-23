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
        ingreso = int(request.form.get("ingreso"))
        retencion = int(request.form.get("retencion"))
        provisionales = int(request.form.get("provisionales"))
        isr_cargo = int(form.calculo_isr(periodo, ingreso, retencion, provisionales))
    return render_template("index.html", template_form=form, isr=isr_cargo)
