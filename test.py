from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from communication.main import *
import math

def plot3D(function, X, Y, color = 1):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    X, Y = np.meshgrid(X, Y)
    # print("!%%###",X.shape)
    Z = []
    for x_idx in range(X.shape[0]):
            # print("!!!",x_line.shape, y_line.shape)
            # print(len(x_line),len(y_line))
            # print("@@@",np.array(list(map(function, x_line, y_line))))
        # print("!")
        next_line = list(map(lambda x, y: function(x,y)[1], X[x_idx,:], Y[x_idx,:]))
        Z.append(next_line)
    # print(Z)
    Z = np.array(Z)
    # print(Z.shape)

    # Plot the surface.
    color_list = [
        'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
        'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
    surf = ax.plot_surface(X, Y, Z, cmap=color_list[color],
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    # ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    ax.set_xlabel("Net Latency")
    ax.set_ylabel("Net Bandwidth")
    ax.set_zlabel("Accuracy")

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

# def _plot_fig1():
#

# def plot_fig_3(bitrate_1_accuracy = None , bitrate_2_accuracy = None, bitrate_3_accuracy = None):
#     # https://www.jianshu.com/p/3170304baf55
#     bitrate_1 = 123
#     bitrate_2 = 234
#     bitrate_3 = 345
#
#     model_1
#
#
#     bitrate_1_accuracy = map(lambda decision, )
#
#     n_groups = 3
#
#     # means_men = bitrate_1_accuracy
#     # # std_men = (2, 3, 4, 1, 2)
#     #
#     # means_women = (25, 32, 34, 20, 25)
#     # std_women = (3, 5, 2, 3, 3)
#
#     fig, ax = plt.subplots()
#
#     index = np.arange(n_groups)
#     bar_width = 0.3
#
#     opacity = 0.4
#     error_config = {'ecolor': '0.3'}
#
#     rects1 = ax.bar(index, bitrate_1_accuracy, bar_width,
#                     alpha=opacity, color='b',
#                     # yerr=std_men, error_kw=error_config,
#                     label='bitrate 1')
#
#     rects2 = ax.bar(index + bar_width, bitrate_2_accuracy, bar_width,
#                     alpha=opacity, color='r',
#                     # yerr=std_women, error_kw=error_config,
#                     label='bitrate 2')
#
#     rects3 = ax.bar(index + 2 * bar_width, bitrate_3_accuracy, bar_width,
#                     alpha=opacity, color='g',
#                     # yerr=std_women, error_kw=error_config,
#                     label='bitrate 3')
#
#     ax.set_xlabel('resolution')
#     ax.set_ylabel('accuracy')
#     ax.set_title('Accuracy of ')
#     ax.set_xticks(index + bar_width / 2)
#     ax.set_xticklabels(('resolution 1', 'resolution 2', 'resolution 3'))
#     ax.legend()
#
#     fig.tight_layout()
#     plt.show()

def plot_fig_4(bandwidth_accuracy):
    n_groups = len(bandwidth_accuracy)
    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.3
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = ax.bar(index, bandwidth_accuracy, bar_width,
                    alpha=opacity, color='b',
                    # yerr=std_men, error_kw=error_config,
                    label='bitrate 1')

    ax.set_xlabel('resolution')
    ax.set_ylabel('accuracy')
    ax.set_title('Accuracy of ')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(('resolution 1', 'resolution 2', 'resolution 3'))
    ax.legend()

    fig.tight_layout()
    plt.show()

def plot_fig_7(energy_target, resolution):
    # fig, ax = plt.subplots()
    #
    # ax.set_xlabel('resolution')
    # ax.set_ylabel('accuracy')
    # ax.set_title('Accuracy of ')
    # ax.set_xticks(index + bar_width / 2)
    # ax.set_xticklabels(('resolution 1', 'resolution 2', 'resolution 3'))
    # ax.legend()
    #
    # fig.tight_layout()
    plt.plot(energy_target, resolution, "*")
    plt.xlabel("energy target")
    plt.ylabel("resolution")
    plt.ylim(bottom = 10, top = 20)
    plt.show()

def plot_fig_1_1():
    fig, ax = plt.subplots()
    ## fig1 in our document

    # List to hold x values.
    x_number_values = [ 2 ** _ for _ in range(200)]

    # List to hold y values.
    y_number_values = [0] * 200

    z_our = list(map(lambda x,y: decision(n_face_interval = y,speed = x)[1], x_number_values, y_number_values))
    z_remote = list(map(lambda x,y: decision(n_face_interval = y,speed = x, model_range=[n_remote,n_model_all])[1], x_number_values, y_number_values))
    z_local = list(map(lambda x,y: decision(n_face_interval = y,speed = x, model_range=[0,n_remote])[1], x_number_values, y_number_values))

    # Plot the number in the list and set the line thickness.
    ax.plot(list(range(200)), z_our, linewidth=0.8)
    ax.plot(list(range(200)), z_remote, linewidth=0.8)
    ax.plot(list(range(200)), z_local, linewidth=0.8)

    # Set the line chart title and the text font size.
    # plt.title("accuracy", fontsize=19)

    # Set x axes label.
    ax.set_xlabel("log2 bandwidth", fontsize=10)

    # Set y axes label.
    ax.set_ylabel("accuracy", fontsize=10)

    # Set the x, y axis tick marks text size.
    ax.tick_params(axis='both', labelsize=9)

    # ax.set_xticklabels(("our",))


    # Display the plot in the matplotlib's viewer.
    plt.show()

# def f(x,y):
#     print("x and y: {} and {}".format(x,y))
#     return (x**2 + y**2)/10000


def plot_fig_2():
    '''
    fig2 in our work
    :return:
    '''
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = [1, 2, 8, 64, 256, 512, 1024, 2048, 4096, 8192]
    Y = [1, 2, 8, 64, 256, 512, 1024, 2048, 4096, 8192]
    # Make data.
    X, Y = np.meshgrid(X, Y)
    # print("!%%###",X.shape)
    Z = np.zeros(X.shape)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            # print("!!!",x_line.shape, y_line.shape)
            # print(len(x_line),len(y_line))
            # print("@@@",np.array(list(map(function, x_line, y_line))))
        # print("!")
            Z[i,j] = fig2(X[i,j],Y[i,j])[0]
    # print(Z)
    # Z = np.array(Z)
    print(Z)
    # print(Z.shape)

    # Plot the surface.
    color_list = [
        'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
        'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
    surf = ax.plot_surface(X, Y, Z, cmap=color_list[0],
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    # ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    ax.set_xlabel("cpu limitation")
    ax.set_ylabel("gpu limitation")
    ax.set_zlabel("Accuracy")

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

def plot_fig_3():
    fig, ax = plt.subplots()
    ## fig1 in our document

    # List to hold w values.
    w_number_values = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]


    z = list(map(fig3, w_number_values))
    # print(z)
    z = list(zip(*z))
    # print(z)

    # Plot the number in the list and set the line thickness.
    ax.plot(w_number_values, z[0], linewidth=0.7)
    ax.plot(w_number_values, z[1], linewidth=0.7)

    # Set the line chart title and the text font size.
    # plt.title("accuracy", fontsize=19)

    # Set x axes label.
    ax.set_xlabel("weight", fontsize=10)

    # Set y axes label.
    ax.set_ylabel("accuracy/latency", fontsize=10)

    # Set the x, y axis tick marks text size.
    ax.tick_params(axis='both', labelsize=9)

    # ax.set_xticklabels(("our",))


    # Display the plot in the matplotlib's viewer.
    plt.show()

def plot_fig_4():


    n_groups = 3

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.3

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    face_range = list(map(fig4, [0, 1, 2]))

    rects1 = ax.bar(index + 0.5 * bar_width, face_range, bar_width,
                    alpha=opacity, color='b')

    ax.set_xlabel('face number range')
    ax.set_ylabel('accuracy')
    ax.set_title('Fance number and Accuracy')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(('no limit', '1-9', '>10'))
    ax.legend()

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    # X = range(2,100)
    # Y = range(2, 100)
    # # f = lambda x, y: (x**2 + y**2)
    # plot3D(decision, X, Y, 7)
    plot_fig_1_1()
    # plot_fig_1_1()
    # for x in range(1,1,5000):
    #     for
    # print(fig2(500,500))
