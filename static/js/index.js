$(document).ready(function () {

        let cuadro = $("#cuadroBlanco");
        
        //cuadro.animate({height: '600px', opacity: '1'}, "slow");
        cuadro.animate({height: '600px', opacity: '1'}, "slow");

        /*
        let titulo = $('#textoAnimado');
        let letras = $('#tituloAnimado')
        titulo.typeIt();
        letras.typeIt();
        */
        new TypeIt('#tituloAnimado', {
                speed: 50,
                startDelay: 900,
                cursor: false
                })
                .type("<h1 class='text-center text-primary'> PRIORIDADES</h1>")
                .pause(500) // Pausa después de escribir el título
                .exec(async () => {
                // Una vez que el título ha terminado, empieza a escribir el texto
                new TypeIt('#textoAnimado', {
                        speed: 50,
                        startDelay: 100,
                        cursor: false
                })
                .type('<h4><b>1.</b> Enfocate en el funcionamiento del sistema <br> <b>2.</b> Enfocate en la escritura de la tesis <br> <b>3.</b> Enfocate en el diseño del sistema  </h4>')
                .go();
              })
              .go();

    

});