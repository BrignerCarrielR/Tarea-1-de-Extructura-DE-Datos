
const contenido=document.getElementById("contenido");

let nombre='Daniel Vera';
let correo='dverap@unemi.edu.ec';
let mensaje='Buen Trabajo..';
contenido.innerHTML= nombre +", revise su correo=> "+correo+" para confirmar su registro, gracias por su comentario: "+"'" +mensaje+"'.";



document.getElementById('datos').addEventListener('submit',function(){
    alert('enviando fotmulario')
})
