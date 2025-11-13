###########################################################################################################
# Utilizaremos este main.py para generar los gráficos de todas las hipótesis y guardarlos como archivo PNG 
# para ser usados desde la memoria
###########################################################################################################

###########################################################################################################
# Importar librerías necesarias
###########################################################################################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


###########################################################################################################
# Carga de datos
###########################################################################################################

clean_data_df = pd.read_csv("..\\data\\CLEAN_Students_Social_Media_Addiction.csv")
clean_data_df.index = clean_data_df["Student_ID"]
clean_data_df = clean_data_df.drop(columns=["Unnamed: 0"]) # Eliminamos la columna que ha quedado guardada como índice

###########################################################################################################
# Hipótesis 1.1
###########################################################################################################

# Sub-hipótesis 1: A nivel de conteo, Instagram y Tik Tok son las redes sociales que más veces han entrado en la categoría de "Most_Used_Platform" de entre todas las del dataset
most_used_platform_count = clean_data_df.groupby("Most_Used_Platform")["Student_ID"].count().reset_index()
most_used_platform_count.columns = ["Most_Used_Platform", "Count"]
most_used_platform_count = most_used_platform_count.sort_values(by="Count", ascending=False)

# Extraemos el gráfico a mostrar
plt.figure(figsize=(12, 8))

fig = sns.barplot(
    data=most_used_platform_count, 
    hue=most_used_platform_count["Most_Used_Platform"],
    x=most_used_platform_count["Most_Used_Platform"],
    y=most_used_platform_count["Count"],
    palette="viridis")

for p in fig.patches:
    # Get the height of the bar (the value on the y-axis)
    height = p.get_height()
    final_label = f'{height:.2f}'

    # Determine where to place the label:
    # x-coordinate: p.get_x() + p.get_width() / 2 (Center of the bar)
    # y-coordinate: height / 2 (Halfway up the bar, inside)

    # Add the text annotation
    fig.text(
        x=p.get_x() + p.get_width() / 2.,  # Center horizontally
        y=height * 0.5,                   # Place vertically at 50% height
        s=final_label,                     # The text to display
        ha='center',                      # Horizontal alignment
        va='center',                      # Vertical alignment
        color='white',                    # Use a contrasting color
        fontsize=12,
        fontweight='bold'
    )

fig.set_title("Number of times reported as 'Most Used Platform'" + "\n", fontweight='bold', fontsize=14);
fig.set_xlabel("Most Used Platform", fontweight='bold', fontsize=14);
fig.set_ylabel("Reported times", fontweight='bold', fontsize=14)
plt.savefig('..\\data\\images\\01.01-Hypothesis.png', dpi=600)

###########################################################################################################
# Hipótesis 1.2
###########################################################################################################

# Sub-hipótesis 2: Los usuarios que reportan como "Most_Used_Platform" las redes Instagram y Tik Tok, también reportan de media un mayor uso de redes sociales al día

mean_daily_usage_hours_grouped_by_most_used_platform = clean_data_df.groupby("Most_Used_Platform")['Avg_Daily_Usage_Hours'].mean().reset_index()
mean_daily_usage_hours_grouped_by_most_used_platform.columns = ["Most_Used_Platform", "Avg_Daily_Usage_Hours_of_ALL_social_media"]
mean_daily_usage_hours_grouped_by_most_used_platform = mean_daily_usage_hours_grouped_by_most_used_platform.sort_values(by="Avg_Daily_Usage_Hours_of_ALL_social_media", ascending=False)

# Respecto al mayor dato de "Avg_Daily_Usage_Hours_of_ALL_social_media", vamos a revisar qué porcentaje de dicho valor representan el resto de filas:

top_usage_baseline = mean_daily_usage_hours_grouped_by_most_used_platform.iloc[[0]]["Avg_Daily_Usage_Hours_of_ALL_social_media"].item()

mean_daily_usage_hours_grouped_by_most_used_platform["Relative_to_TOP_usage_%"] = (mean_daily_usage_hours_grouped_by_most_used_platform["Avg_Daily_Usage_Hours_of_ALL_social_media"] / top_usage_baseline) * 100

# Extraemos el gráfico a mostrar

plt.figure(figsize=(12, 8))

fig = sns.barplot(
    data=mean_daily_usage_hours_grouped_by_most_used_platform, 
    hue=mean_daily_usage_hours_grouped_by_most_used_platform["Most_Used_Platform"],
    x=mean_daily_usage_hours_grouped_by_most_used_platform["Most_Used_Platform"],
    y=mean_daily_usage_hours_grouped_by_most_used_platform["Avg_Daily_Usage_Hours_of_ALL_social_media"],
    palette="viridis")

for p in fig.patches:
    # Get the height of the bar (the value on the y-axis)
    height = p.get_height()

    x_category = fig.get_xticklabels()[fig.patches.index(p)].get_text() # Encuentra la Label del eje X, para poder buscar el porcentaje en el Dataframe

    # 2d. Lookup the specific Label_Text from the DataFrame
    label_percentage = mean_daily_usage_hours_grouped_by_most_used_platform[mean_daily_usage_hours_grouped_by_most_used_platform['Most_Used_Platform'] == x_category]['Relative_to_TOP_usage_%'].iloc[0]
    final_label = f'{height:.2f} h' + "\n" + f'[{label_percentage:.1f}%]' # Format the text (e.g., to 2 decimal places)
    # Determine where to place the label:
    # x-coordinate: p.get_x() + p.get_width() / 2 (Center of the bar)
    # y-coordinate: height / 2 (Halfway up the bar, inside)

    # Add the text annotation
    fig.text(
        x=p.get_x() + p.get_width() / 2.,  # Center horizontally
        y=height * 0.5,                   # Place vertically at 50% height
        s=final_label,                     # The text to display
        ha='center',                      # Horizontal alignment
        va='center',                      # Vertical alignment
        color='white',                    # Use a contrasting color
        fontsize=12,
        fontweight='bold'
    )

fig.set_title("Average daily usage hours on ALL platforms, grouped by reported 'Most Used Platform'" + "\n", fontweight='bold', fontsize=14);
fig.set_xlabel("Most Used Platform", fontweight='bold', fontsize=14);
fig.set_ylabel("Avg Hours/Day on ALL platforms", fontweight='bold', fontsize=14)
plt.savefig('..\\data\\images\\01.02-Hypothesis.png', dpi=600)

###########################################################################################################
# Hipótesis 2
###########################################################################################################

mean_bergen_addiction_scale_grouped_by_most_used_platform = clean_data_df.groupby("Most_Used_Platform")['Addicted_Score'].mean().reset_index()
mean_bergen_addiction_scale_grouped_by_most_used_platform.columns = ["Most_Used_Platform", "Avg_Addicted_Score"]
mean_bergen_addiction_scale_grouped_by_most_used_platform = mean_bergen_addiction_scale_grouped_by_most_used_platform.sort_values(by="Avg_Addicted_Score", ascending=False)

# Respecto al mayor dato de "Avg_Addicted_Score", vamos a revisar qué porcentaje de dicho valor representan el resto de filas:

top_addiction_baseline = mean_bergen_addiction_scale_grouped_by_most_used_platform.iloc[[0]]["Avg_Addicted_Score"].item()

mean_bergen_addiction_scale_grouped_by_most_used_platform["Relative_to_TOP_addicted_score_%"] = (mean_bergen_addiction_scale_grouped_by_most_used_platform["Avg_Addicted_Score"] / top_addiction_baseline) * 100

# Extraemos el gráfico a mostrar

plt.figure(figsize=(12, 8))

fig = sns.barplot(
    data=mean_bergen_addiction_scale_grouped_by_most_used_platform, 
    hue=mean_bergen_addiction_scale_grouped_by_most_used_platform["Most_Used_Platform"],
    x=mean_bergen_addiction_scale_grouped_by_most_used_platform["Most_Used_Platform"],
    y=mean_bergen_addiction_scale_grouped_by_most_used_platform["Avg_Addicted_Score"],
    palette="viridis")

for p in fig.patches:
    # Get the height of the bar (the value on the y-axis)
    height = p.get_height()

    x_category = fig.get_xticklabels()[fig.patches.index(p)].get_text() # Encuentra la Label del eje X, para poder buscar el porcentaje en el Dataframe

    # 2d. Lookup the specific Label_Text from the DataFrame
    label_percentage = mean_bergen_addiction_scale_grouped_by_most_used_platform[mean_bergen_addiction_scale_grouped_by_most_used_platform['Most_Used_Platform'] == x_category]['Relative_to_TOP_addicted_score_%'].iloc[0]
    final_label = f'{height:.2f}' + "\n" + f'[{label_percentage:.1f}%]' # Format the text (e.g., to 2 decimal places)
    # Determine where to place the label:
    # x-coordinate: p.get_x() + p.get_width() / 2 (Center of the bar)
    # y-coordinate: height / 2 (Halfway up the bar, inside)

    # Add the text annotation
    fig.text(
        x=p.get_x() + p.get_width() / 2.,  # Center horizontally
        y=height * 0.5,                   # Place vertically at 50% height
        s=final_label,                     # The text to display
        ha='center',                      # Horizontal alignment
        va='center',                      # Vertical alignment
        color='white',                    # Use a contrasting color
        fontsize=12,
        fontweight='bold'
    )

fig.set_title("Average Addicted Score, grouped by reported 'Most Used Platform'" + "\n", fontweight='bold', fontsize=14);
fig.set_xlabel("Most Used Platform", fontweight='bold', fontsize=14);
fig.set_ylabel("Avg Addicted Score (max 10)", fontweight='bold', fontsize=14)
#plt.ylim(0, 10) # Se ve mejor sin el limite superior en 10
plt.savefig('..\\data\\images\\02-Hypothesis.png', dpi=600)

###########################################################################################################
# Hipótesis 3
###########################################################################################################

# Agrupamos por red social y afectación auto-percibida
percentage_of_students_reporting_social_media_affects_performance = clean_data_df.groupby(["Most_Used_Platform", "Affects_Academic_Performance"])[["Affects_Academic_Performance"]].count()
percentage_of_students_reporting_social_media_affects_performance.columns = ["Affects_Academic_Performance_Count"]

## Debemos calcular el porcentaje de respuestas de cada tipo, para cada red social

# Creamos un dataframe con el conteo total:
most_used_platform_count = clean_data_df.groupby("Most_Used_Platform")["Student_ID"].count().reset_index()
most_used_platform_count.columns = ["Most_Used_Platform", "Total_Platform_Count"]

# Mergeamos el dataframe anterior con el conteo total
percentage_of_students_reporting_social_media_affects_performance_with_totals = pd.merge(percentage_of_students_reporting_social_media_affects_performance.reset_index(), most_used_platform_count, how="left", on="Most_Used_Platform")
percentage_of_students_reporting_social_media_affects_performance_with_totals = percentage_of_students_reporting_social_media_affects_performance_with_totals.set_index(['Most_Used_Platform', 'Affects_Academic_Performance'])

# Calculamos el porcentaje
percentage_of_students_reporting_social_media_affects_performance_with_totals["Affects_Academic_Performance_%"] = percentage_of_students_reporting_social_media_affects_performance_with_totals["Affects_Academic_Performance_Count"] /  percentage_of_students_reporting_social_media_affects_performance_with_totals["Total_Platform_Count"] * 100

# Ordenamos primero los Yes, y luego los que más afectan a los estudios en porcentaje

percentage_of_students_reporting_social_media_affects_performance_with_totals_and_ordered = percentage_of_students_reporting_social_media_affects_performance_with_totals.sort_values(
    by=[
        'Affects_Academic_Performance', # This targets the column/level named 'Product'
        'Affects_Academic_Performance_%'
    ],
    ascending=[
        False,   # Sort Affects_Academic_Performance descending (Yes then No)
        False   # Sort Affects_Academic_Performance_ (highest to lowest)
    ]
)

# restablecemos el índice para poder mostrarlo más fácil como gráfico
percentage_of_students_reporting_social_media_affects_performance_with_totals_and_ordered = percentage_of_students_reporting_social_media_affects_performance_with_totals_and_ordered.reset_index()

# Extraemos el gráfico a mostrar

plt.figure(figsize=(13, 6))

fig = sns.barplot(
    data=percentage_of_students_reporting_social_media_affects_performance_with_totals_and_ordered, 
    x=percentage_of_students_reporting_social_media_affects_performance_with_totals_and_ordered["Most_Used_Platform"],
    hue=percentage_of_students_reporting_social_media_affects_performance_with_totals_and_ordered["Affects_Academic_Performance"],
    y=percentage_of_students_reporting_social_media_affects_performance_with_totals_and_ordered["Affects_Academic_Performance_%"],
    palette=["#FF0000","#006400"])

for p in fig.patches:
    # Get the height of the bar (the value on the y-axis)
    height = p.get_height()

    # 2d. Lookup the specific Label_Text from the DataFrame
    final_label = f'{height:.2f}%' # Format the text (e.g., to 2 decimal places)
    # Determine where to place the label:
    # x-coordinate: p.get_x() + p.get_width() / 2 (Center of the bar)
    # y-coordinate: height / 2 (Halfway up the bar, inside)

    # Add the text annotation
    fig.text(
        x=p.get_x() + p.get_width() / 2.,  # Center horizontally
        y=height * 0.5,                   # Place vertically at 50% height
        s=final_label,                     # The text to display
        ha='center',                      # Horizontal alignment
        va='center',                      # Vertical alignment
        color='white',                    # Use a contrasting color
        fontsize=9,
        fontweight='bold'
    )

fig.set_title("Self perception on how much Social Media Affects Academic Performance" + "\n", fontweight='bold', fontsize=16);
fig.set_xlabel("Most Used Platform", fontweight='bold', fontsize=14);
fig.set_ylabel("Affects Academic Performance (%)", fontweight='bold', fontsize=14)
plt.legend(fontsize=18)
plt.savefig('..\\data\\images\\03-Hypothesis.png', dpi=600)

###########################################################################################################
# Hipótesis 4 y 5 (Matriz de correlación)
###########################################################################################################

# Extraemos la matriz de correlación que servirá para verificar esta hipótesis

f, ax = plt.subplots(figsize=(15, 10))
sns.heatmap(clean_data_df.iloc[:, 1:].corr(numeric_only=True),
            annot=True,
            linewidths=.5,
            ax=ax,
            vmin=-1,
            vmax=1, 
            cmap = "coolwarm")

ax.set_title("Correlation matrix on numeric columns" + "\n", fontweight='bold', fontsize=16);
plt.savefig('..\\data\\images\\04_and_05-Hypothesis.png', dpi=600, bbox_inches="tight")