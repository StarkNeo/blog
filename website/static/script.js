
/*DETERMINA QUE CAMPOS APARECEN Y QUE VALORES SE ENVIARAN PARA CALCULO CON BASE EN EL PERIODO QUE SE ELIJA*/
let choicePeriodo = document.getElementById('periodo');
let provisionales = document.getElementById('provisionales');
let submit = document.getElementById('submit');
console.log(choicePeriodo.value)
document.addEventListener('click', (e) => {
    if (e.target.id === 'periodo') {
        if (e.target.value === '1') {
            provisionales.disabled = true;
        } else {
            provisionales.disabled = false;
        }
    }
})

addEventListener('load', () => {
    let choicePeriodo = document.getElementById('periodo');
    let inputIngreso = document.getElementById('ingreso');
    let inputRetencion = document.getElementById('retencion');
    let isr = document.getElementById('isr-cargo');
    choicePeriodo.value = '1';
    inputIngreso.value=0;
    inputRetencion.value=0;
    isr.value=0;
    provisionales.value = 0;
})

