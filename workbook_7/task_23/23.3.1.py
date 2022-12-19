import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.neural_network import MLPRegressor

url = 'https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv'
digits = pd.read_csv(url, sep=',')
boston = pd.read_csv(url, sep=',')

X_digits, Y_digits = digits.YearsExperience, digits.Salary
print('Dataset sizes:', X_digits.shape, Y_digits.shape, '\n')

X_boston, Y_boston = boston.YearsExperience, boston.Salary
print('Dataset sizes: ', X_boston.shape, Y_boston.shape, '\n')

X_train, X_test, Y_train, Y_test = train_test_split(X_digits,
                                                    Y_digits,
                                                    train_size=0.80,
                                                    test_size=0.20,
                                                    stratify=Y_digits,
                                                    random_state=123)

print('Train/Test sizes : ', X_train.shape, X_test.shape,
      Y_train.shape, Y_test.shape, '\n')

mlp_classifier = MLPClassifier(random_state=123)
mlp_classifier.fit(X_train, Y_train)

MLPClassifier(activation='relu', alpha=0.0001,
              batch_size='auto', beta_1=0.9,
              beta_2=0.999, early_stopping=False,
              epsilon=1e-08, hidden_layer_sizes=(100,),
              learning_rate='constant', learning_rate_init=0.001,
              max_iter=200, momentum=0.9,
              n_iter_no_change=10, nesterovs_momentum=True,
              power_t=0.5, random_state=123,
              shuffle=True, solver='adam',
              tol=0.0001, validation_fraction=0.1,
              verbose=False, warm_start=False)

Y_preds = mlp_classifier.predict(X_test)

print(Y_preds[:151], '\n')
print(Y_test[:151], '\n')

print('Test Accuracy: %.3f' % mlp_classifier.score(X_test, Y_test), '\n')
print('Training Accuracy: %.3f' % mlp_classifier.score(X_train, Y_train), '\n')


def plot_confusion_matrix(Y_test, Y_preds):
    conf_mat = confusion_matrix(Y_test, Y_preds)
    print(conf_mat, '\n')
    fig = plt.figure(figsize=(6, 6))
    plt.matshow(conf_mat, cmap=plt.cm.Blues, fignum=1)
    plt.yticks(range(10), range(10))
    plt.xticks(range(10), range(10))
    plt.colorbar()
    for i in range(10):
        for j in range(10):
            plt.text(i - 0.2, j + 0.1, str(conf_mat[j, i]), color='tab:red')


plot_confusion_matrix(Y_test, mlp_classifier.predict(X_test))

print("Loss: ", mlp_classifier.loss_, '\n')
print("Number of Coefs: ", len(mlp_classifier.coefs_), '\n')
print("Number of Intercepts: ", len(mlp_classifier.intercepts_), '\n')
print("Number of Iterations for Which Estimator Ran: ", mlp_classifier.n_iter_, '\n')
print("Name of Output Layer Activation Function: ", mlp_classifier.out_activation_, '\n')


X_train, X_test, Y_train, Y_test = train_test_split(X_boston, Y_boston,
                                                    train_size=0.80,
                                                    test_size=0.20,
                                                    random_state=123)
print('Train/Test Sizes: ', X_train.shape, X_test.shape, Y_train.shape, Y_test.shape, '\n')

mlp_regressor = MLPRegressor(random_state=123)
mlp_regressor.fit(X_train, Y_train)

MLPRegressor(activation='relu', alpha=0.0001,
             batch_size='auto', beta_1=0.9,
             beta_2=0.999, early_stopping=False,
             epsilon=1e-08, hidden_layer_sizes=(100,),
             learning_rate='constant', learning_rate_init=0.001,
             max_iter=200, momentum=0.9,
             n_iter_no_change=10, nesterovs_momentum=True,
             power_t=0.5, random_state=123,
             shuffle=True, solver='adam', tol=0.0001,
             validation_fraction=0.1, verbose=False, warm_start=False)

Y_preds = mlp_regressor.predict(X_test)
print(Y_preds[:10], '\n')
print(Y_test[:10], '\n')

print('Test R^2 Score: %.3f' % mlp_regressor.score(X_test, Y_test), '\n')
print('Training R^2 Score: %.3f' % mlp_regressor.score(X_train, Y_train), '\n')
print("Loss: ", mlp_regressor.loss_, '\n')
print("Number of Coefs: ", len(mlp_regressor.coefs_), '\n')
print("Number of Intercepts: ", len(mlp_regressor.intercepts_), '\n')
print("Number of Iterations for Which Estimator Ran: ", mlp_regressor.n_iter_, '\n')
print("Name of Output Layer Activation Function: ", mlp_regressor.out_activation_, '\n')
