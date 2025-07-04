#CONSTANTES


#Colores
BLANCO = (255,255,255)
GRIS_CLARO = (200,200,200)
GRIS_OSCURO = (100,100,100)
NEGRO = (0,0,0)
ROJO = (255,0,0)
CREMA_RELLENO = (239, 239, 220)
CREMA_BORDE = (140, 98, 36)


#Dificultades
FACIL = "Facil"
MEDIO = "Medio"
DIFICIL = "Dificil"
dificultad = FACIL


#Dimensiones
ANCHO = "ancho"
ALTO = "alto"
DIMENSIONES = {ANCHO: 800, ALTO: 600}


#Tablero
MATRIZ = "matriz"
#Datos
DATOS = "datos"
BOMBAS = "bombas"
BANDERAS = "banderas"
ESTADO_PARTIDA = "estado_partida"
#Estados de Partida
VICTORIA = "victoria"
JUGANDO = "jugando"
DERROTA = "derrota"
EN_MENU = "en_menu"
#Celda
RECT = "rect"
BANDERA = "bandera"
VALOR = "valor"
tablero = {}


#SCREENS
INICIO_SCREEN = "inicio"
JUEGO_SCREEN = "juego"
CONFIGURACION_SCREEN = "configuracion"
PUNTAJES_SCREEN = "puntajes"
pantalla_actual = INICIO_SCREEN


#CONFIGURACION DE PANTALLA
VENTANA = "Ventana"
FULLSCREEN = "Fullscreen"
tipo_pantalla = VENTANA


#Titulo
TITULO = ("Buscaminas")


#Timer
TIEMPO_ARRANQUE = "tiempo_arranque"
TIEMPO_TRANSCURRIDO = "tiempo_transcurrido"
TIEMPO_VICTORIA = "tiempo_victoria"
TIEMPO_DERROTA = "tiempo_derrota"
timers = {
    TIEMPO_ARRANQUE : 0,
    TIEMPO_TRANSCURRIDO : 0,
    TIEMPO_VICTORIA : 0,
    TIEMPO_DERROTA : 0,
    }


#Texto
texto_ingresado = ""

#Sonido
volumen_sonido = 0.2