import pandas as pd
from scipy.stats import binom_test

# Cargar los datos de la encuesta
path_archivo = 'Encuesta_Resultados_de_Muestra.csv'
df_respuestas = pd.read_csv(path_archivo)

# Calcular el número de éxitos (usuarios dispuestos a pagar precio premium)
exitos_actual = df_respuestas["Disposicion_precio_premium"].gt(0).sum()

# Número total de encuestados
n_actual = len(df_respuestas)

# Proporción observada
proporcion_observada_actual = exitos_actual / n_actual

# Realizar la prueba binomial con hipótesis nula de que al menos el 40% de los usuarios paga el precio premium
prop_esperada_40_actual = 0.4
p_value_40_actual = binom_test(exitos_actual, n_actual, prop_esperada_40_actual, alternative='greater')

# Resultados
print(f"""
      Proporción observada: {round(proporcion_observada_actual*100, 2)}%
      Valor p: {p_value_40_actual:.2e}""")