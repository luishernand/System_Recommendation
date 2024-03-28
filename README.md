## Sistemas de Recomendación  

**Descripción:**  

El objetivo principal de este proyecto es desarrollar un sistema de recomendación de cursos basado en técnicas de Machine Learning. El sistema analizará los patrones de preferencias de aprendizaje de los usuarios, así como las características y metadatos de los cursos, con el fin de recomendar cursos que puedan ser de interés.  

**Objetivos específicos:**  
1. Desarrollar un sistema de recomendación  que analice las calificaciones y preferencias de los usuarios para recomendar los cursos.
2. Realizar diferentes tipos de Motores o Sistema de recomendación: Popularity, Content-based, Colaborative, Avg Weigth, entre otros.

1. Implementar  una aplicación web o una API para que pueda ser utilizado por usuarios finales.  

**¿Qué es un sistema de recomendación?**  
Un sistema de recomendación es una herramienta que establece un conjunto de criterios y valoraciones sobre los datos de los usuarios para realizar predicciones sobre recomendaciones de elementos que puedan ser de utilidad o valor para el usuario. Estos sistemas seleccionan datos proporcionados por el usuario de forma directa o indirecta, y procede a analizar y procesar información del historial del usuario para transformar estos datos en conocimiento de recomendación.  
**Tipos de sistemas de recomendación**  
1. Sistemas de popularidad: Los sistemas basados en la popularidad son implementados principalmente en las ventas de productos o sugerencias concretas. Estos toman como referencia la popularidad del objeto de estudio por una variable principal que puede ser el número de ventas, una característica especial o inclusive una oferta y se muestra de forma general a todos los usuarios que investiguen el área a la que pertenece el objeto. Estos sistemas suelen ser fáciles de implementar y gozan de cierto nivel de efectividad. Su desventaja principal es la imposibilidad de personalizar los criterios de sugerencia para el usuario.
1. Sistemas de contenido: Los sistemas de recomendación basados en contenido son aquellos que tomando en cuenta algunos datos del historial del usuario intenta predecir que busca el usuario y que sugerencias similares puede mostrar. Este tipo de sistemas es uno de los que tiene mayor presencia en la actualidad. Con ellos podemos descubrir opciones que se ajusten a las características de los productos o contenidos que hemos disfrutado con anterioridad y elegir elementos similares nuevos.
1. Sistemas colaborativos:Este tipo de sistema es muy novedoso ya que genera recomendaciones analizando datos, identificando perfiles y haciendo contraste entre la información del perfil del usuario y la de un colectivo de usuarios. Esto permite al modelo aprender a agrupar perfiles similares y aprender de los datos que recibe de forma general, para desarrollar recomendaciones individuales.
1. Filtrado colaborativo: Los filtrados colaborativos funcionan de forma especial para hacer predicciones automáticas sobre los intereses de un usuario en particular mediante la recopilación de preferencias o gustos de un mismo consumidor comparados con los datos suministrados por personas con patrones similares.

**Herramientas y tecnologías utilizadas:**

<pre>Lenguaje de programación: Python
Librerías de Machine Learning: Scikit-learn
Librerías de análisis de datos: Pandas, NumPy
Librerías de procesamiento de texto: NLTK, spaCy
Librerías de visualización de datos: Matplotlib, Seaborn, plotly
Entorno de desarrollo: Jupyter Notebook
Plataforma de despliegue: Streamlit</pre>

**Resultados esperados:**  

Se espera contar con un sistema de recomendación de cursos basado en algoritmos de Machine Learning que pueda proporcionar recomendaciones personalizadas y precisas a los usuarios.  

**Conclusión:**  

El desarrollo de un sistema de recomendación de cursos  representa un desafío emocionante combnando técnicas de análisis de datos, procesamiento de texto y aprendizaje automático. Al utilizar enfoques de los direntes tipos de sistema de recomendación,  el sistema podrá aprovechar tanto la sabiduría colectiva, como el análisis detallado de las características de los datos. 

## Notebooks
| Archivo | Contenido |
|--------|------------------ |
| [Basado en Popularidad](https://nbviewer.org/github/luishernand/System_Recommendation/blob/main/Base%20on%20Popularity.ipynb) | - Sistema basado en popularidad Score   - sistema basado en Weigted Averages  - sistema basado en 50% (popularity score  y Weigted Averages) |
| [KNN Colaborativo](https://nbviewer.org/github/luishernand/System_Recommendation/blob/main/Collaborative%20Filtering.ipynb) | Sistema Colaborativo Utilizando KNN |
| [sigmoid kernel](https://nbviewer.org/github/luishernand/System_Recommendation/blob/main/rec%20collaborative.ipynb) | Sistema colaborativo usando sigmoid kernel |
|[Basado en Contenido](https://nbviewer.org/github/luishernand/System_Recommendation/blob/main/base%20on%20contend.ipynb) | Basado en contenido |
| [sistema de recomendacion con su GUI](https://nbviewer.org/github/luishernand/System_Recommendation/blob/main/sistema%20de%20recomendacion.ipynb) | Basado en popularidad y contenido con sus applicación |



