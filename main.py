from data_Parser import *
import matplotlib.pyplot as plt
import pprint


data_dict = main_run('Feb_19_7am.csv')
def main():
    xvalues = list(range(0, len(data_dict)))
    # teddy_yvalues = data_to_points('Teddy @ B8LTKKxPBI', data_dict)
    # teddy2_yvalues = data_to_points('teddy @ kOMtSCwNxC', data_dict)
    # derek_yvalues = data_to_points('dere @ IB1rRLac0F', data_dict)
    # tyler_yvalues = data_to_points('Thler @ p2tt-yMqE3', data_dict)
    # haoyang_yvalues = data_to_points('Haoyang Zhang @ QntlFAl8Rf', data_dict)

    # plt.plot(xvalues, teddy_yvalues, label = 'teddy1')
    # plt.plot(xvalues, teddy2_yvalues, label = 'teddy2')
    # plt.plot(xvalues, derek_yvalues, label = 'derek')
    # plt.plot(xvalues, tyler_yvalues, label = 'tyler')
    # plt.plot(xvalues, haoyang_yvalues, label = 'haoyang')

    teddy_yvalues = data_to_points('teddye @ kOMtSCwNxC', data_dict)
    derek_yvalues = data_to_points('dk @ IB1rRLac0F', data_dict)

    plt.plot(xvalues, teddy_yvalues, label = "Teddy")
    plt.plot(xvalues, derek_yvalues, label = "Derek")
    plt.legend()
    plt.show()

main()

