def temperatura():
    '''
    Função que busca informações sobre a temperatura de São Paulo no site 'ClimaTempo'.
    '''

    import requests
    from bs4 import BeautifulSoup
    import datetime

    url = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp'

    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    temp_min = soup.find(id='min-temp-1').text
    temp_max = soup.find(id='max-temp-1').text
    chuva_info = soup.find(class_='_margin-l-5').find_next(class_='_margin-l-5')\
        .find_next(class_='_margin-l-5').text.replace('\n', ' ').split()
    chuva_mm = chuva_info[0]
    chuva_porcento = chuva_info[2].replace('%', '')
    qualidade_ar = soup.find(class_='value').text.replace('\n', '')
    dia = datetime.date.today().day
    mes = datetime.date.today().month
    ano = datetime.date.today().year

    print(f'Previsão de Hoje {dia}/{mes} em São Paulo - SP')
    print(f'Temperatura Máxima: {temp_max}\nTemperatura Mínima: {temp_min}')
    print(f'Chuva: {chuva_mm} - {chuva_porcento}%')
    if int(chuva_porcento) > 60:
        print('Grandes Possibilidades de chuva!')
    print(f'Qualidade do ar: {qualidade_ar}')


temperatura()
