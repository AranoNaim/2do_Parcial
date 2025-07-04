import random
import pygame as pg

pg.init()


def generar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial:any ="") -> list:

    """
    Genera una matriz.
    Parametro:
        cantidad_filas (int): la cantidad de filas para la matriz.
        cantidad_columnas (int): la cantidad de columnas para la matriz.
        valor_inicial (any): de los valores de la matriz.
    Retorna:
        Lista (list): una lista determinada por los parametros.
    """
    
    matriz = [] 

    for _ in range(cantidad_filas):
        filas = [valor_inicial] * cantidad_columnas
        matriz += [filas] 
    return matriz


def mostrar_matriz(matriz:list)-> None:

    """
    Recorre cada elemento de la matriz y lo muestra por consola.
    Parametro:
        matriz (list): la lista a recorrer.
    Retorna:
        Nada.
    """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = ' ')
        print()


def generar_bombas (tablero:dict, i:int, j:int) -> None:

    """
    Genera bombas en un dict.
    Parametro:
        tablero (dict): el tablero del juego.
        i (int): posicion x donde se clickeo en el tablero.
        j (int): posicion y donde se clickeo en el tablero.
    Retorna:
        Nada.
    """

    filas = tablero["datos"]["filas"]
    columnas = tablero["datos"]["columnas"]
    bombas_colocadas = 0


    while bombas_colocadas < tablero["datos"]["bombas"]:
        f = random.randint(0, filas - 1)
        c = random.randint(0, columnas - 1)

        es_celda_adyacente = False
        if (f >= i - 1 and f <= i + 1) and (c >= j - 1 and c <= j + 1):
            es_celda_adyacente = True


        if tablero["matriz"][f][c]["valor"] != "X" and tablero["matriz"][f][c] != tablero["matriz"][i][j] and es_celda_adyacente == False:
            tablero["matriz"][f][c]["valor"] = "X"
            bombas_colocadas += 1


def contar_y_revelar_celda(tablero:dict, i:int , j:int, pantalla:pg.Surface, color_relleno:tuple, color_borde:tuple, bomba:pg.Surface)-> any:

    """
    Revela y cuenta las bombas adyacentes de la celda en la que se hizo click. 
    Es una funcion recursiva que en caso de no encontrar bombas adyacentes se vuelve a llama
    Parametro:
        tablero (dict): el tablero del juego.
        i (int): posicion x donde se clickeo en el tablero.
        j (int): posicion y donde se clickeo en el tablero.
        pantalla (pygame Surface): la pantalla del juego.
        color_relleno (tuple): color que va a rellenar la celda.
        color_borde (tuple): color que va a bordear la celda.
        bomba (pygame Surface): es la imagen de la bomba que se renderizara en el tablero en caso de clickear una.
    Retorna:
        retorno (Any): retorna el valor de la celda contada, puede ser un int o un string en caso de ser una bomba.
    """

    matriz = tablero["matriz"]
    celda_rect = matriz[i][j]["rect"]
    filas = len(matriz)
    columnas = len(matriz[0])
    bombas = 0
    retorno = None
    colores_cuenta_minas = [(0,0,255),(0,128,0),(255,0,0),(0,0,128),(128,0,0),(0,128,128),(0,0,0),(128,128,128)]

    if matriz[i][j]["revelada"] == True:
        retorno = matriz[i][j]["valor"]
    elif matriz[i][j]["valor"] == "X":
        pg.draw.rect(pantalla, color_relleno, celda_rect)    
        pg.draw.rect(pantalla, color_borde, celda_rect, 1)            
        bomba_escalada = pg.transform.scale(bomba, (tablero["datos"]["alto_celda"] * 0.75, tablero["datos"]["alto_celda"] * 0.75))
        pantalla.blit(bomba_escalada, (celda_rect.x + celda_rect.w // 2 - bomba_escalada.get_width() // 2, celda_rect.y  + celda_rect.h // 2 - bomba_escalada.get_height() // 2))
        matriz[i][j]["revelada"] = True
        tablero["datos"]["estado_partida"] = "derrota"
        retorno = "X" 
    else:
        matriz[i][j]["valor"] = 0
        matriz[i][j]["revelada"] = True
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if (0 <= k and k < filas) and (0 <= l and l < columnas):
                    if (k != i or l != j) and matriz[k][l]["valor"] == "X":
                        bombas += 1
                            
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if (0 <= k and k < filas) and (0 <= l and l < columnas):
                    if bombas == 0 and matriz[i][j]["revelada"] == True and matriz[i][j]["valor"] == 0 and matriz[k][l]["bandera"] == False:
                        matriz[k][l]["valor"] = contar_y_revelar_celda(tablero, k, l, pantalla, color_relleno, color_borde, bomba)
                    
        pg.draw.rect(pantalla, color_relleno, celda_rect)
        pg.draw.rect(pantalla, color_borde, celda_rect, 1)

        if bombas != 0:
            fuente = pg.font.Font(None, int(tablero["datos"]["ancho_celda"] * 0.9)) 
            texto_celda = fuente.render(str(bombas), True, colores_cuenta_minas[bombas - 1])
            pantalla.blit(texto_celda, (celda_rect.x + celda_rect.w // 2 - texto_celda.get_width() // 2, celda_rect.y  + celda_rect.h // 2 - texto_celda.get_height() // 2)) 
    
        retorno = bombas

    return retorno                        


def crear_tablero(dificultad:str, dimensiones_alto:int) -> dict:

    """
    Crea el tablero que se usara en el juego y una serie de datos que luego se iran utilizando.
    Parametro:
        dificultad (str): string que corresponde a la dificultad que tendra el juego
        dimensiones_alto (int): entero que sera el alto total de la pantalla del juego
    Retorna:
        tablero (dict): retorna el tablero.
    """

    match dificultad:
        case "Facil":
            columnas = 8
            filas = 8
            bombas = 10
            banderas = 10
        case "Medio":
            columnas = 16
            filas = 16
            bombas = 50
            banderas = 50
        case "Dificil":
            columnas = 24
            filas = 24
            bombas = 120
            banderas = 120
        case _:
            print("ERROR")

    ancho_celda = dimensiones_alto * 0.85 // columnas
    alto_celda = dimensiones_alto * 0.85 // columnas

    matriz = generar_matriz(columnas, filas, "")

    tablero = {
            "matriz": matriz,
            "datos": {
                "ancho_celda" : ancho_celda,
                "alto_celda" : alto_celda,
                "bombas": bombas,
                "banderas": banderas,
                "columnas":columnas,
                "filas": filas,
                "estado_partida": "jugando"
                }
            }

    return tablero


def dibujar_matriz(dimensiones:dict, tablero:dict, pantalla:pg.Surface, color_matriz:tuple, color_relleno_celda:tuple, color_borde_celda:tuple) -> dict:

    """
    Renderiza la matriz del talbero teniendo en cuenta las dimensiones de la pantalla,
    ademas de renderizar cada celda y a esa posicion en la matriz del tablero crear un objeto celda con los distintos datos de esta.
    Parametro:
        dimensiones (dict): diccionario que tiene las distintas dimensiones de la pantalla.
        tablero (dict): tablero del juego.
        pantalla (pygame Surface): pantalla del juego.
        color_matriz (tuple): color que tendra el relleno de la martiz.
        color_relleno_celda (tuple): color que tendra el relleno de la celda.
        color_borde_celda (tuple): color que tendra el borde de la martiz.
    Retorna:
        tablero (dict): retorna el tablero.
    """

    ancho_matriz = tablero["datos"]["columnas"] * tablero["datos"]["ancho_celda"]   
    alto_matriz = tablero["datos"]["filas"] * tablero["datos"]["alto_celda"]

    margen_x = (dimensiones["ancho"] - ancho_matriz) // 2
    margen_y = dimensiones["alto"] * 0.1 + (dimensiones["alto"] * 0.90 - alto_matriz) // 2

    pg.draw.rect(pantalla, color_matriz, (margen_x, margen_y, ancho_matriz, alto_matriz))
    for i in range(len(tablero["matriz"])):
        for j in range(len(tablero["matriz"][0])):
            x = j * tablero["datos"]["ancho_celda"] + margen_x
            y = i * tablero["datos"]["alto_celda"] + margen_y
            rect_celda = pg.Rect(x, y, tablero["datos"]["ancho_celda"], tablero["datos"]["alto_celda"])
            pg.draw.rect(pantalla, color_relleno_celda, rect_celda)
            pg.draw.rect(pantalla, color_borde_celda, rect_celda, 1)
            celda = {
                "valor": tablero["matriz"][i][j],
                "revelada": False,
                "rect": rect_celda,
                "bandera": False
                }
            tablero["matriz"][i][j] = celda

    return tablero


def actualizar_pantalla(tipo_pantalla:str, pantalla:pg.Surface, dimensiones:dict) -> None:

    """
    Actualiza el tipo de pantalla pudiendo ser Ventana o FullScreen
    Parametro:
        tipo_pantalla (str): string que determinara el tipo de la pantalla a la cual se va a cambiar.
        pantalla (pygame Surface): pantalla del juego.
        dimensiones (dict): diccionario que tiene las distintas dimensiones de la pantalla.
    Retorna:
        Nada.
    """

    if tipo_pantalla == "Fullscreen":
        pantalla = pg.display.set_mode((dimensiones["ancho"], dimensiones["alto"]), pg.FULLSCREEN)
    elif tipo_pantalla == "Ventana":
        pantalla = pg.display.set_mode((dimensiones["ancho"], dimensiones["alto"]))
    

def dibujar_boton(pantalla:pg.Surface, boton:pg.Rect, color_boton:tuple) -> None:

    """
    Dibuja el boton en la pantalla
    Parametro:
        pantalla (pygame Surface): pantalla del juego.
        boton (pygame Rect): boton con medidas ya determinadas.
        color_boton (tuple): color que tendra el boton.
    Retorna:
        Nada.
    """

    pg.draw.rect(pantalla, color_boton, boton, border_radius = 10)


def centrar_en_boton(pantalla:pg.Surface, relleno:pg.Surface, boton:pg.Rect) -> None:

    """
    Centra en el boton, el relleno pasado por parametro
    Parametro:
        pantalla (pygame Surface): pantalla del juego.
        relleno (pygame Surface): texto que se imprimira en el boton.
        boton (pygame Rect): boton con medidas ya determinadas.
    Retorna:
        Nada.
    """
    
    pantalla.blit(relleno, (boton.x + boton.w // 2 - relleno.get_width() // 2, boton.y  + boton.h // 2 - relleno.get_height() // 2)) 


def icono_y_texto_en_boton(pantalla:pg.Surface, tablero:pg.Surface, icono:pg.Surface, boton:pg.Rect, color:tuple) -> None:

    """
    Pone en un boton un icono y un texto
    Parametro:
        pantalla (pygame Surface): pantalla del juego.
        tablero (dict): tablero del juego.
        icono (pygame Surface): imagen que se renderizara segun el tamaño en el boton.
        boton (pygame Rect): boton con medidas ya determinadas.
        color (tuple): color que tendra el texto.
    Retorna:
        Nada.
    """

    fuente = pg.font.Font(None, int(tablero["datos"]["columnas"] * tablero["datos"]["ancho_celda"]  * 0.085)) 
    relleno = fuente.render(str(tablero["datos"]["banderas"]), True, color)

    pantalla.blit(relleno, (boton.x + boton.w // 2 - icono.get_width(), boton.y  + boton.h // 2 - relleno.get_height() // 2)) 
    pantalla.blit(icono, (boton.x + boton.w // 2 + icono.get_width() * 0.25, boton.y  + boton.h // 2 - icono.get_height() // 2))


def poner_bandera(pantalla:pg.Surface, celda:dict, tablero:dict, color_relleno:tuple, color_borde:tuple, bandera:pg.Surface) ->int:

    """
    Pone o saca una bandera en la celda
    Parametro:
        pantalla (pygame Surface): pantalla del juego.
        celda (dict): celda en la cual se renderizara la bandera.
        tablero (dict): tablero del juego.
        color_relleno (tuple): color que tendra el relleno de la celda.
        color_borde (tuple): color que tendra el borde de la martiz.
        bandera (pygame Surface): es la imagen de la bandera que se renderizara.
    Retorna:
        retorno (int) = retorna -1 en caso de agregar una bandera y 1 en caso de sacarla.
    """

    bandera_escalada = pg.transform.scale(bandera, (tablero["datos"]["alto_celda"] * 0.75, tablero["datos"]["alto_celda"] * 0.75))

    retorno = 0

    if celda["revelada"] == False and celda["bandera"] == False:
        if tablero["datos"]["banderas"] > 0:
            celda["bandera"] = True
            pantalla.blit(bandera_escalada, (celda["rect"].x + celda["rect"].w // 2 - bandera_escalada.get_width() // 2, celda["rect"].y  + celda["rect"].h // 2 - bandera_escalada.get_height() // 2))
            retorno = -1
    elif celda["bandera"] == True:
        celda["bandera"] = False
        pg.draw.rect(pantalla, color_relleno, celda["rect"])
        pg.draw.rect(pantalla, color_borde, celda["rect"], 1)
        retorno = 1
    
    return retorno


def verificar_victoria(tablero:dict) -> bool:

    """
    Verifica si la partida fue ganada o no.
    Parametro:
        tablero (dict): tablero del juego.
    Retorna:
        retorno (bool) = retorna True en caso de ganar y False en caso de seguir.
    """
    
    retorno = True

    for i in range(len(tablero["matriz"])):
        for j in range(len(tablero["matriz"][i])):
            celda = tablero["matriz"][i][j]
            if celda["valor"] != "X" and celda["revelada"] == False:
                retorno = False

    return retorno


def mostrar_bombas(tablero:dict,bomba:pg.Surface, pantalla:pg.Surface, color_borde:tuple, color_relleno:tuple) -> None:

    """
    En caso de derrota muestra todas las bombas.
    Parametro:
        tablero (dict): tablero del juego.
        bomba (pygame Surface): es la imagen de la bomba que se renderizara en el tablero en caso de clickear una.
        pantalla (pygame Surface): pantalla del juego.
        color_borde (tuple): color que tendra el borde de la martiz.
        color_relleno (tuple): color que tendra el relleno de la celda.
    Retorna:
        Nada.
    """

    for i in range(len(tablero["matriz"])):
        for j in range(len(tablero["matriz"][i])):
            valor_bomba = tablero["matriz"][i][j]
            if valor_bomba["valor"] == "X":
                rect = valor_bomba["rect"]
                pg.draw.rect(pantalla, color_relleno, rect) 
                pg.draw.rect(pantalla, color_borde, rect, 1)  
                bomba_escalada = pg.transform.scale(bomba, (tablero["datos"]["alto_celda"] * 0.75, tablero["datos"]["alto_celda"] * 0.75))
                pantalla.blit(bomba_escalada, (rect.x + rect.w // 2 - bomba_escalada.get_width() // 2,rect.y + rect.h // 2 - bomba_escalada.get_height() // 2))


def reiniciar_temporizador(timers:dict) -> None:

    """
    Reestablece todos los timers a 0.
    Parametro:
        timers (dict): un diccionario con todos los timeres dentro
    Retorna:
        Nada.
    """

    for tiempo in timers:
        timers[tiempo] = 0
    

def obtener_puntajes_por_dificultad() -> dict:
    
    """
    Busca en un archivo ".csv" los distintos puntajes y nombres y lo retorna en un diccionario.
    Parametro:
        Ninguno.
    Retorna:
        resultado (dict): diccionario donde estan separados por 3 listas los distintos top 5 de cada dificultad.
    """
    
    resultado = {"Facil": [], "Medio": [], "Dificil": []}

    with open("puntajes.csv", "r") as puntajes:
        next(puntajes)
        for linea in puntajes:
            nombre, dificultad, puntaje = linea.strip().split(",")
            puntaje = int(puntaje)
            if dificultad in resultado:
                resultado[dificultad].append((nombre, puntaje ))

    return resultado


def hacer_top_puntajes(puntajes:dict) -> dict: # HACER DOCUMENTACION

    """"""

    titulos = ["Facil", "Medio", "Dificil"]
    resultado = {}

    for i in range(len(titulos)):
        titulo = titulos[i]
        lista = puntajes.get(titulo, [])

        for i in range(len(lista)):
            for j in range(0,len(lista) -1 - i):
                if lista[j][1] > lista[j + 1][1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        resultado[titulo] = lista[:5]

    return resultado




def renderizar_puntajes(pantalla:pg.Surface, fuente:pg.font.Font, puntajes:dict, color:tuple, dimensiones:dict) -> None:
    
    """
    Renderiza en 3 distintas columnas los distintos top 5 de los puntajes segun dificultad.
    Parametro:
        pantalla (pygame Surface): pantalla del juego.
        fuente (pygame font Font): fuente que se usara para renderizar los distintos puntajes.
        puntajes (dict): diccionario de distintos top5 de puntajes segun dificultad.
        color (tuple): color que tendra el texto.
        dimensiones (dict): diccionario con las distintas dimensiones de la pantalla
    Retorna:
        Nada.
    """

    posiciones_x = [
        dimensiones["ancho"] * 0.2,       
        dimensiones["ancho"] * 0.5,       
        dimensiones["ancho"] * 0.8      
    ]

    titulos = ["Facil", "Medio", "Dificil"]

    y_inicial = dimensiones["alto"] *0.45
    espacio_entre_lineas = dimensiones["alto"] * 0.07

    for i in range(len(titulos)):
        titulo = titulos[i]
        x = posiciones_x[i]
        lista = puntajes.get(titulo, [])
        for j in range(len(lista)):
            nombre, puntaje = lista[j]
            texto = f"{nombre}: {puntaje}"
            superficie_texto = fuente.render(texto, True, color)
            rect = superficie_texto.get_rect(center=(x, y_inicial + j * espacio_entre_lineas))
            pantalla.blit(superficie_texto, rect)


def renderizar_input(usuario:pg.Surface, dimensiones:dict) -> pg.Rect:
    
    """
    Renderiza un Rect con un ancho minimo que crece si lo que ingresa el usuario es mas largo.
    Parametro:
        usuario (pygame Surface): renderiza el nombre que este ingresando el usuario
        dimensiones (dict): diccionario con las distintas dimensiones de la pantalla
    Retorna:
        boton_rect (pygame Rect): Retorna un Rect que se utilizara como input.
    """
    
    ancho_boton = max(usuario.get_width() + 20, 200)
    alto_boton = dimensiones["alto"] // 10
    boton_rect = pg.Rect(dimensiones["ancho"] // 2 - ancho_boton // 2, dimensiones["ancho"] * 0.50, ancho_boton, alto_boton)

    return boton_rect


def cronometrar_juego(timers:dict) -> int:

    """
    Verifica el tiempo que paso desde el arranque de la partida hasta que se pierde o se gana, y lo retorna.
    Parametro:
        timers (dict): diccionario con todos los tiempos con los que se cronometra.
    Retorna:
        tiempo (int) = retorna el tiempo transcurrido hasta que se pierde o se gana.
    """

    tiempo = 0

    if timers["tiempo_arranque"] != 0:
        if timers["tiempo_victoria"] == 0 and timers["tiempo_derrota"] == 0:
            tiempo = (pg.time.get_ticks() - timers["tiempo_arranque"]) // 1000
        else:
            if timers["tiempo_victoria"] != 0:
                tiempo = (timers["tiempo_victoria"] - timers["tiempo_arranque"]) // 1000
            else:
                tiempo = (timers["tiempo_derrota"] - timers["tiempo_arranque"]) // 1000

    return tiempo
