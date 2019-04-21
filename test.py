from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def plot3D(function, X, Y, color = 1):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    X, Y = np.meshgrid(X, Y)
    Z = np.array(list(map(function, X, Y)))

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

    ax.set_xlabel("Not Latency")
    ax.set_ylabel("Net Bandwidth")
    ax.set_zlabel("Accuracy")

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

def plot_fig_3(bitrate_1_accuracy, bitrate_2_accuracy, bitrate_3_accuracy):
    # https://www.jianshu.com/p/3170304baf55
    n_groups = 3

    # means_men = bitrate_1_accuracy
    # # std_men = (2, 3, 4, 1, 2)
    #
    # means_women = (25, 32, 34, 20, 25)
    # std_women = (3, 5, 2, 3, 3)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.3

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = ax.bar(index, bitrate_1_accuracy, bar_width,
                    alpha=opacity, color='b',
                    # yerr=std_men, error_kw=error_config,
                    label='bitrate 1')

    rects2 = ax.bar(index + bar_width, bitrate_2_accuracy, bar_width,
                    alpha=opacity, color='r',
                    # yerr=std_women, error_kw=error_config,
                    label='bitrate 2')

    rects3 = ax.bar(index + 2 * bar_width, bitrate_3_accuracy, bar_width,
                    alpha=opacity, color='g',
                    # yerr=std_women, error_kw=error_config,
                    label='bitrate 3')

    ax.set_xlabel('resolution')
    ax.set_ylabel('accuracy')
    ax.set_title('Accuracy of ')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(('resolution 1', 'resolution 2', 'resolution 3'))
    ax.legend()

    fig.tight_layout()
    plt.show()

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

def plot_fig_8():
    # List to hold x values.
    x_number_values = [1, 2, 3, 4, 5]

    # List to hold y values.
    y_number_values = [1, 4, 9, 16, 25]

    # Plot the number in the list and set the line thickness.
    plt.plot(x_number_values, y_number_values, linewidth=3)

    # Set the line chart title and the text font size.
    plt.title("accuracy", fontsize=19)

    # Set x axes label.
    plt.xlabel("times", fontsize=10)

    # Set y axes label.
    plt.ylabel("Square of Number", fontsize=10)

    # Set the x, y axis tick marks text size.
    plt.tick_params(axis='both', labelsize=9)

    # Display the plot in the matplotlib's viewer.
    plt.show()




if __name__ == "__main__":
    # X = range(-100,100)
    # Y = range(-100, 100)
    # f = lambda x, y: (x**2 + y**2)/10000
    # plot3D(f, X, Y, 7)
    plot_fig_8()
