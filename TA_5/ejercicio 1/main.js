const contenido =document.getElementById("contenido")


let nombre="Brigner Carriel";
let edad = 19;

let edades=[23,45,2,42,82];

addContent(`<h2>${nombre}</h2><h3>${edad}</h3>`);

for(let i = 0; i< edades.length; i++){
    addContent(`<h3>La edad es de ${edades[i]}</h3>`);
}

function addContent(newContent){
    contenido.innerHTML += newContent
}