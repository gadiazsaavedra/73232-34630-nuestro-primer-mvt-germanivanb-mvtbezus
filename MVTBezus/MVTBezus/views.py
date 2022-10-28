from django.http import HttpResponse
from django.template import Context, Template, loader


def saludo(
    request,
):  # Definir una funcion -> Crear una vista (view): lo que se ve en la pantalla de la pagina web.

    return HttpResponse("Hola Django-Coder")


def Temp_tp(request, nombre):
    # HtmlTp = open(r"D:\Users\Ivan\Desktop\Curso Visual Studio Code\MVTBezus\MVTBezus\Templeted\Templated1.html")

    # plantilla = Template(HtmlTp.read())

    # HtmlTp.close()  #operacion de seguridad para cerrar el acceso luego de su uso (evitar que otro entre)

    # mi_contexto = Context({"my_name": nombre , "notas" : [4, 6, 7, 8]})
    plantilla = loader.get_template("Templated1.html")

    documento = plantilla.render({"my_name": nombre, "notas": [4, 6, 7, 8]})

    return HttpResponse(documento)
