# ISS Location

## Descrição

O projeto ISS Location consiste em um código que cria um bloco de notas informativo sobre a Estação Espacial Internacional (ISS). Ele fornece detalhes sobre quantas pessoas estão a bordo da ISS atualmente, incluindo seus nomes, e indica a localização geográfica da ISS em tempo real. O programa abre uma imagem do mapa-múndi com um ícone da ISS que se move a cada 10 segundos, mostrando sua posição no mapa enquanto imprime no terminal as coordenadas geográficas (latitude e longitude) da ISS.

## Funcionalidades

- Informa quantas pessoas estão a bordo da ISS e seus respectivos nomes.
- Mostra a localização geográfica da ISS em tempo real em um mapa-múndi.
- Atualiza a posição da ISS a cada 10 segundos.

## Bibliotecas Utilizadas

- json: Para manipulação de dados em formato JSON.
- turtle: Para desenhar a representação gráfica da ISS em um mapa-múndi.
- urllib: Para fazer solicitações HTTP para a API da NASA.
- time: Para controlar o intervalo de atualização da posição da ISS.
- webbrowser: Para abrir a imagem do mapa-múndi em um navegador da web.
- geocoder: Para converter coordenadas geográficas em informações de localização.

## APIs Utilizadas

- [API da NASA - Astros](http://api.open-notify.org/astros.json): Fornece informações sobre as pessoas atualmente a bordo da ISS.
- [API da NASA - ISS Location](http://api.open-notify.org/iss-now.json): Retorna a localização geográfica atual da ISS.

## Como Executar

1. Certifique-se de ter as bibliotecas necessárias instaladas.
2. Execute o script iss_location.py.
3. Aguarde enquanto o programa obtém os dados da API da NASA e abre a imagem do mapa-múndi.
4. Observe a posição atual da ISS no mapa e as informações de localização impressas no terminal.


