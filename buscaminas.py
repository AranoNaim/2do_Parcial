from funciones import *
from constantes import *
import pygame as pg
import pygame.mixer as mixer


pg.init()  
mixer.init()
pantalla = pg.display.set_mode((DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
pg.display.set_caption(TITULO) 


#Imagenes
fondo_inicio = pg.transform.scale(pg.image.load("img/fondo-inicio.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
fondo_configuracion = pg.transform.scale(pg.image.load("img/fondo-configuracion.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
fondo_juego = pg.transform.scale(pg.image.load("img/fondo-juego.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
fondo_victoria = pg.transform.scale(pg.image.load("img/fondo-victoria.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
fondo_puntajes = pg.transform.scale(pg.image.load("img/fondo-puntajes.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
titulo = pg.transform.scale(pg.image.load("img/titulo.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
bandera = pg.transform.scale(pg.image.load("img/bandera.png"), (DIMENSIONES[ANCHO] * 0.05, DIMENSIONES[ANCHO] * 0.05))
bomba = pg.transform.scale(pg.image.load("img/bomba.png"), (DIMENSIONES[ANCHO] * 0.05, DIMENSIONES[ANCHO] * 0.05))

#Rectangulos
rectangulo_x_centrado = (DIMENSIONES[ANCHO] * 0.5) - ((DIMENSIONES[ANCHO] // 4) * 0.5)
rectangulo_chico_x_centrado = (DIMENSIONES[ANCHO] * 0.5) - ((DIMENSIONES[ANCHO] // 7) * 0.5)
rectangulo_y_centrado = (DIMENSIONES[ALTO] * 0.5)
rectangulo_x_izquierda = (DIMENSIONES[ANCHO] * 0.1) - ((DIMENSIONES[ANCHO] // 4) * 0.5)
rectangulo_x_derecha = (DIMENSIONES[ANCHO] * 0.99) - ((DIMENSIONES[ANCHO] // 4) * 0.5)
rectangulo_y_up = (DIMENSIONES[ALTO] * 0.015)
rectangulo_volumen = (DIMENSIONES[ANCHO] * 0.5) - ((DIMENSIONES[ANCHO] // 13) * 0.5)
rectangulo_volumen_mas = (DIMENSIONES[ANCHO] * 0.5) + ((DIMENSIONES[ANCHO] // 4) * 0.5)


#Botones Inicio
boton_jugar = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )
boton_configuracion = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + DIMENSIONES[ALTO] * 0.125, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )
boton_puntajes = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + (DIMENSIONES[ALTO] * 0.125) * 2, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )
boton_salir = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + (DIMENSIONES[ALTO] * 0.125) * 3, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )


#Botones Configuracion
boton_pantalla = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + (DIMENSIONES[ALTO] * 0.125), DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )
boton_volver = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + ( + DIMENSIONES[ALTO] * 0.125) * 3, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 ) #Tambien en puntajes
boton_volumen_menos = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + (DIMENSIONES[ALTO] * 0.125) * 2, DIMENSIONES[ANCHO] // 13, DIMENSIONES[ALTO] // 10)
boton_volumen_pausa = pg.Rect(rectangulo_volumen, rectangulo_y_centrado + (DIMENSIONES[ALTO] * 0.125) * 2, DIMENSIONES[ANCHO] // 13, DIMENSIONES[ALTO] // 10)
boton_volumen_mas = pg.Rect(rectangulo_volumen_mas - DIMENSIONES[ANCHO] // 13, rectangulo_y_centrado + (DIMENSIONES[ALTO] * 0.125) * 2, DIMENSIONES[ANCHO] // 13, DIMENSIONES[ALTO] // 10)


#Botones Juego
boton_volver_juego = pg.Rect(rectangulo_x_izquierda, rectangulo_y_up, DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10 )
boton_facil = pg.Rect(rectangulo_x_izquierda, rectangulo_y_centrado - DIMENSIONES[ALTO] * 0.15, DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10 )
boton_medio = pg.Rect(rectangulo_x_izquierda, rectangulo_y_centrado , DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10 )
boton_dificil = pg.Rect(rectangulo_x_izquierda, rectangulo_y_centrado + DIMENSIONES[ALTO] * 0.15, DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10 )
boton_reiniciar = pg.Rect(rectangulo_chico_x_centrado - DIMENSIONES[ANCHO] * 0.15, rectangulo_y_up, DIMENSIONES[ANCHO] // 7, DIMENSIONES[ALTO] // 10 )
boton_banderas = pg.Rect(rectangulo_chico_x_centrado + DIMENSIONES[ANCHO] * 0.15, rectangulo_y_up, DIMENSIONES[ANCHO] // 7, DIMENSIONES[ALTO] // 10 )
boton_timer = pg.Rect(rectangulo_x_derecha, rectangulo_y_centrado, DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10)
boton_timer_victoria = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado, DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10 )
boton_input = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + DIMENSIONES[ALTO] * 0.25, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )


#Fuente
fuente = pg.font.Font(None, DIMENSIONES[ANCHO] // 25) 
fuente_puntajes = pg.font.Font(None, DIMENSIONES[ANCHO] // 30) 
fuente_titulo = pg.font.Font(None, DIMENSIONES[ANCHO] // 19)


#Textos
jugar = fuente.render("Jugar", True, NEGRO)
config = fuente.render("Configuracion", True, NEGRO)
puntajes = fuente.render("Puntajes", True, NEGRO)
salir = fuente.render("Salir", True, NEGRO)
volver = fuente.render("Volver", True, NEGRO)
texto_pantalla = fuente.render(VENTANA, True, NEGRO)
facil = fuente.render(FACIL, True, NEGRO)
medio = fuente.render(MEDIO, True, NEGRO)
dificil = fuente.render(DIFICIL, True, NEGRO)
banderas = fuente.render("0", True, NEGRO)
reiniciar = fuente.render("Reiniciar", True, NEGRO)
texto_volumen_menos = fuente.render("-", True, NEGRO)
texto_volumen_mas = fuente.render("+", True, NEGRO)

#Bucle Principal
corriendo = True
primer_click = False
sonido_pausado = False

#sonidos
sonido_juego = mixer.Sound('./sonidos/sonido_juego.mp3')
sonido_derrota = mixer.Sound('./sonidos/sonido_derrota.mp3')
sonido_victoria = mixer.Sound('./sonidos/sonido_victoria.mp3')
sonido_juego.play() # REVISAR
sonido_juego.set_volume(volumen_sonido)


dict_puntajes = obtener_puntajes_por_dificultad()
    

while corriendo:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            quit()

        if evento.type == pg.MOUSEBUTTONDOWN:        

            if pantalla_actual == PUNTAJES_SCREEN:
                if evento.button == 1:
                    if boton_volver.collidepoint(evento.pos) == True:
                        pantalla_actual = INICIO_SCREEN


            elif pantalla_actual == INICIO_SCREEN:
                if evento.button == 1:
                    if boton_jugar.collidepoint(evento.pos) == True:
                        tablero = crear_tablero(dificultad, DIMENSIONES[ALTO])
                        pantalla.blit(fondo_juego, (0,0))
                        tablero = dibujar_matriz(DIMENSIONES,tablero,pantalla, GRIS_CLARO, GRIS_OSCURO, NEGRO)
                        pantalla_actual = JUEGO_SCREEN
                    elif boton_puntajes.collidepoint(evento.pos) == True:
                        pantalla_actual = PUNTAJES_SCREEN
                    elif boton_configuracion.collidepoint(evento.pos) == True:
                        pantalla_actual = CONFIGURACION_SCREEN
                    elif boton_salir.collidepoint(evento.pos) == True:
                        pg.quit()
                        quit()
                

            elif pantalla_actual == CONFIGURACION_SCREEN:
                if evento.button == 1:
                    if boton_pantalla.collidepoint(evento.pos) == True:
                        if tipo_pantalla == FULLSCREEN: 
                            tipo_pantalla = VENTANA
                        else:
                            tipo_pantalla = FULLSCREEN                         
                        actualizar_pantalla(tipo_pantalla,pantalla,DIMENSIONES)
                        texto_pantalla = fuente.render(tipo_pantalla, True, NEGRO)
                    elif boton_volver.collidepoint(evento.pos) == True:
                        pantalla_actual = INICIO_SCREEN
                    elif boton_volumen_menos.collidepoint(evento.pos) == True:
                        if volumen_sonido > 0.05:
                            volumen_sonido -= 0.05
                            volumen_sonido = round(volumen_sonido, 2)   # Usamos Round porque sino nos da muchos decimales y no funciona el > 0.05
                        sonido_juego.set_volume(volumen_sonido)
                    elif boton_volumen_mas.collidepoint(evento.pos) == True:
                        if volumen_sonido < 0.4:
                            volumen_sonido += 0.05
                            volumen_sonido = round(volumen_sonido, 2)
                        sonido_juego.set_volume(volumen_sonido)
                    elif boton_volumen_pausa.collidepoint(evento.pos) == True:
                        if sonido_pausado == False:  
                            sonido_juego.set_volume(0)
                            sonido_pausado = True
                        else:
                            sonido_juego.set_volume(volumen_sonido)
                            sonido_pausado = False


                        
            elif pantalla_actual == JUEGO_SCREEN:
                if evento.button == 1:

                    if boton_volver_juego.collidepoint(evento.pos) == True:
                        pantalla_actual = INICIO_SCREEN
                        primer_click = False
                        tablero[DATOS][ESTADO_PARTIDA] = EN_MENU
                        reiniciar_temporizador(timers)

                    elif boton_reiniciar.collidepoint(evento.pos) == True:
                        pantalla.blit(fondo_juego, (0,0))
                        tablero = crear_tablero(dificultad, DIMENSIONES[ALTO])                        
                        tablero = dibujar_matriz(DIMENSIONES,tablero,pantalla, GRIS_CLARO, GRIS_OSCURO, NEGRO)
                        tablero[DATOS][ESTADO_PARTIDA] = JUGANDO
                        primer_click = False
                        reiniciar_temporizador(timers)

                    elif boton_facil.collidepoint(evento.pos) == True:
                        pantalla.blit(fondo_juego, (0,0))
                        dificultad = FACIL
                        tablero = crear_tablero(dificultad, DIMENSIONES[ALTO])                        
                        tablero = dibujar_matriz(DIMENSIONES,tablero,pantalla, GRIS_CLARO, GRIS_OSCURO, NEGRO)
                        tablero[DATOS][ESTADO_PARTIDA] = JUGANDO
                        primer_click = False
                        reiniciar_temporizador(timers)

                    elif boton_medio.collidepoint(evento.pos) == True:
                        pantalla.blit(fondo_juego, (0,0))
                        dificultad = MEDIO
                        tablero = crear_tablero(dificultad, DIMENSIONES[ALTO])
                        tablero = dibujar_matriz(DIMENSIONES,tablero,pantalla, GRIS_CLARO, GRIS_OSCURO, NEGRO)
                        tablero[DATOS][ESTADO_PARTIDA] = JUGANDO
                        primer_click = False
                        reiniciar_temporizador(timers)

                    elif boton_dificil.collidepoint(evento.pos) == True:
                        pantalla.blit(fondo_juego, (0,0)) 
                        dificultad = DIFICIL                       
                        tablero = crear_tablero(dificultad, DIMENSIONES[ALTO])
                        tablero = dibujar_matriz(DIMENSIONES,tablero,pantalla, GRIS_CLARO, GRIS_OSCURO, NEGRO)
                        tablero[DATOS][ESTADO_PARTIDA] = JUGANDO
                        primer_click = False
                        reiniciar_temporizador(timers)

                    if tablero[DATOS][ESTADO_PARTIDA] == JUGANDO:
                        for i in range(len(tablero[MATRIZ])):
                            for j in range(len(tablero[MATRIZ][i])):
                                celda = tablero[MATRIZ][i][j]
                                if celda[RECT].collidepoint(evento.pos) == True and celda[BANDERA] == False:
                                    if primer_click == False:
                                        generar_bombas(tablero, i, j)
                                        primer_click = True
                                        timers[TIEMPO_ARRANQUE] = pg.time.get_ticks()
                                    celda[VALOR] = contar_y_revelar_celda(tablero, i , j, pantalla, GRIS_CLARO, GRIS_OSCURO, bomba)                                    
                                    if tablero[DATOS][ESTADO_PARTIDA] == DERROTA:
                                        mostrar_bombas(tablero, bomba, pantalla, NEGRO, ROJO)
                                        timers[TIEMPO_DERROTA] = pg.time.get_ticks()
                                        sonido_derrota.play()
                                    if verificar_victoria(tablero) and primer_click:
                                        tablero[DATOS][ESTADO_PARTIDA] = VICTORIA
                                        timers[TIEMPO_VICTORIA] = pg.time.get_ticks()
                                        sonido_victoria.play()

                elif evento.button == 3 and tablero[DATOS][ESTADO_PARTIDA] == JUGANDO:
                    for i in range(len(tablero[MATRIZ])):
                        for j in range(len(tablero[MATRIZ][i])):
                            celda = tablero[MATRIZ][i][j]
                            if celda[RECT].collidepoint(evento.pos) == True:
                                tablero[DATOS][BANDERAS] += poner_bandera(pantalla, celda, tablero, GRIS_OSCURO, NEGRO, bandera)   

        if evento.type == pg.KEYDOWN and len(tablero) != 0:
            if tablero[DATOS][ESTADO_PARTIDA] == VICTORIA:
                if evento.key == pg.K_BACKSPACE:
                    texto_ingresado = texto_ingresado[0:-1]

                elif evento.key == pg.K_RETURN or evento.key == pg.K_KP_ENTER:
                    ganador = [texto_ingresado, dificultad, timers[TIEMPO_TRANSCURRIDO]]
                    nombre_existente = False
                    for i in range(len(dict_puntajes[dificultad])):
                        nombre, puntaje = dict_puntajes[dificultad][i]
                        if nombre == texto_ingresado:
                            nombre_existente = True
                            if ganador[2] < puntaje: 
                                dict_puntajes[dificultad][i] = (texto_ingresado, ganador[2])
                            break
                    if not nombre_existente:
                        dict_puntajes[dificultad].append((texto_ingresado, ganador[2]))

                    with open("puntajes.csv", "w") as archivo:
                        archivo.write("NOMBRE,DIFICULTAD,PUNTAJE\n")
                        for dificultad_top in dict_puntajes:
                            for nombre, puntaje in dict_puntajes[dificultad_top]:
                                archivo.write(f"{nombre},{dificultad_top},{puntaje}\n")

                    pantalla_actual = INICIO_SCREEN
                    primer_click = False
                    tablero[DATOS][ESTADO_PARTIDA] = EN_MENU
                    reiniciar_temporizador(timers)
                    texto_ingresado = ""

                else:
                    if len(texto_ingresado) < 10:
                        texto_ingresado += evento.unicode
            

    if pantalla_actual == INICIO_SCREEN:

        pantalla.blit(fondo_inicio, (0,0))
        pantalla.blit(titulo,(DIMENSIONES[ANCHO] * 0.5 - titulo.get_width() * 0.5, (DIMENSIONES[ALTO] * 0.5) * 0.5 - titulo.get_height() * 0.5))
        
        dibujar_boton(pantalla, boton_jugar, GRIS_CLARO)
        dibujar_boton(pantalla, boton_configuracion, GRIS_CLARO)
        dibujar_boton(pantalla, boton_puntajes, GRIS_CLARO)
        dibujar_boton(pantalla, boton_salir, GRIS_CLARO)

        centrar_en_boton(pantalla, jugar, boton_jugar)
        centrar_en_boton(pantalla, config, boton_configuracion)
        centrar_en_boton(pantalla, puntajes, boton_puntajes)
        centrar_en_boton(pantalla, salir, boton_salir)


    elif pantalla_actual == JUEGO_SCREEN:
        
        timer = fuente_titulo.render(str(timers[TIEMPO_TRANSCURRIDO]), True, NEGRO)
        usuario = fuente.render(str(texto_ingresado), True, NEGRO)
        
        dibujar_boton(pantalla, boton_volver_juego, GRIS_CLARO)
        dibujar_boton(pantalla, boton_facil, GRIS_CLARO)
        dibujar_boton(pantalla, boton_medio, GRIS_CLARO)
        dibujar_boton(pantalla, boton_dificil, GRIS_CLARO)
        dibujar_boton(pantalla, boton_reiniciar, GRIS_CLARO)
        dibujar_boton(pantalla, boton_banderas, GRIS_CLARO)
        dibujar_boton(pantalla, boton_timer, GRIS_CLARO)


        icono_y_texto_en_boton(pantalla, tablero, bandera, boton_banderas, NEGRO)
        centrar_en_boton(pantalla, volver, boton_volver_juego)
        centrar_en_boton(pantalla, facil, boton_facil)
        centrar_en_boton(pantalla, medio, boton_medio)
        centrar_en_boton(pantalla, dificil, boton_dificil)
        centrar_en_boton(pantalla, reiniciar, boton_reiniciar)
        centrar_en_boton(pantalla, timer, boton_timer)

        timers[TIEMPO_TRANSCURRIDO] = cronometrar_juego(timers)

        if tablero[DATOS][ESTADO_PARTIDA] == VICTORIA:
            pantalla.blit(fondo_victoria, (0,0))
            pantalla.blit(timer, (DIMENSIONES[ANCHO] * 0.5 - timer.get_width() * 0.5, DIMENSIONES[ALTO] * 0.575 - timer.get_height() * 0.5)) 
            boton_input = renderizar_input(usuario, DIMENSIONES)
            dibujar_boton(pantalla, boton_input, CREMA_RELLENO)
            pg.draw.rect(pantalla, CREMA_BORDE, boton_input, 2, 10)
            centrar_en_boton(pantalla, usuario, boton_input)
        

    elif pantalla_actual == CONFIGURACION_SCREEN:

        pantalla.blit(fondo_configuracion, (0,0))

        if sonido_juego.get_volume() == 0:
            texto_volumen_pausa = fuente.render("Play", True, NEGRO)
        else:
            texto_volumen_pausa = fuente.render("Mute", True, NEGRO)

        dibujar_boton(pantalla, boton_pantalla, GRIS_CLARO)
        dibujar_boton(pantalla, boton_volver, GRIS_CLARO)
        dibujar_boton(pantalla, boton_volumen_menos, GRIS_CLARO)
        dibujar_boton(pantalla, boton_volumen_pausa, GRIS_CLARO)
        dibujar_boton(pantalla, boton_volumen_mas, GRIS_CLARO)
        centrar_en_boton(pantalla, texto_volumen_menos, boton_volumen_menos)
        centrar_en_boton(pantalla, texto_volumen_pausa, boton_volumen_pausa)
        centrar_en_boton(pantalla, texto_volumen_mas, boton_volumen_mas)
        centrar_en_boton(pantalla, texto_pantalla, boton_pantalla)
        centrar_en_boton(pantalla, volver, boton_volver)

        



    elif pantalla_actual == PUNTAJES_SCREEN:
        
        pantalla.blit(fondo_puntajes, (0,0))

        dibujar_boton(pantalla, boton_volver, GRIS_CLARO)
        centrar_en_boton(pantalla, volver, boton_volver)
        tops = hacer_top_puntajes(dict_puntajes)
        renderizar_puntajes(pantalla,fuente_puntajes,tops,NEGRO,DIMENSIONES)

        

    pg.display.flip()
    pg.display.update()