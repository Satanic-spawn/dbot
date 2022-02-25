import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential




def predd2(crp, cur):

    crypto_curr = crp
    curr = cur

    start = dt.datetime(2016,1,1)
    end = dt.datetime.now()

    data = web.DataReader(f'{crypto_curr}-{curr}', 'yahoo', start, end)

    #Prepare data squeeze in -1 -- 0 -- 1
    print(data.head())

    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))

    pred_days = 90

    x_train, y_train = [], []

    for x in range(pred_days, len(scaled_data)):
        x_train.append(scaled_data[x-pred_days:x, 0])
        y_train.append(scaled_data[x, 0])


    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    #NN
    #numpy == 1.19.5
    #model =
    model = Sequential()

    model.add(LSTM(units = 50, return_sequences = True, input_shape = (x_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units = 50, return_sequences = True))
    model.add(Dropout(0.2))
    model.add(LSTM(units = 50))
    model.add(Dropout(0.2))
    model.add(Dense(units = 1))

    model.compile(optimizer = 'adam', loss = 'mean_squared_error')
    #model.fit(x_train, y_train, epochs = 50, batch_size = 32)
    #model.fit(x_train, y_train, epochs = 25, batch_size = 32)
    model.fit(x_train, y_train, epochs = 2, batch_size = 32)



    #Testing model


    test_s = dt.datetime(2020,1,1)
    test_e = dt.datetime.now()

    test_data = web.DataReader(f'{crypto_curr}-{curr}', 'yahoo', test_s, test_e)
    act_prices = test_data['Close'].values

    total_dataset = pd.concat((data['Close'], test_data['Close']), axis = 0)

    model_inputs = total_dataset[len(total_dataset) - len(test_data) - pred_days:].values
    model_inputs = model_inputs.reshape(-1, 1)
    model_inputs = scaler.fit_transform(model_inputs)

    x_test = []

    for x in range(pred_days, len(model_inputs)):
        x_test.append(model_inputs[x-pred_days:x, 0])

    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))


    pred_prices = model.predict(x_test)
    pred_prices = scaler.inverse_transform(pred_prices)

    plt.plot(act_prices, color = 'black', label = 'Actual prices')
    plt.plot(pred_prices, color = 'green', label = 'Pred prices')
    plt.title(f'adfssadf')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend(loc = 'upper left')
    plt.show()
    input1 = input()
    if input1 == "y":
        model.save('dbot/moddel')












#predd2("RVN", "INR")
