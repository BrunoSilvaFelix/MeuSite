#!/urs/bin/envy python3
import cgi
import cgitb


# python3 -m http.server 8080 --cgi

def conversor_distancia(distancia: float, de: str, para: str) -> float:
    resultado = 0
    if de == para:
        resultado = distancia
    if (de == "Milímetros" and para == "Centímetros") or (de == "Centímetros" and para == "Decímetros") or (de == "Decímetros" and para == "Metros") or (de == "Metros" and para == "Decâmetros") or (de == "Decâmetros" and para == "Hectômetros") or (de == "Hectômetros" and para == "Quilômetros"):
        resultado = distancia/10.0
    elif (de == "Milímetros" and para == "Decímetros") or (de == "Centímetros" and para == "Metros") or (de == "Decímetros" and para == "Decâmetros") or (de == "Metros" and para == "Hectômetros") or (de == "Decâmetros" and para == "Quilômetros"):
        resultado = distancia/100.0
    elif (de == "Milímetros" and para == "Metros") or (de == "Centímetros" and para == "Decâmetros") or (de == "Decímetros" and para == "Hectômetros") or (de == "Metros" and para == "Quilômetros"):
        resultado = distancia/1000.0
    elif (de == "Milímetros" and para == "Decâmetros") or (de == "Centímetros" and para == "Hectômetros") or (de == "Decímetros" and para == "Quilômetros"):
        resultado = distancia/10000.0
    elif (de == "Milímetros" and para == "Hectômetros") or (de == "Centímetros" and para == "Quilômetros"):
        resultado == distancia/100000.0
    elif de == "Milímetros" and para == "Quilômetros":
        resultado = distancia/1000000.0
    elif (de == "Centímetros" and para == "Milímetros") or (de == "Decímetros" and para == "Centímetros") or (de == "Metros" and para == "Decímetros") or (de == "Decâmetros" and para == "Metros") or (de == "Hectômetros" and para == "Decâmetros") or (de == "Quilômetros" and para == "Hectômetros"):
        resultado = distancia*10.0
    elif (de == "Decímetros" and para == "Milímetros" )or (de == "Metros" and para == "Centímetros") or (de == "Decâmetros" and para == "Decímetros") or (de == "Hectômetros" and para == "Metros") or (de == "Quilômetros" and para == "Decâmetros"):
        resultado = distancia*100.0
    elif (de == "Metros" and para == "Milímetros") or (de == "Decâmetros" and para == "Centímetros") or (de == "Hectômetros" and para == "Decímetros") or (de == "Quilômetros" and para == "Metros"):
        resultado = distancia*1000.0
    elif (de == "Decâmetros" and para == "Milímetros") or (de == "Hectômetros" and para == "Centímetros") or (de == "Quilômetros" and para == "Decímetros"):
        resultado = distancia*10000.0
    elif (de == "Hectômetros" and para == "Milímetros") or (de == "Quilômetros" and para == "Centímetros"):
        resultado == distancia*100000.0
    elif de == "Quilômetros" and para == "Milímetros":
        resultado = distancia*1000000.0
    return resultado

def conversor_tempo(tempo: int, de: str, para: str) -> int:
    resultado = 0
    if de == para:
        resultado = tempo
    elif (de == "Segundos" and para == "Minutos") or (de == "Minutos" and para == "Horas"):
        resultado = tempo/60
    elif de == "Segundos" and para == "Horas":
        resultado = tempo/3600
    elif de == "Segundos" and para == "Anos":
        resultado = tempo/31536000
    elif de == "Minutos" and para == "Anos":
        resultado = tempo/525600
    elif de == "Horas" and para == "Segundos":
        resultado = tempo*3600
    elif (de == "Horas" and para == "Minutos") or (de == "Minutos" and para == "Segundos"):
        resultado = tempo*60
    elif de == "Horas" and para == "Anos":
        resultado = tempo/8760
    elif de == "Anos" and para == "Segundos":
        resultado = tempo*31536000
    elif de == "Anos" and para == "Minutos":
        resultado = tempo*525600
    elif de == "Anos" and para == "Horas":
        resultado = tempo*8760
    return resultado


cgitb.enable()

form = cgi.FieldStorage()

resultado_distancia = 0
distancia = form.getvalue("distancia")
de_distancia = str(form.getvalue("deDistancia"))
para_distancia = str(form.getvalue("paraDistancia"))

resultado_tempo = 0
tempo = form.getvalue("tempo")
de_tempo = form.getvalue("deTempo")
para_tempo = form.getvalue("paraTempo")

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<style>"
        "body{"
            "font-family: Arial, Helvetica, sans-serif;"
            "background-image: linear-gradient(to right, rgb(40, 220, 80), rgb(40, 90, 50))"
        "}"
        "div{"
            "color: white;"
            "position: absolute;"
            "top: 50%;"
            "left: 50%;"
            "transform: translate(-50%, -50%);"
            "background-color: rgba(0, 0, 0, 0.8);"
            "padding: 15px;"
            "border-radius: 15px;"
            "width: 40%;"
        "}"
        "fieldset{"
            "border: 3px solid forestgreen;"
        "}"
        "legend{"
            "border: 1px solid forestgreen;"
            "padding: 10px;"
            "text-align: center;"
            "background-color: forestgreen;"
            "border-radius: 8px;"
        "}"
      "</style>")
print("</head>")
print("<body>")
print("<div>"
        "<fieldset>"
            "<legend><b>Resultado</b></legend>")
if tempo == None:
    distancia = float(distancia)
    resultado_distancia = conversor_distancia(distancia, de_distancia, para_distancia)
    print(          "<h1>{} {} equivalem a {} {}</h1>".format(distancia, de_distancia,
                                                                   resultado_distancia, para_distancia))
if distancia == None:
    tempo = float(tempo)
    resultado_tempo = conversor_tempo(tempo, de_tempo, para_tempo)
    print(          "<h1>{} {} equivalem a {} {}</h1>".format(tempo, de_tempo, resultado_tempo,
                                                                   para_tempo))
print(  "</fieldset>"
      "</div>")

print("</body>")
print("</html>")