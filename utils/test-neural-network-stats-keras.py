#!/usr/bin/env python3

"""
https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
"""

# standard libraries
import copy
import logging
import sys

# third party libraries
import numpy

# rubiks cube libraries
from keras.layers import Dense
from keras.models import Sequential, load_model
from tabulate import tabulate

numpy.random.seed(7)

def get_train_vs_test_centers_stage_444():
    # The first 6 inputs (horizontal bar count, etc) do not buy us much
    INPUTS_TO_IGNORE = 6
    INPUTS = 9
    stats_filename = "lookup-table-4x4x4-step10-ULFRBD-centers-stage.txt.nn"
    dataset = numpy.loadtxt(stats_filename, delimiter=",", dtype=int)

    # split into input (X) and output (Y) variables
    X_all = dataset[:,INPUTS_TO_IGNORE:INPUTS]
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

    return (X_train, Y_train, X_test, Y_test)


def train_model_centers_stage_444():
    (X_train, Y_train, X_test, Y_test) = get_train_vs_test_centers_stage_444()
    HEADER = ('Hidden Layers', 'Nodes Per Layer', 'optimzer', 'epochs', 'batch_size', 'accuracy')
    rows = []

    #optimizers = ('adam', 'sgd')
    optimizers = ('adam',)

    #batch_sizes = (8, 16, 32, 64, 128, 256, 512)
    batch_sizes = (16,)

    max_accuracy = 0
    max_accuracy_model = None
    index = 0

    test_parameters = []

    for num_hidden_layers in range(1, 3):
        for num_nodes_per_layers in range(100, 500, 100):
            for optimizer in optimizers:
                #for num_epochs in range(40, 70, 10):
                for num_epochs in range(10, 30, 10):
                    for batch_size in batch_sizes:
                        test_parameters.append((num_hidden_layers, num_nodes_per_layers, optimizer, num_epochs, batch_size))

    len_test_parameters = len(test_parameters)

    for (index, (num_hidden_layers, num_nodes_per_layers, optimizer, num_epochs, batch_size)) in enumerate(test_parameters):

        # create model
        model = Sequential()
        model.add(Dense(num_nodes_per_layers, input_dim=(INPUTS - INPUTS_TO_IGNORE), activation='relu'))

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
            max_accuracy_model = copy.deepcopy(model)
            accuracy = "\033[92m%.2f\033[0m" % accuracy
        else:
            accuracy = "%.2f" % accuracy

        log.info("%d/%d: %d hidden layers, %d nodes per layer, %s optimizer, %d epochs, %d batch_size, %s accuracy" %
            (index, len_test_parameters, num_hidden_layers, num_nodes_per_layers, optimizer, num_epochs, batch_size, accuracy))

        rows.append((str(num_hidden_layers), str(num_nodes_per_layers), optimizer, str(num_epochs), str(batch_size), accuracy))
        #print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    print("\n\n")
    print(tabulate(rows, headers=HEADER))
    max_accuracy_model.save("centers-stage-444.h5")


def load_model_centers_stage_444():
    model = load_model("centers-stage-444.h5")
    (X_train, Y_train, X_test, Y_test) = get_train_vs_test_centers_stage_444()
    scores = model.evaluate(X_test, Y_test)
    accuracy = scores[1] * 100
    print("%.2f" % accuracy)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    train_model_centers_stage_444()
    #load_model_centers_stage_444()
