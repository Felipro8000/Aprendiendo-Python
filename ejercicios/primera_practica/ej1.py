#Ejercicio nro 1
#Un video dura minimo 2.5 horas, promedio 4 hrs y maximo 7hrs
#Hay un video que enseño lo mismo pero duró 1.5 hrs
#a)
#Cual es la diferencia porsentual entre el video de 1.5 hrs y:
#El segundo video mas rapido, el video mas lento y el promedio de los otros videos
#b)
# El promedio de hrs de material sin editar de los videos es en promedio 5hrs
# y el material crudo del video mas rapido es de 3.5 hrs
# Que porsentaje se reduce en cada caso?
#c)
#Ver 10 hrs del video mas rapido, cuantas horas equivalen en los otros videos? Y al reves?

video_minimo = 2.5
video_promedio = 4.0
video_maximo = 7.0
video_veloz = 1.5
video_promedio_crudo = 5.0
video_veloz_crudo = 3.5

diferencia_veloz_minimo = video_veloz * 100 / video_minimo
diferencia_veloz_promedio = video_veloz * 100 / video_promedio
diferencia_veloz_maximo = video_veloz * 100 / video_maximo

print (f"""El video veloz dura:
       {diferencia_veloz_minimo:.2f}%del video mininmo
       {diferencia_veloz_promedio:.2f}% del video promedio
       {diferencia_veloz_maximo:.2f}% del video maximo""")

diferencia_veloz_minimo = 100 - diferencia_veloz_minimo
diferencia_veloz_promedio = 100 - diferencia_veloz_promedio
diferencia_veloz_maximo = 100 - diferencia_veloz_maximo

print (f"""El video veloz dura:
       {diferencia_veloz_minimo}%menos que el video mininmo
       {diferencia_veloz_promedio}% menos que el video promedio
       {diferencia_veloz_maximo}% menos que el video maximo""")


material_desechado_veloz = (video_veloz_crudo - video_veloz)* 100 / video_veloz_crudo
material_desechado_promedio = (video_promedio_crudo - video_promedio)* 100 / video_promedio_crudo

print (f"""El porcentaje de material desechado es del:
       {material_desechado_promedio:.2f}% en caso de un video promedio
       {material_desechado_veloz:.2f}% en caso del video veloz""")

realcion_veloz_minimo = 10 * video_minimo / video_veloz
realcion_minimo_veloz = 10 * video_veloz / video_minimo
realcion_veloz_maximo = 10 * video_maximo / video_veloz
realcion_maximo_veloz = 10 * video_veloz / video_maximo
realcion_veloz_promedio = 10 * video_promedio / video_veloz
realcion_promedio_veloz = 10 * video_veloz / video_promedio

print (f"""Mirar 10hrs el video veloz equivale a mirar
       {realcion_veloz_minimo:.2f} hrs del minimo
       {realcion_veloz_maximo:.2f} hrs del maximo
       {realcion_veloz_promedio:.2f} hrs del promedio
       en cambio mirar diez horas de cada uno de los otros equivale a
       {realcion_minimo_veloz:.2f} hrs del veloz en el caso del minimo
       {realcion_maximo_veloz:.2f} hrs del veloz en el caso del maximo
       {realcion_promedio_veloz:.2f} hrs del veloz en caso del promedio""")