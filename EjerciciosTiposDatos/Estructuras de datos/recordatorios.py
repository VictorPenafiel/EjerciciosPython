eventos = [['2021-01-01', '11:00', 'Levantarse y ejercitar'],
['2021-05-01', '09:00', 'No hacer nada es feriado, Día del Trabajador'],
['2021-07-16', '13:00', 'No hacer nada es feriado'],
['2021-09-18', '16:00', 'Ramadas'],
['2021-12-25', '00:00', 'Navidad']]

#Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para "Empezar el Año"

eventos.insert(1,['2021-02-02','6:00','Empezar el Año'])

#Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar de tal manera que sea el 16 de Julio"
eventos[2] = ['2021-07-16', '13:00', 'No hacer nada es feriado']

#Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día del trabajo"
eventos.pop(3)

#Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
eventos.insert(4,['2021-12-24', '22:00', 'Cena de Navidad'])
eventos.append(['2021-12-31', '22:00', 'Cena de año nuevo'])
print(eventos)