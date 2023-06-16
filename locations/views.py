from django.shortcuts import render, HttpResponse
from locations.models import Department, City, Neighborhood

# Create your views here.

def index (request):
    template_name = 'locations/index.html'
    return render(request, template_name)


def Departamentos(request):
    template_name = 'locations/Departamentos.html'
    departments = Department.objects.all() # es lo mismo que un select * from Department en una base de datos
    list_department = []
    for department in departments:
        # print("estoy en el for")
        name_departments = "{}".format(department.namedepartment)
        list_department.append(name_departments)

        # print(name_departments)
    context = {
        "list_department": list_department,
    }
    return render(request, template_name, context)


def list_city(request, department_id):
    template_name = 'locations/city_list.html'
    cities = City.objects.filter(department_id=department_id).first()
    cities2= City.objects.filter(department_id=department_id)
    lista_ciudades = [ ]
    departamento = "{}".format(cities.department)
    

    for citys in cities2:
                name_citys = "{}".format(citys.nameCity)
                lista_ciudades.append(name_citys)




    context = {
                "lista_ciudades": lista_ciudades,
                "departamento": departamento
    }
        



    return render(request, template_name, context)
    

    





def list_city2(request, department_id):



    
    template_name = 'locations/city_list.html'


    cities = City.objects.filter(department_id=department_id).first() # select * from city where departamento = departamento
    cities2= City.objects.filter(department_id=department_id)
    lista_ciudades=[ ]
    for citys in cities2 :
            name_citys = """ {} """.format(citys.nameCity)
            lista_ciudades.append(name_citys)

    
  
    if cities:
        # print("estoy en el if")
        # print(lista_ciudades)
        # print("despues de la lista")
        
        texto_respuesta= """

            <h1> Departamento de : {} </h1>    
            <ul> Ciudades:
                <li>
                    {}
                </li>
            </ul>
        """.format(cities.department, lista_ciudades )
        
    else:
        texto_respuesta = """no se encuentras registros de  {}""".format(department_id)
    
    return HttpResponse(texto_respuesta)


def ciudades(request, name_department):

    template_name = 'locations/Cuidades.html'
    departamento = Department.objects.filter(namedepartment__iexact=name_department).first()

    if departamento :
        ciudad = City.objects.filter(department = departamento).all()

        context = {
            "display" : True,
            "departamento":departamento,
            "ciudad" : ciudad
        }

    else:
        context = {
            "display" : False,

        }
    return render(request, template_name, context)


def barrios(request, name_department, name_city):

    template_name = 'locations/Barrios.html'
    
    departamento = Department.objects.filter(namedepartment=name_department).first()

    if departamento :

        ciudad = City.objects.filter(nameCity= name_city, department=departamento).first()

        if ciudad :
            barrio = Neighborhood.objects.filter(city=ciudad)

            context = {
                "display" : True,
                "ciudad" : ciudad,
                "barrio" : barrio
            }
        else:

            context = {
                "display" : False,

            }
    else:

        context = {
            "display" : False,

        }



    return render(request, template_name, context)
        

