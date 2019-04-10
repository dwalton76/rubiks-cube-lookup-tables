#!/usr/bin/env python3

"""
https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
"""

from keras.models import Sequential
from keras.layers import Dense
from tabulate import tabulate
import logging
import numpy
import sys

numpy.random.seed(7)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))



'''
$ head lookup-table-4x4x4-step10-ULFRBD-centers-stage.txt.nn
0,2,0,0,1,0,6
2,1,1,2,0,0,5
0,1,1,1,1,2,6
0,0,0,2,4,0,5
'''

INPUTS = 6
stats_filename = "lookup-table-4x4x4-step10-ULFRBD-centers-stage.txt.nn"
dataset = numpy.loadtxt(stats_filename, delimiter=",", dtype=int)

# split into input (X) and output (Y) variables
X_all = dataset[:,0:INPUTS]
Y_all = dataset[:,INPUTS]

len_dataset = len(X_all)
eighty_percent_count = int(len_dataset * .80)
X_train = X_all[:eighty_percent_count]
Y_train = Y_all[:eighty_percent_count]
X_test = X_all[eighty_percent_count:]
Y_test = Y_all[eighty_percent_count:]

print("%d train entries, %d test entries" % (len(X_train), len(X_test)))
print("Inputs\n======\n%s\n" % X_train[0:10])
print("Outputs\n=======\n%s\n" % Y_train[0:10])


HEADER = ('Hidden Layers', 'Nodes Per Layer', 'optimzer', 'epochs', 'batch_size', 'accuracy')
rows = []

#optimizers = ('adam', 'sgd')
optimizers = ('adam',)

#batch_sizes = (16, 32, 64, 128, 256, 512)
batch_sizes = (16,)

max_accuracy = 0
index = 0

test_parameters = []

for num_hidden_layers in range(1, 2):
    for num_nodes_per_layers in range(100, 300, 100):
        for optimizer in optimizers:
            for num_epochs in range(40, 70, 10):
                for batch_size in batch_sizes:
                    test_parameters.append((num_hidden_layers, num_nodes_per_layers, optimizer, num_epochs, batch_size))

len_test_parameters = len(test_parameters)

for (index, (num_hidden_layers, num_nodes_per_layers, optimizer, num_epochs, batch_size)) in enumerate(test_parameters):

    # create model
    model = Sequential()
    model.add(Dense(num_nodes_per_layers, input_dim=INPUTS, activation='relu'))

    for x in range(num_hidden_layers):
        model.add(Dense(num_nodes_per_layers, activation='relu'))

    model.add(Dense(7, activation='softmax'))

    # Compile model
    model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    # Fit the model
    model.fit(X_train, Y_train, epochs=num_epochs, batch_size=batch_size, verbose=0)

    # evaluate the model
    scores = model.evaluate(X_test, Y_test)
    accuracy = scores[1] * 100

    if accuracy > max_accuracy:
        max_accuracy = accuracy
        accuracy = "\033[92m%.2f\033[0m" % accuracy
    else:
        accuracy = "%.2f" % accuracy

    log.info("%d/%d: %d hidden layers, %d nodes per layer, %s optimizer, %d epochs, %d batch_size, %s accuracy" %
        (index, len_test_parameters, num_hidden_layers, num_nodes_per_layers, optimizer, num_epochs, batch_size, accuracy))

    rows.append((str(num_hidden_layers), str(num_nodes_per_layers), optimizer, str(num_epochs), str(batch_size), accuracy))
    #print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

print("\n\n")
print(tabulate(rows, headers=HEADER))
