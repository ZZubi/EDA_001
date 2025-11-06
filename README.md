## 📊 Exploratory Data Analysis (EDA) sobre la Adicción a Redes Sociales en Estudiantes

Este repositorio contiene un **Análisis Exploratorio de Datos (EDA)** centrado en el estudio de la **adicción a las redes sociales** y su impacto en el rendimiento académico y la salud mental de estudiantes a nivel global. El análisis utiliza el *Student Social Media & Relationships dataset* obtenido desde [Kaggle](https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships) para investigar patrones de uso, preferencias de plataforma y la autopercepción de adicción entre los participantes.

---

### 📝 **Resumen del Dataset Utilizado**

El *Student Social Media & Relationships dataset* compila registros anónimos sobre los comportamientos de estudiantes en redes sociales y sus resultados de vida relacionados. Abarca múltiples países y niveles académicos, enfocándose en dimensiones clave como la intensidad de uso, las plataformas preferidas y otros parámetros asociados con la salud mental y el bienestar emocional. Cada fila representa la respuesta de un estudiante a una encuesta, ofreciendo una instantánea transversal ideal para análisis estadístico.

La **población** incluye estudiantes de **16 a 25 años** matriculados en secundaria, pregrado o posgrado. La **cobertura geográfica** es amplia e incluye países como Bangladesh, India, EE. UU., Reino Unido, Canadá, Australia, Alemania, Brasil, Japón y Corea del Sur. Los **datos fueron recolectados** mediante una única encuesta en línea en el primer trimestre de 2025. El **diseño de la encuesta** adaptó preguntas de escalas validadas sobre adicción a redes sociales (como la Escala de Adicción a Redes Sociales de Bergen) e índices de conflicto en relaciones, asegurando diversidad académica y geográfica en el reclutamiento.

---

### ❓ **Hipótesis a Responder**

El EDA está diseñado para probar y validar las siguientes **cuatro hipótesis** principales relacionadas con el uso de redes sociales en la población estudiantil:

* Instagram y Tik Tok son las redes sociales donde, de media, más horas dedican los participantes de la encuesta

* Los usuarios de las 2 redes sociales donde más horas invierten de media los encuestados, puntuan en la **Bergen Social Media Addiction Scale** como más adictos que aquellos encuestados que invierten menos horas

* Los usuarios de las 2 redes sociales donde más horas invierten de media los encuestados, perciben que el uso de las redes sociales afecta negativamente a su rendimiento académico

* Existe una fuerte correlación negativa entre el número de horas dedicados a redes sociales y la puntuación que se otorgan a sí mismos en el apartado de salud mental

---

### ⚙️ **Estructura del Repositorio**

* `src/data`: todos los archivos de datos utilizados en el analisis, incluyendo datos de origen y archivos intermedios
* `src/notebooks`: notebooks usados para pruebas y generación de resultados intermedios.
* `src/utils`: módulos, funciones auxiliares o clases creados para el desarrollo del proyecto.
* `src/memoria.ipynb`: notebook con el resumen de los pasos de la analítica.
