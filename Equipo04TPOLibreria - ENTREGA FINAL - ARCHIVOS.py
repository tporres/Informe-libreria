"""
-----------------------------------------------------------------------------------------------
Título: TPO Entrega final
Fecha:  07/07/2025
Autor:  Grupo 04

Descripción: Se trata de un sistema informático para una biblioteca de organización educativa que da préstamos de libros a alumnos.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
import json
import re

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

#FUNCIONES DE VALIDACION

def validarEmail(_email):
    '''
    Valida si el formato del email ingresado es correcto mediante una expresión regular.
    
    PARAMETROS:
    _email: cadena de texto que representa el email a validar.
    
    SALIDA:
    Devuelve True si el email tiene un formato válido, False en caso contrario.
    '''
    pat = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pat, _email))




def pedirMail():
    '''
    Solicita al usuario que ingrese un email y valida su formato.
    
    PARAMETROS:
    SALIDA:
    Devuelve el email ingresado una vez que cumple con el formato válido.
    '''
    email = input("Ingrese un email:").strip()
    while not validarEmail(email):
        print("Email inválido. Intente nuevamente.")
        email = input("Ingrese un email válido: ").strip()
    return email

def pedirMailOpcional(email_actual):
    """
    Pide un nuevo email. Si se deja vacío, conserva el actual.
    
    PARAMETROS:
    email_actual: string con el email que ya tiene el alumno
    
    SALIDA:
    - Nuevo email validado si se ingresa uno.
    - El mismo email si se deja vacío.
    """
    entrada = input(f"Ingrese nuevo email (actual: {email_actual}, Enter para mantenerlo): ").strip()
    if entrada == "":
        return email_actual

    while not validarEmail(entrada):
        print("Email inválido. Intente nuevamente o presione Enter para dejar el actual.")
        entrada = input("Ingrese un email válido: ").strip()
        if entrada == "":
            return email_actual

    return entrada

def pedirTelefono(nro="Telefono"):
    '''
    Solicita al usuario que ingrese un número de teléfono válido, con opción a dejarlo vacío.
    
    PARAMETROS:
    nro: etiqueta opcional que indica qué tipo de número se solicita (por defecto "Telefono").
    
    SALIDA:
    Devuelve el número de teléfono ingresado si es válido, o una cadena vacía si el usuario lo omite.
    '''
    while True:
        telefono = input(f"Ingrese {nro} (Enter para dejar vacío): ").strip()
        
        if telefono == "":
            return ""  # Permite dejar vacío
        
        if validarTelefono(telefono):
            return telefono
        else:
            print("Número inválido. Debe contener solo dígitos y tener entre 10 y 12 caracteres.")
        

def validarTelefono(_telefono):
    '''
    Valida que el número de teléfono contenga solo dígitos y tenga entre 10 y 12 caracteres.
    
    PARAMETROS:
    _telefono: cadena de texto que representa el número a validar.
    
    SALIDA:
    Devuelve True si el número es válido (solo dígitos, largo adecuado y mayor a 0), False en caso contrario.
    '''
    _telefono = _telefono.strip()
    if _telefono.isdigit() and 10 <= len(_telefono) <= 12:
        return int(_telefono) > 0
    else:
        return False
    
def validarNombre(_nombre):
    '''
    Valida que el nombre ingresado contenga solo letras (permitiendo espacios).
    
    PARAMETROS:
    _nombre: cadena de texto que representa el nombre a validar.
    
    SALIDA:
    Devuelve True si el nombre contiene únicamente letras y espacios, False en caso contrario.
    '''
    nombreSinEspacios= _nombre.replace(" ", "")
    return nombreSinEspacios.isalpha()

def pedirNombre():
    '''
    Solicita al usuario que ingrese un nombre y valida que contenga solo letras y espacios.
    
    PARAMETROS:
    SALIDA:
    Devuelve el nombre ingresado si es válido. Muestra un mensaje de error si el formato es incorrecto.
    '''
    while True:
        try:
            nombre = input("Nombre: ").strip()
            if not validarNombre(nombre):
                raise ValueError
            return nombre
        except ValueError:
            print("Error: El nombre solo debe contener letras y espacios")
            
def pedirNombreOpcional(nombreActual):
    '''
    Solicita un nuevo nombre o permite mantener el actual si se deja vacío.
    
    PARÁMETROS:
    nombreActual: El nombre que ya tiene el alumno.

    SALIDA:
    Devuelve el nuevo nombre si es válido o el actual si se deja vacío.
    '''
    while True:
        try:
            nombre = input(f"Ingrese nuevo nombre (actual: {nombreActual}, Enter para mantenerlo): ").strip()
            if nombre == "":
                return nombreActual
            if not validarNombre(nombre):
                raise ValueError
            return nombre
        except ValueError:
            print("Error: El nombre solo debe contener letras y espacios.")
            

def pedirApellido():
    '''
    Solicita al usuario que ingrese un apellido y valida que contenga solo letras y espacios.
    
    PARAMETROS:
    SALIDA:
    Devuelve el apellido ingresado si es válido. Muestra un mensaje de error si el formato es incorrecto.
    '''
    while True:
        try:
            apellido = input("Apellido: ").strip()
            if not validarNombre(apellido):
                raise ValueError
            return apellido
        except ValueError:
            print("Error: El apellido solo debe contener letras y espacios")
            
def pedirApellidoOpcional(apellidoActual):
    '''
    Solicita un nuevo apellido o permite mantener el actual si se deja vacío.
    
    PARÁMETROS:
    apellidoActual: El apellido que ya tiene el alumno.

    SALIDA:
    Devuelve el nuevo apellido si es válido o el actual si se deja vacío.
    '''
    while True:
        try:
            apellido = input(f"Ingrese nuevo apellido (actual: {apellidoActual}, Enter para mantenerlo): ").strip()
            if apellido == "":
                return apellidoActual
            if not validarNombre(apellido):
                raise ValueError
            return apellido
        except ValueError:
            print("Error: El apellido solo debe contener letras y espacios.")

def enteroPositivo(mensaje):
    '''
    Solicita al usuario que ingrese un número entero positivo o cero, y valida la entrada.
    
    PARAMETROS:
    mensaje: texto que se muestra al solicitar el valor al usuario.
    
    SALIDA:
    Devuelve el valor ingresado como entero si es válido (mayor o igual a 0). Muestra mensajes de error en caso de entrada inválida.
    '''
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            print("Debe ser un número igual o mayor a 0.")
        except ValueError:
            print("Entrada inválida. Ingrese un número igual o mayor a 0.")
            
def enteroPositivoOpcional(mensaje):
    """
    Solicita un número entero mayor o igual a 0.
    Permite dejar vacío (devuelve None si se presiona Enter).
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            return None
        if entrada.isdigit():
            return int(entrada)
        print("Error: debe ingresar un número entero positivo o dejar vacío.")
            
def validarEstado(actual):
    """
    Solicita el estado activo/inactivo del libro.
    Permite ingresar 'si', 'no', o Enter para no modificar.
    
    Retorna:
        - True si se ingresa 'si'
        - False si se ingresa 'no'
        - None si se deja vacío (no se modifica)
    """
    while True:
        try:
            entrada = input(f"¿Activo? (actual: {actual}, si/no, Enter para mantener): ").strip().lower()
            if entrada == "":
                return None
            elif entrada == "si":
                return True
            elif entrada == "no":
                return False
            else:
                raise ValueError
        except ValueError:
            print("Error: Debe ingresar 'si', 'no' o presionar Enter para no modificarlo.")


# FUNCIONES PARA GESTIONAR ALUMNOS

def ingresoAlumno():
    
    """
    Funcion para ingresar alumnos al sistema.
    
    PARÁMETROS:
    SALIDA:
            Mensaje informativo que el Alumno fue ingresado correctamente. Ademas se carga el Alumno ingresado en el diccionario "Alumnos".
    """
    try:
                
        #Leo archivo json de Alumnos y lo paso a un diccionario
        Alumnos=open("Alumnos.json",mode="r",encoding="utf-8")
        alumnos=json.load(Alumnos)
        Alumnos.close()
        print("---------------------------")
        print("Ingreso de nuevo Alumno")
        print("---------------------------")

        nombre = pedirNombre()
        apellido = pedirApellido()
        direccion = input("Dirección: ").strip()
        email = pedirMail()
        carrera = input("Carrera de estudio: ").strip()
        telefono1 = pedirTelefono("Telefono 1:")
        telefono2 = pedirTelefono("Telefono 2:")
        telefono3 = pedirTelefono("Telefono 3:")

        if not alumnos:
            nuevoId = "1001"
        else:
            idExistentes = [int(k) for k in alumnos.keys()]
            nuevoNum = max(idExistentes) + 1
            nuevoId = str(nuevoNum)


        alumno = {
            "IdAlumno": nuevoId,
            "activo": True,
            "nombre": nombre,
            "apellido": apellido,
            "direccion": direccion,
            "email": email,
            "carrera": carrera,
            "telefonos":
            {
                "telefono1": telefono1,
                "telefono2": telefono2,
                "telefono3": telefono3
            }

        }
        

        alumnos[nuevoId] = alumno  # Se agrega al archivo original
        
        #Escribo el archivo json de alumnos con el diccionario de alumnos
        Alumnos=open("Alumnos.json",mode="w",encoding="utf-8")
        alumnos=json.dump(alumnos,Alumnos,ensure_ascii=False,indent=4)
        Alumnos.close()

        print(f"\n El alumno '{nombre}' (ID: {nuevoId}) fue agregado con éxito.\n")
        
    except(FileNotFoundError,OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)
        
        return

def modificarAlumno():
    """
    Funcion para modificar alumnos al sistema.
    
    PARÁMETROS:
            No recibe, busca el archivo Alumnos y lo convierte en diccionario
    SALIDA:
            Mensaje informativo que el Alumno fue modificado correctamente junto con las modificaciones realizadas.
            Ademas se actualiza el alumno ingresado en el diccionario "Alumnos".
    """
    try:
        #Leo archivo json de Alumnos y lo paso a un diccionario
        Alumnos=open("Alumnos.json",mode="r",encoding="utf-8")
        alumnos=json.load(Alumnos)
        Alumnos.close()
        print("\n=== Modificar Alumno ===")
        print("Alumnos disponibles:")
        for idAl, datos in alumnos.items():
            print(f"{idAl}: {datos['nombre']} {datos['apellido']}")
        idAlumno = input("Ingrese el ID del alumno a modificar: ").strip()
        if idAlumno not in alumnos:
            print("ID de alumno no válido.")
            return

        alumno = alumnos[idAlumno]
        print("\nDeje en blanco para no modificar ese campo.")

        nombre=pedirNombreOpcional(alumno['nombre'])
        apellido = pedirApellidoOpcional(alumno['apellido'])
        direccion = input(f"Dirección actual ({alumno['direccion']}): ").strip()
        print((f"Email actual ({alumno['email']}): "))
        email = pedirMailOpcional(alumno['email'])
        carrera = input(f"Carrera actual ({alumno['carrera']}): ").strip()

        print(f"Teléfono 1 actual ({alumno['telefonos']['telefono1']}): ")
        telefono1 = pedirTelefono("Telefono 1:")        
        print(f"Teléfono 2 actual ({alumno['telefonos']['telefono2']}): ")
        telefono2 = pedirTelefono("Telefono 2:")
        print(f"Teléfono 3 actual ({alumno['telefonos']['telefono3']}): ")
        telefono3 = pedirTelefono("Telefono 3:")

        # Solo actualiza si el campo no está vacío
        if nombre:
            alumno['nombre'] = nombre
        if apellido:
            alumno['apellido'] = apellido
        if direccion:
            alumno['direccion'] = direccion
        if email:
            alumno['email'] = email
        if carrera:
            alumno['carrera'] = carrera
        if telefono1:
            alumno['telefonos']['telefono1'] = telefono1
        if telefono2:
            alumno['telefonos']['telefono2'] = telefono2
        if telefono3:
            alumno['telefonos']['telefono3'] = telefono3
        
        #Escribo el archivo json de alumnos con el diccionario de alumnos
        Alumnos=open("Alumnos.json",mode="w",encoding="utf-8")
        alumnos=json.dump(alumnos,Alumnos,ensure_ascii=False,indent=4)
        Alumnos.close()
        
        print("\nAlumno modificado exitosamente.")
        return
    except(FileNotFoundError,OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)


def eliminarAlumno():
    """
    Funcion para eliminar alumnos del sistema, lee un archivo y lo modifica.
    SALIDA:
            Mensaje informativo que el Alumno fue eliminado correctamente. Ademas se elimina mediante baja logica el Alumno eliminado en el archivo "Alumnos".
    """
    try:
        #Leo archivo json de Alumnos y lo paso a un diccionario
        Alumnos=open("Alumnos.json",mode="r",encoding="utf-8")
        alumnos=json.load(Alumnos)
        Alumnos.close()
        
        while True:
            legajo = input("Ingrese el ID del alumno a eliminar (entre 1000 y 9999): ")
            print()

            if not legajo.isdigit():
                print("Error: Debe ingresar un número entero.")
                continue

            legajoInt = int(legajo)
            if legajoInt < 1000 or legajoInt > 9999:
                print("El ID ingresado está fuera del rango válido (1000 a 9999).")
                continue

            legajo = str(legajoInt)
            break  # Si todo está OK, salimos del bucle

        if legajo in alumnos:
            if alumnos[legajo]["activo"]:
                alumnos[legajo]["activo"] = False
                print(f"El alumno con ID {legajo} fue dado de baja.")
            else:
                print(f"El alumno con ID {legajo} ya estaba dado de baja.")
        else:
            print(f"No se encontró ningún alumno con ID {legajo}.")
            
        #Escribo el archivo json de alumnos con el diccionario de alumnos
        Alumnos=open("Alumnos.json",mode="w",encoding="utf-8")
        alumnos=json.dump(alumnos,Alumnos,ensure_ascii=False,indent=4)
        Alumnos.close()
        
        return alumnos
    except(FileNotFoundError,OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)


def listarAlumnos():
    """
    Funcion para ingresar alumnos al sistema.
    SALIDA:
            Listado de alumnos con campo "Activo" == True.
    """
    try:
        #Leo archivo json de Alumnos y lo paso a un diccionario
        Alumnos=open("Alumnos.json",mode="r",encoding="utf-8")
        alumnos=json.load(Alumnos)
        Alumnos.close()        
        encontrados = False
        for legajo, datos in alumnos.items():
            if datos["activo"]:
                encontrados = True
                print("-" * 30)
                print(f"Legajo: {legajo}")
                print(f"Nombre completo: {datos['nombre']} {datos['apellido']}")
                print(f"Email: {datos['email']}")
                print(f"Carrera: {datos['carrera']}")
                print(f"Teléfono 1: {datos['telefonos']['telefono1']}")
                print(f"Teléfono 2: {datos['telefonos']['telefono2']}")
                print(f"Teléfono 3: {datos['telefonos']['telefono3']}")
                print("-" * 30)
        if not encontrados:
            print("No hay alumnos activos para listar.")
        return
    except(FileNotFoundError,OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)
        
#FUNCIONES PARA GESTIONAR LIBROS
def ingresoLibros():

    """
    Funcion para ingresar libros al sistema, guarda el libro en archivo "Libros"
    
    PARÁMETROS:
    SALIDA:
            Mensaje informativo que el libro fue ingresado correctamente. Ademas se carga el libro ingresado en el archivo "Libros".
    """
    try:
        #Leo archivo json de Libros y lo paso a un diccionario
        Libros=open("Libros.json",mode="r",encoding="utf-8")
        libros=json.load(Libros)
        Libros.close()    
        print("---------------------------")
        print("Ingreso de nuevo libro")
        print("---------------------------")

        nombre = input("Nombre del libro: ").strip()
        editorial = input("Editorial: ").strip()
        categoria = input("Categoría: ").strip()
        stock = enteroPositivo("Ingrese stock:") #Llamo a una funcion que valide que se ingrese un entero >=0
        costo=enteroPositivo("Ingrese costo:")
            

        autor1 = input("Autor principal: ").strip()
        autor2 = input("Segundo autor: ").strip()
        autor3 = input("Tercer autor: ").strip()

        # Generación del nuevo ID (extrae el número más alto y suma 1)
        if not libros:
            nuevoId = "L001"
        else:
            ultimoId = [int(clave[1:]) for clave in libros.keys()]
            nuevoNum = max(ultimoId) + 1
            nuevoId = f"L{nuevoNum:03d}"

        if stock > 0:
            activo = True
        else:
            activo = False

        libro = {
            "activo": activo,
            "stock": stock,
            "nombre": nombre,
            "editorial": editorial,
            "categoria": categoria,
            "autores": {
                "autor1": autor1,
                "autor2": autor2,
                "autor3": autor3
            },
            "costo": costo
        }

        libros[nuevoId] = libro  # Se agrega al diccionario original
        
         #Escribo el archivo json de Libros con el diccionario de libros
        Libros=open("Libros.json",mode="w",encoding="utf-8")
        libros=json.dump(libros,Libros,ensure_ascii=False,indent=4)
        Libros.close()

        print(f"\n El libro '{nombre}' (ID: {nuevoId}) fue agregado con éxito.\n")
        return
    except(FileNotFoundError,OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

def modificarLibro():
    """
    Funcion para modificar libros al sistema.
    
    PARÁMETROS:
    SALIDA:
            Mensaje informativo que el libro fue modificado correctamente. Ademas se carga el libro modificado en el archivo "Libros".
    """
    try:
        #Leo archivo json de Libros y lo paso a un diccionario
        Libros=open("Libros.json",mode="r",encoding="utf-8")
        libros=json.load(Libros)
        Libros.close() 
        print("\n=== Modificar Libro ===")
        print("Libros disponibles:")
        for idLib, datos in libros.items():
            print(f"{idLib}: {datos['nombre']}")
        idLibro = input("Ingrese el ID del libro a modificar: ").strip()
        if idLibro not in libros:
            print("ID de libro no válido.")
            return

        libro = libros[idLibro]
        print("\nDeje en blanco para no modificar ese campo.")

        nombre = input(f"Nombre actual ({libro['nombre']}): ").strip()
        editorial = input(f"Editorial actual ({libro['editorial']}): ").strip()
        categoria = input(f"Categoría actual ({libro['categoria']}): ").strip()
        stock = enteroPositivoOpcional((f"Stock actual ({libro['stock']}): "))
        costo=enteroPositivoOpcional(f"Costo actual ({libro['costo']}): ")
        activo = validarEstado(libro['activo'])

        autor1 = input(f"Autor 1 actual ({libro['autores']['autor1']}): ").strip()
        autor2 = input(f"Autor 2 actual ({libro['autores']['autor2']}): ").strip()
        autor3 = input(f"Autor 3 actual ({libro['autores']['autor3']}): ").strip()

        # Solo actualiza si el campo no está vacío
        if nombre:
            libro['nombre'] = nombre
        if editorial:
            libro['editorial'] = editorial
        if categoria:
            libro['categoria'] = categoria
        if stock:
            libro['stock'] = int(stock)
        if costo:
            libro['costo'] = int(costo)
        if activo is not None :
            libro['activo'] = activo

        if autor1:
            libro['autores']['autor1'] = autor1
        if autor2:
            libro['autores']['autor2'] = autor2
        if autor3:
            libro['autores']['autor3'] = autor3
            
        #Escribo el archivo json de Libros con el diccionario de libros
        Libros=open("Libros.json",mode="w",encoding="utf-8")
        libros=json.dump(libros,Libros,ensure_ascii=False,indent=4)
        Libros.close()
        print("\nLibro modificado exitosamente.")
        return
    except(FileNotFoundError,OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)



def eliminarLibro():
    
    """
    Función para Eliminar libros del sistema.

    SALIDA:
        Mensaje informativo de que el libro fue eliminado correctamente.
        Además, se actualiza el valor del campo "activo" a False en el archivo "Libros"
        en el registro con el idLibro ingresado por teclado.
    """
    try:
        # Leer archivo json de Libros y cargar en un diccionario
        Libros = open("Libros.json", mode="r", encoding="utf-8")
        libros = json.load(Libros)
        Libros.close()

        idLibro = input("Ingrese el ID del libro que desea desactivar: ").strip()

        if idLibro in libros:
            if libros[idLibro]["activo"]:
                libros[idLibro]["activo"] = False

                # Guardar el diccionario actualizado en el archivo JSON
                Libros = open("Libros.json", mode="w", encoding="utf-8")
                json.dump(libros, Libros, ensure_ascii=False, indent=4)
                Libros.close()

                # Mostrar mensaje después de guardar, usando el diccionario original
                print(f"Libro '{libros[idLibro]['nombre']}' con ID {idLibro} fue desactivado correctamente.")
                return
            else:
                print(f"El libro con ID {idLibro} ya estaba inactivo.")
                return
        else:
            print(f"No se encontró ningún libro con ID {idLibro}.")
            return

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)



def librosActivos():
    """
    Funcion para mostrar libros activos
    
    PARÁMETROS:
    SALIDA:
            Listado de libros que cumplen con la condicion campo "Activo" sea True.
    """
    try:
        # Leer archivo json de Libros y cargar en un diccionario
        Libros = open("Libros.json", mode="r", encoding="utf-8")
        libros = json.load(Libros)
        Libros.close()
    
        encontrados = False
        for idLibro, datos in libros.items():
            if datos["activo"]:
                encontrados = True
                print(f"ID del Libro: {idLibro}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Editorial: {datos['editorial']}")
                print(f"Categoría: {datos['categoria']}")
                print(f"Stock: {datos['stock']}")
                print(f"Autor 1: {datos['autores']['autor1']}")
                print(f"Autor 2: {datos['autores']['autor2']}")
                print(f"Autor 3: {datos['autores']['autor3']}")
                print(f"Costo de garantia por dia: {datos['costo']}")
                print("-" * 30)

        if not encontrados:
            print("No hay libros activos para listar.")
        return
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)


def buscarLibrosPorAutor(): #Funcion para buscar libros en base a su autor
    
    '''
    Solicita un autor a buscar y luego imprime por pantalla un listado de los libros que coinciden con el autor solicitado
    
    PARAMETROS:
    SALIDA:
    imprime un listado con los libros cuya categoria coincide con el autor buscado dentro del archivo Libros, en caso de no haber encontrado ninguno informa que no hay libros con ese autor
    '''
    try:
        # Leer archivo json de Libros y cargar en un diccionario
        Libros = open("Libros.json", mode="r", encoding="utf-8")
        libros = json.load(Libros)
        Libros.close()
        
        autorBuscado = input("Ingrese el nombre del autor a buscar: ").strip().lower()
        encontrados = False

        for idLibro, datos in libros.items():
            for key in ['autor1', 'autor2', 'autor3']:
                autor = datos["autores"].get(key, "").strip().lower()
                if autor and autorBuscado in autor:
                    encontrados = True
                    print("-" * 30)
                    print(f"ID del Libro: {idLibro}")
                    print(f"Nombre: {datos['nombre']}")
                    print(f"Editorial: {datos['editorial']}")
                    print(f"Categoría: {datos['categoria']}")
                    print(f"Stock: {datos['stock']}")
                    print(f"Autor 1: {datos['autores']['autor1']}")
                    print(f"Autor 2: {datos['autores']['autor2']}")
                    print(f"Autor 3: {datos['autores']['autor3']}")
                    print("-" * 30)
                    break  # Evita duplicar si el autor aparece más de una vez en el mismo libro

        if not encontrados:
            print(f"No se encontraron libros para el autor '{autorBuscado}'.")
        return
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)



def buscarLibrosPorCategoria():      #Funcion para buscar libros en base a su categoria
    '''
    Solicita una categoria a buscar y luego imprime por pantalla un listado de los libros que coinciden con la categoria solicitada
    
    PARÁMETROS:
            No recibe, busca el archivo Libros y lo convierte en diccionario
    SALIDA:
    imprime un listado con los libros cuya categoria coincide con la categoria buscada, en caso de no haber encontrado ninguno informa que no hay libros con esa categoria
    '''
    try:
        # Leer archivo json de Libros y cargar en un diccionario
        Libros = open("Libros.json", mode="r", encoding="utf-8")
        libros = json.load(Libros)
        Libros.close()
        
        categoria = input("Ingrese la categoría a buscar: ").strip().lower()
        encontrados = False

        for idLibro, datos in libros.items():
            if datos["activo"] and categoria in datos["categoria"].lower():
                encontrados = True
                print("-" * 30)
                print(f"ID del Libro: {idLibro}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Editorial: {datos['editorial']}")
                print(f"Categoría: {datos['categoria']}")
                print(f"Stock: {datos['stock']}")
                print(f"Autor 1: {datos['autores']['autor1']}")
                print(f"Autor 2: {datos['autores']['autor2']}")
                print(f"Autor 3: {datos['autores']['autor3']}")
                print("-" * 30)

        if not encontrados:
            print(f"\nNo se encontraron libros en la categoría '{categoria}'.")
        return
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

#FUNCIONES PARA GESTIONAR PRESTAMOS
       

def sumarDias(fecha, dias): #Funcion auxiliar para calcular los dias para devolver un prestamo
    return fecha + timedelta(days=dias)



def registrarPrestamo(): #Funcion para registrar un nuevo prestamo
    '''
    Permite registrar un nuevo prestamo, solicitando el idAlumno, idLibro y tipo de prestamo para calcular la fecha de devolucion y el costo del prestamo en base a
    la cantidad de dias del prestamo y el costo de la garantia del libro
    
    PARAMETROS:
    SALIDA:
    Carga un registro de prestamo nuevo en el archivo de Prestamos, en caso de ingresar un ID erroneo o tipo de prestamo erroneo devuelve un mensaje informando el error
    '''
    
    try:
        #Leo archivo json de Alumnos y lo paso a un diccionario
        Alumnos=open("Alumnos.json",mode="r",encoding="utf-8")
        alumnos=json.load(Alumnos)
        Alumnos.close()
        # Leer archivo json de Libros y cargar en un diccionario
        Libros = open("Libros.json", mode="r", encoding="utf-8")
        libros = json.load(Libros)
        Libros.close()
        #Leo archivo json de Prestamos y lo paso a un diccionario
        Prestamos=open("Prestamos.json",mode="r",encoding="utf-8")
        prestamos=json.load(Prestamos)
        Prestamos.close()
        
        
        
        print("\n--- Registro de nuevo préstamo ---")

        idAlumno = input("ID del alumno (ej: 1001): ").strip()
        if idAlumno not in alumnos or not alumnos[idAlumno]["activo"]:
            print("Alumno no válido o inactivo.")
            return

        idLibro = input("ID del libro (ej: L001): ").strip()
        if idLibro not in libros or not libros[idLibro]["activo"] or libros[idLibro]["stock"] <= 0:
            print("Libro no válido, inactivo o sin stock.")
            return

        tipoPrestamo = input("Tipo de préstamo (1 para semanal, 2 para 15 días y 3 para 30 días): ").strip()
        if tipoPrestamo not in ["1", "2", "3"]:
            print("Tipo de préstamo inválido.")
            return
        tipoPrestamo = int(tipoPrestamo)

        # Calcular costoPrestamo basado en costoGarantia * tipoPrestamo
        costo = libros[idLibro].get("costo", 0)
        

        fechaPrestamo = datetime.now()

        if tipoPrestamo == 1:
            diasADevolver = 7
        elif tipoPrestamo == 2:
            diasADevolver = 15
        else:
            diasADevolver = 30
            
        costoPrestamo = costo * diasADevolver

        fechaDevolucion = sumarDias(fechaPrestamo, diasADevolver)

        idPrestamo = fechaPrestamo.strftime("%Y.%m.%d %H.%M.%S")
        nuevoPrestamo = {
            "IdAlumno": idAlumno,
            "IdLibro": idLibro,
            "tipoPrestamo": tipoPrestamo,
            "costoPrestamo": costoPrestamo,
            "fechaDevolucion": fechaDevolucion.strftime("%Y.%m.%d %H.%M.%S"),
            "Devuelto": False
        }

        prestamos[idPrestamo] = nuevoPrestamo
        libros[idLibro]["stock"] -= 1

        print(f"✅ Préstamo registrado correctamente con ID: {idPrestamo}")
        print(nuevoPrestamo)
        # Guardar el diccionario actualizado en el archivo JSON
        Prestamos = open("Prestamos.json", mode="w", encoding="utf-8")
        json.dump(prestamos, Prestamos, ensure_ascii=False, indent=4)
        Prestamos.close()
        return
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)





def devolverPrestamo():
    '''
    Solicita el id del prestamo a devolver y cambia su status de Devuelto=False a Devuelto=True
    
    PARAMETROS:
    SALIDA:
    Cambia el valor del atributo Devuelto a True, para identificar que un prestamo fue devuelto, en caso de no encontrar el prestamo informa que no fue encontrado ese ID
    '''
    try:
        #Leo archivo json de Prestamos y lo paso a un diccionario
        Prestamos=open("Prestamos.json",mode="r",encoding="utf-8")
        prestamos=json.load(Prestamos)
        Prestamos.close()
        print("----- REGISTRAR DEVOLUCIÓN -----")
        idPrestamo = input("Ingrese el ID del préstamo (formato AAAA.MM.DD hh.mm.ss): ").strip()

        if idPrestamo in prestamos:
            if prestamos[idPrestamo].get("Devuelto", False):
                print("Este préstamo ya fue registrado como devuelto.")
            else:
                prestamos[idPrestamo]["Devuelto"] = True
                print("La devolución fue registrada correctamente.")
                # Guardar el diccionario actualizado en el archivo JSON
                Prestamos = open("Prestamos.json", mode="w", encoding="utf-8")
                json.dump(prestamos, Prestamos, ensure_ascii=False, indent=4)
                Prestamos.close()
        else:
            print("No se encontró un préstamo con ese ID.")
        return
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)


#-------------------------------

#FUNCIONES PARA INFORMES 

#-------------------------------


def listarPrestamosMesActual(): #11 FUNCION PARA MOSTRAR LOS PRESTAMOS DEL MES ACTUAL
    '''
    Genera un resumen para mostrar la informacion de todos los prestamos del mes actual
    
    PARAMETROS:
    SALIDA:
    Imprime un listado con la informacion de todos los prestamos del mes actual
    '''
    try:
        #Leo archivo json de Prestamos y lo paso a un diccionario
        Prestamos=open("Prestamos.json",mode="r",encoding="utf-8")
        prestamos=json.load(Prestamos)
        Prestamos.close()
        
    
    
        tipoDict = {1: "Semanal", 2: "15 días", 3: "Mensual"}
        hoy = datetime.now()

        print(f"{'Prestamo':<20} {'Alumno':<8} {'Libro':<6} {'TipoPrestamo':<12} {'FechaDevolucion':<20} {'Devuelto':<8} {'PrecioGarantía':>15}")
        print("-" * 100)

        for fechaStr, datos in prestamos.items():
            fecha = datetime.strptime(fechaStr, "%Y.%m.%d %H.%M.%S")
            if fecha.year == hoy.year and fecha.month == hoy.month:
                tipoTexto = tipoDict.get(datos["tipoPrestamo"], "Desconocido")
                precio = f"{datos['costoPrestamo']:,.2f}"
                print(f"{fechaStr:<20} {datos['IdAlumno']:<8} {datos['IdLibro']:<6} {tipoTexto:<12} {datos['fechaDevolucion']:<20} {str(datos['Devuelto']):<8} {precio:>15}")
        return
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)



def resumenAnualPrestamosCantidadTabla(año):  #FUNCION PARA IMPRIMIR UN RESUMEN ANUAL POR LIBROS SEGUN CANTIDAD EN FORMATO DE MATRIZ
    '''
    Genera un resumen anual de préstamos por libro en base a la cantidad de veces que fue prestado, en formato de matriz de tabla mensual, permitiendo elegir el año deseado 
    
    PARAMETROS:
    año:Valor numerico para saber en que año realizar la busqueda, en un rango desde el 2000 hasta el 2026
    SALIDA:
    Imprime un resumen en base a la cantidad de veces que un libro fue prestado por libro de los prestamos del año seleccionado en un formato de matriz mes a mes
    '''
    try:
        # Leer archivo json de Libros y cargar en un diccionario
        Libros = open("Libros.json", mode="r", encoding="utf-8")
        libros = json.load(Libros)
        Libros.close()
        #Leo archivo json de Prestamos y lo paso a un diccionario
        Prestamos=open("Prestamos.json",mode="r",encoding="utf-8")
        prestamos=json.load(Prestamos)
        Prestamos.close()
        meses = [
            "ENE", "FEB", "MAR", "ABR", "MAY", "JUN",
            "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"
        ]
        # Inicializar estructura: {idLibro: [0, 0, ..., 0] (12 meses)}
        resumen = {}
        for idLibro, info in libros.items():
            resumen[idLibro] = [0] * 12

        # Procesar préstamos
        for fechaPrestamo, datos in prestamos.items():
            añoPrestamo, mesPrestamo = fechaPrestamo.split('.')[:2]
            if añoPrestamo == año:
                idLibro = datos["IdLibro"]
                mesIdx = int(mesPrestamo) - 1  # 0-indexed
                if idLibro in resumen:
                    resumen[idLibro][mesIdx] += 1

        # Imprimir encabezado
        print(f"\n{'Producto':<25}", end="")
        for m in meses:
            print(f"{m+'.'+año[-2:]:>9}", end="")
        print()

        # Imprimir filas por libro, con salto de línea entre filas
        for idLibro, valores in resumen.items():
            nombre = libros[idLibro]["nombre"][:23]
            print(f"{nombre:<25}", end="")
            for v in valores:
                print(f"{v:>9}", end="")
            print("\n")  # Salto de línea extra entre filas

        # (Opcional) Totales por mes
        print(f"{'TOTAL':<25}", end="")
        for i in range(12):
            totalMes = sum(resumen[libro][i] for libro in resumen)
            print(f"{totalMes:>9}", end="")
        print("\n")
        return
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)



def resumenAnualPrestamosPesosTabla(año):   #FUNCION PARA IMPRIMIR UN RESUMEN DE LOS PRESTAMOS DEL AÑO SELECCIONADO EN FORMATO MATRIZ
    '''
    Genera un resumen anual de préstamos por libro en pesos, en formato de matriz de tabla mensual, permitiendo elegir el año deseado 
    
    PARAMETROS:
    año:Valor numerico para saber en que año realizar la busqueda, en un rango desde el 2000 hasta el 2026
    SALIDA:
    Imprime un resumen en pesos por libro de los prestamos del año seleccionado en un formato de matriz mes a mes
    '''
    try:
        # Leer archivo json de Libros y cargar en un diccionario
        Libros = open("Libros.json", mode="r", encoding="utf-8")
        libros = json.load(Libros)
        Libros.close()
        #Leo archivo json de Prestamos y lo paso a un diccionario
        Prestamos=open("Prestamos.json",mode="r",encoding="utf-8")
        prestamos=json.load(Prestamos)
        Prestamos.close()
        
        meses = [
            "ENE", "FEB", "MAR", "ABR", "MAY", "JUN",
            "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"
        ]
        # Inicializar estructura: {idLibro: [0, 0, ..., 0] (12 meses)}
        resumen = {}
        for idLibro, info in libros.items():
            resumen[idLibro] = [0] * 12

        # Procesar préstamos
        for fechaPrestamo, datos in prestamos.items():
            añoPrestamo, mesPrestamo = fechaPrestamo.split('.')[:2]
            if añoPrestamo == año:
                idLibro = datos["IdLibro"]
                costo = datos["costoPrestamo"]
                mesIdx = int(mesPrestamo) - 1  # 0-indexed
                if idLibro in resumen:
                    resumen[idLibro][mesIdx] += costo

        # Imprimir encabezado
        print(f"\n{'Producto':<25}", end="")
        for m in meses:
            print(f"{m+'.'+año[-2:]:>9}", end="")
        print()

        # Imprimir filas por libro, con salto de línea entre filas
        for idLibro, valores in resumen.items():
            nombre = libros[idLibro]["nombre"][:23]
            print(f"{nombre:<25}", end="")
            for v in valores:
                print(f"{v:>9}", end="")
            print("\n")  # Salto de línea extra entre filas

        # (Opcional) Totales por mes
        print(f"{'TOTAL':<25}", end="")
        for i in range(12):
            totalMes = sum(resumen[libro][i] for libro in resumen)
            print(f"{totalMes:>9}", end="")
        print("\n")
        return
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)


def listarPrestamosAtrasados(): #Funcion para listar los prestamos atrasados
    '''
    Muestra un listado de los prestamos atrasados, es decir aquellos cuyo valor Devuelto=false y fechaDevolucion sea anterior a la fecha actual
    
    PARAMETROS:
    SALIDA:
    Imprime un listado de todos los prestamos atrasados
    '''
    try:
        #Leo archivo json de Alumnos y lo paso a un diccionario
        Alumnos=open("Alumnos.json",mode="r",encoding="utf-8")
        alumnos=json.load(Alumnos)
        Alumnos.close()
        #Leer archivo json de Libros y cargar en un diccionario
        Libros = open("Libros.json", mode="r", encoding="utf-8")
        libros = json.load(Libros)
        Libros.close()
        #Leo archivo json de Prestamos y lo paso a un diccionario
        Prestamos=open("Prestamos.json",mode="r",encoding="utf-8")
        prestamos=json.load(Prestamos)
        Prestamos.close()
        fechaActual = datetime.now()
        print("Listado de préstamos atrasados al", fechaActual.strftime("%Y-%m-%d %H:%M:%S"))
        print("-" * 55)

        for idPrestamo in prestamos:
            datosPrestamo = prestamos[idPrestamo]
            fechaDevolucion = datetime.strptime(datosPrestamo["fechaDevolucion"], "%Y.%m.%d %H.%M.%S")

            if fechaDevolucion < fechaActual and datosPrestamo.get("Devuelto") == False:
                idAlumno = datosPrestamo["IdAlumno"]
                nombreAlumno = alumnos[idAlumno]["nombre"] + " " + alumnos[idAlumno]["apellido"]
                diasAtraso = (fechaActual - fechaDevolucion).days

                print(f"ID Préstamo: {idPrestamo}")
                print(f"Alumno: {nombreAlumno}")
                print(f"ID Alumno: {idAlumno}")
                print(f"ID Libro: {datosPrestamo['IdLibro']}")
                print(f"Tipo de préstamo: {datosPrestamo['tipoPrestamo']}")
                print(f"Costo del préstamo: ${datosPrestamo['costoPrestamo']}")
                print(f"Fecha de devolución: {datosPrestamo['fechaDevolucion']}")
                print(f"Días de atraso: {diasAtraso}")
                print("-" * 55)
        return
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

        
        

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    
    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 4
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de Alumnos")
            print("[2] Gestión de Libros")
            print("[3] Gestión de Préstamos")
            print("[4] Informes")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcionSubmenu = ""
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0": # Opción salir del programa
            exit()

        elif opcionMenuPrincipal == "1":   # Opción 1 del menú principal, accede a la gestion de alumnos
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE ALUMNOS")
                    print("---------------------------")
                    print("[1] Ingresar Alumno")
                    print("[2] Modificar Alumno")
                    print("[3] Eliminar Alumno")
                    print("[4] Listado de Alumnos Activos")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú, permite cargar un alumno
                    ingresoAlumno()
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú, permite modificar la informacion de un alumno
                    modificarAlumno()
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú, permite realizar un borrado logico de un alumno
                    
                    eliminarAlumno()
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú, muestra un listado de los alumnos activos
                    listarAlumnos()

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        elif opcionMenuPrincipal == "2":   # Opción 2 del menú principal, accede a la gestion de libros
            while True:
                while True:
                    opciones = 6
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE LIBROS")
                    print("---------------------------")
                    print("[1] Ingresar Libro")
                    print("[2] Modificar Libro")
                    print("[3] Eliminar Libro")
                    print("[4] Listado de Libros Activos")
                    print("[5] Listado de Libros por Autor")
                    print("[6] Listado de Libros por Categoría")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú, permite ingresar un nuevo libro
                    ingresoLibros()
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú, accede a modificar libro
                    modificarLibro()
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú, permite eliminar logicamente un libro
                    eliminarLibro()
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú, muestra un listado de los libros activos
                    librosActivos()
                    
                elif opcionSubmenu == "5":   # Opción 5 el submenú, muestra un listado de libros segun su autor
                    buscarLibrosPorAutor()
                
                elif opcionSubmenu == "6":   # Opción 6 del submenú, muestra un listado de libros segun su categoria
                    buscarLibrosPorCategoria()
                    

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")
        
        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal, accede a registrar prestamo
            while True:
                while True:
                    opciones = 2
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > PRESTAMOS")
                    print("---------------------------")
                    print("[1] Registrar Prestamo")
                    print("[2] Devolver Prestamo")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    registrarPrestamo()
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    devolverPrestamo()
                

            if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
                input("\nPresione ENTER para volver al menú.")
                print("\n\n")
        
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal, accede a los informes
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > INFORMES")
                    print("---------------------------")
                    print("[1] Préstamos del Mes")
                    print("[2] Resumen Anual de Préstamos por Libro (cantidades)")
                    print("[3] Resumen Anual de Préstamos por Libro (pesos)")
                    print("[4] Resumen de Préstamos Atrasados")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    listarPrestamosMesActual()
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    año = int(input("Ingrese el año a realizar el resumen: "))
                    while año <2000 or año>2026:
                        print("Error, ingrese un año entre el 2000 y el 2026")
                        año = int(input("Ingrese el año a realizar el resumen: "))
                    año=str(año)                       
                    resumenAnualPrestamosCantidadTabla(año)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    año = int(input("Ingrese el año a realizar el resumen: "))
                    while año <2000 or año>2026:
                        print("Error, ingrese un año entre el 2000 y el 2026")
                        año = int(input("Ingrese el año a realizar el resumen: "))
                    año=str(año) 
                    resumenAnualPrestamosPesosTabla(año)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    listarPrestamosAtrasados()


        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


#---------------------------------------------------------------------------------------------
# Inicialización de variables
#----------------------------------------------------------------------------------------------
 #Estos eran los diccionarios que utilizamos en la version previa, actualmente se utilizan archivos JSON que fueron generados en base a estos diccionarios   
    """
    Alumnos = {
    "1001": {"activo": True, "nombre": "Sofía", "apellido": "Martínez", "direccion": "Av. Corrientes 1234", "email": "sofia.martinez@gmail.com", "carrera": "Ingeniería en Sistemas", "telefonos": {"telefono1": "1134567890", "telefono2": "1145678901", "telefono3": "1156789012"}},
    "1002": {"activo": True, "nombre": "Lucas", "apellido": "Fernández", "direccion": "Calle Falsa 123", "email": "lucas.fernandez@gmail.com", "carrera": "Licenciatura en Sistemas", "telefonos": {"telefono1": "1176543210", "telefono2": "", "telefono3": ""}},
    "1003": {"activo": True, "nombre": "María", "apellido": "Gómez", "direccion": "Av. San Juan 456", "email": "maria.gomez@gmail.com", "carrera": "Ingeniería Industrial", "telefonos": {"telefono1": "1133344556", "telefono2": "", "telefono3": ""}},
    "1004": {"activo": True, "nombre": "Tomás", "apellido": "Pérez", "direccion": "Av. Libertador 789", "email": "tomas.perez@gmail.com", "carrera": "Contador Público", "telefonos": {"telefono1": "1155556666", "telefono2": "1177778888", "telefono3": ""}},
    "1005": {"activo": True, "nombre": "Camila", "apellido": "López", "direccion": "Calle Mendoza 234", "email": "camila.lopez@gmail.com", "carrera": "Derecho", "telefonos": {"telefono1": "1166667777", "telefono2": "", "telefono3": ""}},
    "1006": {"activo": True, "nombre": "Mateo", "apellido": "Rodríguez", "direccion": "Calle Salta 100", "email": "mateo.rodriguez@gmail.com", "carrera": "Medicina", "telefonos": {"telefono1": "1188889999", "telefono2": "1199990000", "telefono3": ""}},
    "1007": {"activo": True, "nombre": "Valentina", "apellido": "Díaz", "direccion": "Av. Córdoba 900", "email": "valentina.diaz@gmail.com", "carrera": "Arquitectura", "telefonos": {"telefono1": "1133214455", "telefono2": "", "telefono3": ""}},
    "1008": {"activo": True, "nombre": "Julián", "apellido": "Sánchez", "direccion": "Calle Perú 678", "email": "julian.sanchez@gmail.com", "carrera": "Psicología", "telefonos": {"telefono1": "1122233344", "telefono2": "", "telefono3": ""}},
    "1009": {"activo": True, "nombre": "Martina", "apellido": "Romero", "direccion": "Av. Rivadavia 200", "email": "martina.romero@gmail.com", "carrera": "Diseño Gráfico", "telefonos": {"telefono1": "1165432109", "telefono2": "", "telefono3": ""}},
    "1010": {"activo": True, "nombre": "Benjamín", "apellido": "Ruiz", "direccion": "Calle Tucumán 300", "email": "benjamin.ruiz@gmail.com", "carrera": "Ingeniería Civil", "telefonos": {"telefono1": "1144433221", "telefono2": "", "telefono3": ""}}
}
    
    Prestamos = {
    "2025.06.01 09.15.00": {"IdAlumno": "1001", "IdLibro": "L001", "tipoPrestamo": 1,"costoPrestamo": 150, "fechaDevolucion": "2025.06.08 09.15.00", "Devuelto": True},
    "2025.06.02 14.30.00": {"IdAlumno": "1002", "IdLibro": "L002", "tipoPrestamo": 2,"costoPrestamo": 120, "fechaDevolucion": "2025.06.17 14.30.00", "Devuelto": False},
    "2024.06.02 14.30.00": {"IdAlumno": "1002", "IdLibro": "L002", "tipoPrestamo": 2,"costoPrestamo": 120, "fechaDevolucion": "2025.06.17 14.30.00", "Devuelto": True},
    "2025.06.03 10.00.00": {"IdAlumno": "1003", "IdLibro": "L003", "tipoPrestamo": 3,"costoPrestamo": 200, "fechaDevolucion": "2025.07.03 10.00.00", "Devuelto": False},
    "2025.06.04 11.45.00": {"IdAlumno": "1004", "IdLibro": "L004", "tipoPrestamo": 1,"costoPrestamo": 180, "fechaDevolucion": "2025.06.11 11.45.00", "Devuelto": True},
    "2024.06.05 13.20.00": {"IdAlumno": "1005", "IdLibro": "L005", "tipoPrestamo": 2,"costoPrestamo": 300, "fechaDevolucion": "2024.06.20 13.20.00", "Devuelto": False},
    "2024.06.06 08.10.00": {"IdAlumno": "1006", "IdLibro": "L006", "tipoPrestamo": 3,"costoPrestamo": 450, "fechaDevolucion": "2024.07.06 08.10.00", "Devuelto": False},
    "2025.06.07 15.30.00": {"IdAlumno": "1007", "IdLibro": "L007", "tipoPrestamo": 1,"costoPrestamo": 170, "fechaDevolucion": "2025.06.14 15.30.00", "Devuelto": True},
    "2025.06.08 12.25.00": {"IdAlumno": "1008", "IdLibro": "L008", "tipoPrestamo": 2,"costoPrestamo": 220, "fechaDevolucion": "2025.06.23 12.25.00", "Devuelto": False},
    "2022.06.09 09.00.00": {"IdAlumno": "1009", "IdLibro": "L009", "tipoPrestamo": 3,"costoPrestamo": 600, "fechaDevolucion": "2022.07.09 09.00.00", "Devuelto": False}
}
    Libros = {
    "L001": {"activo": True, "stock": 7, "nombre": "Cien Años de Soledad", "editorial": "Sudamericana", "categoria": "Novela", "autores": {"autor1": "Julio Cortázar", "autor2": "", "autor3": ""}, "costo": 350},
    "L002": {"activo": True, "stock": 5, "nombre": "1984", "editorial": "Secker & Warburg", "categoria": "Distopía", "autores": {"autor1": "George Orwell", "autor2": "", "autor3": ""}, "costo": 280},
    "L003": {"activo": True, "stock": 3, "nombre": "El Principito", "editorial": "Reynal & Hitchcock", "categoria": "Fantasía", "autores": {"autor1": "Antoine de Saint-Exupéry", "autor2": "", "autor3": ""}, "costo": 150},
    "L004": {"activo": True, "stock": 4, "nombre": "Don Quijote de la Mancha", "editorial": "Francisco de Robles", "categoria": "Clásico", "autores": {"autor1": "Miguel de Cervantes", "autor2": "", "autor3": ""}, "costo": 400},
    "L005": {"activo": True, "stock": 2, "nombre": "La Sombra del Viento", "editorial": "Planeta", "categoria": "Misterio", "autores": {"autor1": "Carlos Ruiz Zafón", "autor2": "", "autor3": ""}, "costo": 320},
    "L006": {"activo": True, "stock": 8, "nombre": "Rayuela", "editorial": "Sudamericana", "categoria": "Novela", "autores": {"autor1": "Julio Cortázar", "autor2": "", "autor3": ""}, "costo": 270},
    "L007": {"activo": True, "stock": 6, "nombre": "Ficciones", "editorial": "Sur", "categoria": "Cuentos", "autores": {"autor1": "Jorge Luis Borges", "autor2": "", "autor3": ""}, "costo": 310},
    "L008": {"activo": True, "stock": 10, "nombre": "Harry Potter y la piedra filosofal", "editorial": "Salamandra", "categoria": "Fantasía", "autores": {"autor1": "J.K. Rowling", "autor2": "", "autor3": ""}, "costo": 380},
    "L009": {"activo": True, "stock": 1, "nombre": "Los Juegos del Hambre", "editorial": "Scholastic", "categoria": "Ciencia Ficción", "autores": {"autor1": "Suzanne Collins", "autor2": "", "autor3": ""}, "costo": 290},
    "L010": {"activo": True, "stock": 5, "nombre": "Orgullo y Prejuicio", "editorial": "T. Egerton", "categoria": "Romance", "autores": {"autor1": "Jane Austen", "autor2": "", "autor3": ""}, "costo": 260}
}
    """
# Punto de entrada al programa
main()

