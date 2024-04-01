const app = document.getElementById('typewriter');

const typewriter = new Typewriter(app, {
    loop : true,
    delay: 75
});

typewriter
.typeString('La Ciudad de la Eterna Primavera')
.pauseFor(300)
.start();