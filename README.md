
# Aplicación del principio SOLID en el proyecto Movie Fetcher

En el proyecto Movie Fetcher, se han aplicado los siguientes principios SOLID:

## Principio de responsabilidad única (SRP)

El principio de responsabilidad única establece que una clase o módulo debe tener una única razón para cambiar. En el proyecto Movie Fetcher se puede observar la aplicación de este principio en los siguientes métodos:

- `get_movies`: Este método se encarga de obtener la información de las películas y la devuelve en varias listas. Su única responsabilidad es obtener la información, no modificarla o transformarla.
- `parse_movie`: Este método se encarga de transformar la información obtenida por `get_movies` en un diccionario con los campos correspondientes. Su única responsabilidad es la transformación de datos, no la obtención o almacenamiento de los mismos.
- `Movie`: La clase `Movie` se encarga de almacenar la información de una película. Su única responsabilidad es almacenar y proporcionar acceso a la información de la película.

## Principio abierto/cerrado (OCP)

El principio abierto/cerrado establece que una entidad de software debe estar abierta a la extensión pero cerrada a la modificación. En el proyecto Movie Fetcher se puede observar la aplicación de este principio en los siguientes métodos:

- `scrape_movies`: Este método se encarga de obtener la información de las películas y transformarla en objetos de la clase `Movie`. Si se desea añadir un nuevo campo a las películas, no es necesario modificar este método, sino simplemente añadir el campo correspondiente a la clase `Movie` y actualizar el método `parse_movie` para incluir el nuevo campo.
- `save_movies_to_csv`: Este método se encarga de guardar la información de las películas en un archivo CSV. Si se desea cambiar el formato de salida, no es necesario modificar este método, sino simplemente añadir un nuevo método que convierta la información de las películas en el formato deseado.

## Principio de sustitución de Liskov (LSP)

El principio de sustitución de Liskov establece que una clase derivada debe ser sustituible por su clase base sin alterar el comportamiento del programa. En el proyecto Movie Fetcher se puede observar la aplicación de este principio en la clase `Movie`. Cualquier objeto de la clase `Movie` puede ser utilizado en lugar de un objeto de su clase base (por ejemplo, `object`) sin alterar el comportamiento del programa.

## Principio de segregación de la interfaz (ISP)

El principio de segregación de la interfaz establece que una clase no debe ser forzada a depender de métodos que no utiliza. En el proyecto Movie Fetcher se puede observar la aplicación de este principio en la clase `Movie`. La clase `Movie` define sólo los métodos necesarios para acceder a la información de la película y no depende de otros métodos innecesarios.

## Principio de inversión de dependencia (DIP)

El principio de inversión de dependencia establece que los módulos de alto nivel no deben depender de módulos de bajo nivel, sino de abstracciones. En el proyecto Movie Fetcher se puede observar la aplicación de este principio en los siguientes métodos:

- `save_movies_to_csv`: Este método depende de la abstracción proporcionada por el módulo `csv`, en lugar de depender directamente de la implementación de `csv`.
