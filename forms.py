from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, IntegerField,validators, RadioField
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
    submit = SubmitField('Calcular')
    periodo = RadioField('Periodo de calculo', choices=[('1','Mensual'),('2','Anual')], render_kw={'id':'periodo'}, default='1')
    provisionales = IntegerField('Pagos realizados',default=0, validators=[DataRequired(),validators.NumberRange(min=0)], render_kw={'id':'provisionales'})
    #resultado = Field('impuesto',render_kw={'disabled':True})
    
    def calculo_isr(self,periodo, ingreso=0, retencion=0, provisionales=0):
        if periodo == '1':
            for limite in tabla_mensual:
                if ingreso <= limite[0]:
                    return (ingreso * limite[1])-retencion
        else:
            for limite in tabla_anual:
                if ingreso <= limite[0]:
                    return (ingreso * limite[1])-provisionales
    