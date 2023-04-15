#Aplicación del principio SOLID en movie_fetcher.py

El principio SOLID es un conjunto de principios de diseño de software que se enfocan en facilitar el mantenimiento, la escalabilidad y la flexibilidad del código. A continuación, se detalla cómo se aplican estos principios en el archivo movie_fetcher.py.
Principio de responsabilidad única (SRP)

El principio SRP establece que cada clase o función debe tener una única responsabilidad dentro del sistema. En el archivo movie_fetcher.py, podemos observar que la función main() tiene una única responsabilidad: descargar la información de las mejores películas del sitio web de IMDB, guardarla en un archivo CSV y mostrar un mensaje de éxito o fracaso. Por lo tanto, se cumple el principio de SRP en esta función.
Principio de abierto/cerrado (OCP)

El principio OCP establece que una entidad de software debe estar abierta para su extensión pero cerrada para su modificación. En el archivo movie_fetcher.py, podemos observar que la función save_movies_to_csv() está diseñada para ser reutilizable en otras partes del sistema. Por lo tanto, se cumple el principio de OCP en esta función.
Principio de sustitución de Liskov (LSP)

El principio LSP establece que si una clase es una subclase de otra, entonces debe ser posible utilizar objetos de la subclase en lugar de objetos de la superclase sin alterar el comportamiento del programa. En el archivo movie_fetcher.py, no hay clases que hereden de otras, por lo que no es aplicable el principio de LSP.
Principio de segregación de interfaz (ISP)

El principio ISP establece que ninguna clase debe verse forzada a implementar interfaces que no utilice. En el archivo movie_fetcher.py, no hay clases que implementen interfaces, por lo que no es aplicable el principio de ISP.
Principio de inversión de dependencia (DIP)

El principio DIP establece que los módulos de alto nivel no deben depender de los módulos de bajo nivel, sino de abstracciones. En el archivo movie_fetcher.py, la función scrape_movies() depende del módulo movie_scraper.py para obtener la información de las películas. Sin embargo, la función scrape_movies() no depende directamente del módulo movie_scraper.py, sino que utiliza una interfaz abstracta (una función) para obtener la información. Por lo tanto, se cumple el principio de DIP en esta función.

En conclusión, el archivo movie_fetcher.py cumple con el principio SRP, OCP y DIP, y no es aplicable el principio LSP ni ISP. Esto indica que el archivo tiene un buen diseño en términos de mantenibilidad, escalabilidad y flexibilidad.
