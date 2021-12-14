#!/urs/bin/envy python3
import cgi
import cgitb

def conversor_distancia(distancia: float, de: float, para: float) -> float:
    resultado = 0
    if de == para:
        resultado = distancia
    if (de == "Milímetro" and para == "Centímetro") or (de == "Centímetro" and para == "Decímetro") or (de == "Decímetro" and para == "Metro") or (de == "Metro" and para == "Decâmetro") or (de == "Decâmetro" and para == "Hectômetro") or (de == "Hectômetro" and para == "Quilômetro"):
        resultado = distancia/10.0
    elif (de == "Milímetro" and para == "Decímetro") or (de == "Centímetro" and para == "Metro") or (de == "Decímetro" and para == "Decâmetro") or (de == "Metro" and para == "Hectômetro") or (de == "Decâmetro" and para == "Quilômetro"):
        resultado = distancia/100.0
    elif (de == "Milímetro" and para == "Metro") or (de == "Centímetro" and para == "Decâmetro") or (de == "Decímetro" and para == "Hectômetro") or (de == "Metro" and para == "Quilômetro"):
        resultado = distancia/1000.0
    elif (de == "Milímetro" and para == "Decâmetro") or (de == "Centímetro" and para == "Hectômetro") or (de == "Decímetro" and para == "Quilômetro"):
        resultado = distancia/10000.0
    elif (de == "Milímetro" and para == "Hectômetro") or (de == "Centímetro" and para == "Quilômetro"):
        resultado == distancia/100000.0
    elif de == "Milímetro" and para == "Quilômetro":
        resultado = distancia/1000000.0
    elif (de == "Centímetro" and para == "Milímetro") or (de == "Decímetro" and para == "Centímetro") or (de == "Metro" and para == "Decímetro") or (de == "Decâmetro" and para == "Metro") or (de == "Hectômetro" and para == "Decâmetro") or (de == "Quilômetro" and para == "Hectômetro"):
        resultado = distancia*10.0
    elif (de == "Decímetro" and para == "Milímetro" )or (de == "Metro" and para == "Centímetro") or (de == "Decâmetro" and para == "Decímetro") or (de == "Hectômetro" and para == "Metro") or (de == "Quilômetro" and para == "Decâmetro"):
        resultado = distancia*100.0
    elif (de == "Metro" and para == "Milímetro") or (de == "Decâmetro" and para == "Centímetro") or (de == "Hectômetro" and para == "Decímetro") or (de == "Quilômetro" and para == "Metro"):
        resultado = distancia*1000.0
    elif (de == "Decâmetro" and para == "Milímetro") or (de == "Hectômetro" and para == "Centímetro") or (de == "Quilômetro" and para == "Decímetro"):
        resultado = distancia*10000.0
    elif (de == "Hectômetro" and para == "Milímetro") or (de == "Quilômetro" and para == "Centímetro"):
        resultado == distancia*100000.0
    elif de == "Quilômetro" and para == "Milímetro":
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
    elif de == "Horas" and para == "Minutos":
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

tempo = form.getvalue("tempo")
distancia = form.getvalue("distancia")
de_distancia = form.getvalue("deDistancia")
para_distancia = form.getvalue("paraDistancia")
de_tempo = form.getvalue("deTempo")
para_tempo = form.getvalue("paraTempo")

resultado_distancia = 0
resultado_tempo = 0

print("Content-Type:text/html\r\n\r\n")
print("<html>")
'''print("<head>")
print("</head>")
print("<body>")
print("<div>"
        "<fieldset>"
            "<legend><b>Resultado</b></legend>")
if tempo == None:
    dist = float(distancia)
    resultado_distancia = conversor_distancia(dist, de_distancia, para_distancia)
    print(          "<label>{} {} equivale a {} {}</label>".format(distancia, de_distancia,
                                                                   para_distancia, resultado_distancia))
print(  "</fieldset>"
      "</div>")'''
print("<h1>%s<h1>", de_tempo)
print("</body>")
print("</html>")

#python -m http.server 8080 --cgi