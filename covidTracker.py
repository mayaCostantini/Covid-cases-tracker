from covid import Covid 
import PySimpleGUI as sg
import os.path 
import csv 



covid = Covid()
covid_data = covid.get_data()

countries_list = []


with open('covidData.csv', 'w') as csv_file : 
    csv_writer = csv.writer(csv_file)
    for element in covid_data : 
        csv_writer.writerow([element['id'], 
                            element['country'], 
                            element['confirmed'], 
                            element['active'], 
                            element['deaths'], 
                            element['recovered'], 
                            element['latitude'], 
                            element['longitude'], 
                            element['last_update']])

        countries_list.append(element['country'])

countries_list.sort()


sg.theme('LightGrey')
layout = [  [sg.Text('Welcome to the Covid-19 Desktop Notifier', key = '-TEXT-')],
            # [sg.Text('', key='-TEXT2-')],
            [sg.Button('Choose country'), sg.Button('Close')],
            [sg.Combo(countries_list)]]



window = sg.Window('Covid-19 Desktop Notifier', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks Close
        window.close()
        break
    if event == 'Choose country' : 
        with open('covidData.csv', 'r') as csv_file : 
            csv_reader = csv.reader(csv_file)
            for row in csv_reader : 
                if row[1] == values[0] : 
                    sg.popup('The last Covid-19 numbers for {} are : '.format(values[0]),
                                'Confirmed cases : ' + row[2],
                                'Active cases : ' + row[3],
                                'Deaths : ' + row[4],
                                'Recovered : ' + row[5],
                                )

                    break
window.close()



                    





