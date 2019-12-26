### Description of Part-03

In the third part of the project we will create an API for predictive analysis of customer sent data, to make this API available we will create a docker container (https://docs.docker.com/).

Practical example:

- Through a browser, the client passes information to the API and receives a prediction response that was made by the algorithm: ACTIVE status or CANCELED status (the value of this result tells the prediction of which group it belongs to).

- Algorithm analysis will use a CSV file with the test base to return the result.

- Insert CSV your file into "Etapa-03/data" directory


### IMPORTANT

- The columns of the SCV file in the data directory must be separated by "," (comma).
Example: (column1, column2, column3, column4 ...)

- The STATUS column has been modified to integers and is as follows:

ATIVO = 0

CANCELADO = 1


### Creating the Project Framework with Docker:

With Docker properly installed, inside the Etapa-03 directory execute the commands:

	docker build -t previsao .

After the above command completes run

	docker run -p 9999:9999 previsao


#### Training the model

To train our model, we go to the URL:

	http://localhost:9999/train

Note: In this step we can use a browser of your choice.

#### Wipe model

To clear the template we use the URL:

	http://localhost:9999/wipe

Note: In this step we can use a browser of your choice.

#### Making predictions

To make predictions we will need a Client API to perform prediction testing. In this case we use Postman (https://www.getpostman.com/product/api-client).

At this stage we will send POST data to the API in the container and receive our forecast. We will use the URL:

	http://localhost:9999/predict

Standard for data submission:

	[
    {"qtde_em_aberto": 80, "qtde_em_dia": 0, "qtde_em_atraso": 0, "qtde_frequencia_ano":0},
    {"qtde_em_aberto": 20, "qtde_em_dia": 0, "qtde_em_atraso": 15, "qtde_frequencia_ano":0},
    {"qtde_em_aberto": 30, "qtde_em_dia": 4, "qtde_em_atraso": 6, "qtde_frequencia_ano":10},
    {"qtde_em_aberto": 0, "qtde_em_dia": 24, "qtde_em_atraso": 0, "qtde_frequencia_ano":40}
]

Forecast Return (Each row below is the same as the row above):

	{
    "Previsão": [
        1,
        0,
        0,
        0
    ]
}

In the example above we sent 4 forecasts and only one of them is in the risk area for dropout. Number 1 means status = CANCELADO.


### Closing the container

Write down the container_id with the command below:

	docker ps  

Put the container_id in the command below

	docker rm container_id -f


Created by Ueslei JF da Silva

