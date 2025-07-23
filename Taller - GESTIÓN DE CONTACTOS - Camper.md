# Taller

## GESTIÓN DE CONTACTOS

A continuación se ejemplifica paso a paso un mini taller para crear una pequeña aplicación de línea de comandos que permita **Crear, Leer, Actualizar y Eliminar** registros de contactos, almacenándolos en un archivo json (`contacts.json`). Cada contacto tendrá:

- **ID** (entero único)
- **Nombre** (cadena)
- **Teléfono** (cadena)
- **Email** (cadena)

Se empleará un formato simple donde cada elemento del array del archivo `contacts.json` corresponde a un contacto:

```json
[
  {
    "ID": 100,
    "Nombre": "No es Johlver",
    "Telefono": "3176126174",
    "Email": "no.soy.jolver@gmail.com"
  },
  ....
]
```

### Requerimientos

1. Menú de consola para CRUD de contactos.
   El Menú de debe permitir las siguientes acciones:
   1. Listar todos los contactos
   2. Crear nuevo contacto
   3. Actualizar contacto
   4. Eliminar contacto
2.  Verifica si el archivo de datos existe. Si no existe, lo crea vacío.
3. Lee todos los contactos del archivo y devuelve una lista de diccionarios.
4. Sobrescribe el archivo con la lista completa de contactos.
5.  Crea un nuevo contacto con ID automático (1 + máximo ID existente).
6.  Muestra todos los contactos en pantalla.
7. Actualiza campos de un contacto dado su ID.
8. Elimina un contacto por su ID.

