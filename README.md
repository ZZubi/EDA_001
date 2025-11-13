## 📊 Exploratory Data Analysis (EDA) sobre la Adicción a Redes Sociales en Estudiantes

Este repositorio contiene un **Análisis Exploratorio de Datos (EDA)** centrado en el estudio de la **adicción a las redes sociales** y su impacto en el rendimiento académico y la salud mental de estudiantes a nivel global. El análisis utiliza el *Student Social Media & Relationships dataset* obtenido desde [Kaggle](https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships) para investigar patrones de uso, preferencias de plataforma y la autopercepción de adicción entre los participantes.

---

### 📝 **Resumen del Dataset Utilizado**

El *Student Social Media & Relationships dataset* compila registros anónimos sobre los comportamientos de estudiantes en redes sociales y sus resultados de vida relacionados. Abarca múltiples países y niveles académicos, enfocándose en dimensiones clave como la intensidad de uso, las plataformas preferidas y otros parámetros asociados con la salud mental y el bienestar emocional. Cada fila representa la respuesta de un estudiante a una encuesta, ofreciendo una instantánea transversal ideal para análisis estadístico.

La **población** incluye estudiantes de **16 a 25 años** matriculados en secundaria, pregrado o posgrado. La **cobertura geográfica** es amplia e incluye países como Bangladesh, India, EE. UU., Reino Unido, Canadá, Australia, Alemania, Brasil, Japón y Corea del Sur. Los **datos fueron recolectados** mediante una única encuesta en línea en el primer trimestre de 2025. El **diseño de la encuesta** adaptó preguntas de escalas validadas sobre adicción a redes sociales (como la Escala de Adicción a Redes Sociales de Bergen) e índices de conflicto en relaciones, asegurando diversidad académica y geográfica en el reclutamiento.

---

### ❓ **Hipótesis a Responder (iniciales)**

El EDA está diseñado para probar y validar las siguientes **cuatro hipótesis** principales relacionadas con el uso de redes sociales en la población estudiantil:

* Instagram y Tik Tok son las redes sociales donde, de media, más horas dedican los participantes de la encuesta

* Los usuarios de las 2 redes sociales donde más horas invierten de media los encuestados, puntuan en la **Bergen Social Media Addiction Scale** como más adictos que aquellos encuestados con preferencia por otras redes sociales

* Los usuarios de las 2 redes sociales donde más horas invierten de media los encuestados, perciben que el uso de las redes sociales afecta negativamente a su rendimiento académico

* Existe una fuerte correlación negativa entre el número de horas dedicados a redes sociales y la puntuación que se otorgan a sí mismos en el apartado de salud mental

---

### ❓ **Hipótesis a Responder (tras comenzar a trabajar en los datos)**

Tras analizar y trabajar los datos en mayor profundidad, **las hipótesis han debido redefinirse y finalmente han quedado de la siguiente manera:**

* Instagram y Tik Tok son las redes sociales donde, de media, más horas dedican los participantes de la encuesta

* Los usuarios que mayoritariamente usan Instagram y Tik Tok, puntuan como más adictos en la **Bergen Social Media Addiction Scale**  que aquellos encuestados con preferencia por otras redes sociales

* Los usuarios que mayoritariamente usan Instagram y Tik Tok, perciben que el uso de las redes sociales afecta negativamente a su rendimiento académico que aquellos encuestados con preferencia por otras redes sociales

* Existe una fuerte correlación **negativa** entre el número de horas dedicados a redes sociales y la puntuación que se otorgan a sí mismos en el apartado de salud mental. Esta hipótesis trata de profundizar en si a nivel autopercibido existe relación entre el elevado uso de redes sociales y una peor salud mental

* Existe una fuerte correlación **positiva** entre el número de horas dedicados a redes sociales y el número de conflictos que los usuarios tienen con familiares, amigos y compañeros en relación con el uso de estas plataformas
---

### ⚙️ **Estructura del Repositorio**

* `src/data`: todos los archivos de datos utilizados en el analisis, incluyendo datos de origen y archivos intermedios
* `src/notebooks`: notebooks usados para pruebas y generación de resultados intermedios.
* `src/utils`: módulos, funciones auxiliares o clases creados para el desarrollo del proyecto.
* `src/memoria.ipynb`: notebook con el resumen de los pasos de la analítica.

### 💻 **Ejecutar creación de gráficos**

* Ir la ruta `src/utils`
* Ejecutar:
> python .\main.py