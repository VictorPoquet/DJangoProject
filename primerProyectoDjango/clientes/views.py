from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory
from clientes.models import Cliente

# def list_client(request):
#    return render(request, "list_client.html")

# para poder quitarle campos DEL POST DEL FORMULAIRO exclude=[]  Y PODER COGER TODOS LOS DATOS DEL FORMULARIO POST
ClienteForm = modelform_factory(Cliente, exclude=[])


def add_new_client(request):
    msg = "No creado"
    if request.method == 'POST':
        try:
            '''nombre = request.POST["nombre"]
            apellidos = request.POST["apellidos"]
            dni = request.POST["dni"]
            email = request.POST["email"]
            cliente = Cliente(nombre=nombre, apellidos=apellidos, dni=dni, email=email)
            print("cliente = ", cliente)'''
            clienteForm = ClienteForm(request.POST)
            clienteForm.save()


        except Exception as e:
            msg = f"Error al almacenar el cliente {e}"
        else:
            msg = "CREADO"
    else:
        clienteForm = ClienteForm()
    mensaje = {"cliente_from": clienteForm, "msg": msg}
    return render(request, "add_new_client.html", mensaje)

def delete_client(request,id):
    client = Cliente.objects.get(pk=id)
    print(f"Cliente a eliminar {id}")
    client.delete()
    print("Cliente borrado")
    return render(request, "delete_client.html")

def delete_client_template(request):
    if request.method == 'POST':
        id = request.POST['id_cli']
        #client = Cliente.objects.get(pk=id) #COMO BUSCAR ALGO EN LA BASE DE DATOS
        client = get_object_or_404(Cliente, pk=id)
        client.delete()

    return render(request, "delete_client.html")