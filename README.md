# Python-Project-Software-Project-Management
A Project in Python


[EN]
Project Statement:
A software development company in our city has commissioned us to develop a system for managing Software Projects. For each project, the following information
is known:

* Project number
* Title
* Update date in dd-mm-yyyy format, validating that the year is between 2000 and 2022
* Language (with 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8:C#, 9:VB, 10:Go)
* Number of lines of code

We are asked to develop a program in two modules: one of them must contain the definition of the class of the record and the basic functions that allow to
handle a record, and the other must contain the main program, which must be controlled by a menu of options to allow the following:

Load projects: The generation of n software projects loaded into an array of records. To do this, data can be generated totally randomly or have complete 
pre-loaded projects and randomly selecting from them. Each time this option is selected during execution, data will be added to the array, without deleting
the ones that were already loaded. The project number must not be repeated within the array.

List projects: Show all projects contained in the array, but sorted alphabetically by title. Each project must occupy a maximum of two lines on the screen,
and instead of showing the language identifier, its name must be displayed.

Update project: Search if there is a project with number x, where x is a value entered by keyboard. If it exists, it should allow modifying its number of
lines of code and update date (remembering that it must comply with the dd-mm-yyyy format). If it doesn't exist, it should indicate with a message.

Summary by language: Calculate the amount of lines of code accumulated by language. Show the results taking into account that the language name must be 
displayed instead of the code.

Summary by year: Calculate the number of projects per update year, considering the years between 2000 and 2022 inclusive. Show the results only for the 
years that have some software project.

Filter language: Show the software projects ordered by project number in ascending order, of language ln, where ln is a value entered by keyboard.

Productivity: Based on the result obtained in point 5, determine the year with the highest number of updated projects, considering showing all years 
if there is more than one with that amount.

============================================================================================================================================================

[ES]
Enunciado del Proyecto:
Una empresa de desarrollo de software de nuestra ciudad nos encarga un sistema para la gestión de Proyectos de Software. De cada proyecto se conoce:

* Número de proyecto
* Título
* Fecha de actualización con el formato dd-mm-yyyy validando que el año esté entre 2000 y 2022
* Lenguaje (siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go)
* Cantidad de líneas de código

Se pide desarrollar un programa en dos módulos: uno de ellos debe contener la definición de la clase del regisstro y las funciones básicas que permitan 
manejar un registro, y el otro debe contener el programa principal, que debe estar controlado por un menú de opciones para permitir hacer lo siguiente:

1) Cargar proyectos: La generación de n proyectos de software cargados en un arreglo de registros. Para ello se pueden generar los datos totalmente aleatorios
o bien contar con proyectos completos precargados e ir seleccionando aleatoriamente entre los mismos. Cada vez que selecciona esta opción durante la ejecución 
se agregarán datos al arreglo, sin eliminar los que ya estaban cargados. El número del proyecto no debe repetirse dentro del arreglo.

2) Listar proyectos: Mostrar todos los proyectos contenidos en el arreglo, pero ordenados alfabéticamente por título. Cada proyecto debe ocupar un máximo de dos 
líneas en pantalla y en lugar de mostrarse el identificador del lenguaje se debe mostrar su nombre.

3) Actualizar proyecto: Buscar si existe un proyecto con número x, siendo x un valor que se ingrese por teclado. Si existe, se debe permitir modificar su 
cantidad de líneas de código y la fecha de actualización (recuerde que debe cumplir con el formato dd-mm-yyyy). Si no existe, debe indicar con un mensaje.

4) Resumen por lenguaje: Calcular la cantidad de líneas de código acumuladas por lenguaje. Mostrar los resultados teniendo en cuenta que se debe visualizar 
el nombre del lenguaje en lugar del código. 

5) Resumen por año:  Calcular la cantidad de proyectos por año de actualización, considerando los años entre 2000 y 2022 inlcuidos ambos. Mostrar los 
resultados sólo de los años que tengan algún proyecto de software.

6) Filtrar lenguaje: Mostrar los proyectos de software ordenados por número de proyecto de manera ascendente, del lenguaje ln, siendo ln un valor ingresado 
por teclado.

7) Productividad: A partir del resultado obtenido en el punto 5, determinar el año con mayor cantidad de proyectos actualizados, considerando mostrar todos 
los años si fuera más de uno con dicha cantidad.

