
/*DETERMINA QUE CAMPOS APARECEN Y QUE VALORES SE ENVIARAN PARA CALCULO CON BASE EN EL PERIODO QUE SE ELIJA*/
let inputIngreso = document.getElementById('ingreso');
let inputRetencion = document.getElementById('retencion');
let choicePeriodo = document.getElementById('periodo');
let provisionales = document.getElementById('provisionales');
document.addEventListener('click', (e) => {
    let resultadoIsr = document.getElementById('isr-cargo');
    switch (e.target.id) {
        case 'ingreso':
            e.target.value = 0;
            resultadoIsr.value = 0;
            break;
        case 'retencion':
            e.target.value = 0;
            resultadoIsr.value = 0;
            break;
        default:
            break;
    }
})


//FUNCION PARA AGREGAR PROYECTOS AL ARREGLO projects 
/*
function proyecto(nombre, url, descripcion, lenguaje) {
    return {
        nombre: nombre,
        url_imagen: url,
        descripcion: descripcion,
        lenguaje: lenguaje
    }
}

const skill = (imagen, descripcion, link, disenador, otroUno, otroDos, otroTres) => {
    return {
        imagen: imagen,
        descripcion: descripcion,
        link: link,
        disenador: disenador,
        otroUno: otroUno,
        otroDos: otroDos,
        otroTres: otroTres
    }
}


let projects = [
    {
        nombre: 'Podcast Webpage',
        url_imagen: "./images/podcast.png",
        descripcion: '',
        lenguaje: ''
    },
    {
        nombre: 'GIFOS',
        url_imagen: "./images/gifos.png",
        descripcion: '',
        lenguaje: ''
    },
    {
        nombre: 'Costo Patronal',
        url_imagen: "./images/costopatronal.png",
        descripcion: '',
        lenguaje: ''
    },
    {
        nombre: 'Calculo Asimilados',
        url_imagen: "./images/asimilados.png",
        descripcion: '',
        lenguaje: ''
    },
    {
        nombre: 'SuperApp V2',
        url_imagen: "./images/superappV2.png",
        descripcion: '',
        lenguaje: ''
    }
]

let skills = [

]

const cargar = (projects) => {

    let n = 1;
    let arraylength = projects.length;
    console.log(arraylength);
    let nombre = document.querySelector('.proj-Name');
    let imagen = document.querySelector('.proj-img');
    setInterval(() => {

        if (n < arraylength) {
            nombre.innerHTML = projects[n].nombre;
            imagen.src = projects[n].url_imagen;
            n++;
        }
        else if (n === arraylength) {
            n = 0;
        }



    }, 2000);

}

//cargar(projects);

document.addEventListener('click', e => {
    if (e.target.classList[0] === 'fa-solid') {
        let element = e.target.nextElementSibling;
        element.classList.toggle('data-project');

    }

})


let burger = document.getElementById('burger');
let menu = document.querySelector('#main-nav');
let titulo = document.querySelector('#titulo');

burger.addEventListener('click', () => {



    let fig = burger.innerHTML;
    console.log(fig);
    if (fig === '☰') {
        burger.innerHTML = 'x';
        titulo.style.display = 'none';
        menu.style.display = 'flex';

    }
    else {
        burger.innerHTML = '☰';
        titulo.style.display = 'flex';
        menu.style.display = 'none';

    }


});



/*
cuando de un click en la imagen con clase lang-icons
verificar su parentNode
si parentNode es igual a figure
asignale la clase .figure al parent
y a su nextSibling cambia el estilo a display flex
*/
/*
document.addEventListener('click', e => {
    let popUp = e.target.parentNode;
    let caption = e.target.nextElementSibling;
    if (popUp.localName === 'figure') {
        popUp.classList.toggle('figure');
        caption.classList.toggle('figcaption');
    }

})*/