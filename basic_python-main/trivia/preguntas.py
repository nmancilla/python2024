preguntas_basicas = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es la capital de Francia?'],
        'alternativas': [
            ['Madrid', 0], 
            ['París', 1], 
            ['Berlín', 0], 
            ['Roma', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Qué gas es esencial para la respiración humana?'],
        'alternativas': [
            ['Dióxido de carbono', 0], 
            ['Oxígeno', 1], 
            ['Hidrógeno', 0], 
            ['Nitrógeno', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Cuántos continentes hay en el mundo?'],
        'alternativas': [
            ['5', 0], 
            ['7', 1], 
            ['6', 0], 
            ['8', 0]
        ]
    }
}

preguntas_intermedias = {
    'pregunta_1': {
        'enunciado':['¿Quién escribió “Don Quijote de la Mancha”?'],
        'alternativas': [
            ['Gabriel García Márquez', 0], 
            ['Miguel de Cervantes', 1], 
            ['William Shakespeare', 0], 
            ['Julio Cortázar', 0]
        ]
    },
    'pregunta_2': {
        'enunciado':['¿Cuál es el río más largo del mundo?'],
        'alternativas': [
            ['Río Nilo', 0],
            ['Río Amazonas', 1], 
            ['Río Yangtsé', 0], 
            ['Río Misisipi', 0]
        ]
    },
    'pregunta_3': {
        'enunciado':['¿Qué elemento químico tiene el símbolo ‘Au’?'],
        'alternativas': [
            ['Plata', 0], 
            ['Oro', 1], 
            ['Alumino', 0], 
            ['Cobre', 0]
        ]
    }
}

preguntas_avanzadas = {
    'pregunta_1': {
        'enunciado':['¿Cuál es la velocidad de la luz en el vacío?'],
        'alternativas': [
            ['300,000 km/s', 0], 
            ['299,792 km/s', 1], 
            ['150,000 km/s', 0], 
            ['1,000,000 km/s', 0]
        ]
    },
    'pregunta_2': {
        'enunciado':['¿Quién fue el primer ser humano en viajar al espacio?'],
        'alternativas': [
            ['Neil Armstrong', 0], 
            ['Yuri Gagarin', 1], 
            ['John Glenn', 0], 
            ['Alan Shepard', 0]
        ]
    },
    'pregunta_3': {
        'enunciado':['¿Qué teorema establece que en un triángulo rectángulo, el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos?'],
        'alternativas': [
            ['Teorema de Pitágoras', 0], 
            ['Teorema de Euclides', 1], 
            ['Teorema de Thales', 0], 
            ['Teorema de Fermat', 0]
        ]
    }
}

pool_preguntas = {
    'basicas': preguntas_basicas,
    'intermedias': preguntas_intermedias,
    'avanzadas': preguntas_avanzadas
}