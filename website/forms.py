from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, IntegerField,validators, SelectField
from wtforms.validators import DataRequired

tabla_mensual=[
    (25000,0.01),
    (50000,0.0110),
    (83333.33,0.0150),
    (208333.33,0.02),
    (3500000,0.025)
    ]

tabla_anual =[
    (300000,0.01),
    (600000,0.0110),
    (1000000,0.0150),
    (2500000,0.02),
    (3500000,0.025)
]

class CalculadoraResico(FlaskForm):
    ingreso =  IntegerField('Ingreso',default=0, validators=[DataRequired(),validators.NumberRange(min=0)], render_kw={'id':'ingreso'})
    retencion = IntegerField('Retencion de PM', default=0,validators=[validators.NumberRange(min=0)], render_kw={'id':'retencion'})
    submit = SubmitField('Calcular', render_kw={'id':'calcular'})
    provisionales = IntegerField('Pagos realizados',default=0, validators=[DataRequired(),validators.NumberRange(min=0)], render_kw={'id':'provisionales','disabled':'true'})
    periodo = SelectField('periodo', choices=[('1','Mensual'),('2','Anual')], render_kw={'id':'periodo'},default='1')
    #provisionales = IntegerField('Pagos realizados',default=0, validators=[DataRequired(),validators.NumberRange(min=0)], render_kw={'id':'provisionales', 'disabled':'true'})
    #resultado = Field('impuesto',render_kw={'disabled':True})
    #periodo = RadioField('Periodo de calculo', choices=[('1','Mensual'),('2','Anual')], render_kw={'id':'periodo'}, default='1')
    #periodo = RadioField('Periodo de calculo', choices=('1','Mensual'), render_kw={'id':'periodo'}, default='1')
    
    def calculo_isr(self,periodo, ingreso, retencion, provisionales):
        if periodo == 1:
            for limite in tabla_mensual:
                if ingreso <= limite[0]:
                    return int(ingreso * limite[1]-retencion)
        else:
            for limite in tabla_anual:
                if ingreso <= limite[0]:
                    return int(ingreso * limite[1]-retencion-provisionales)
    