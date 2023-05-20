from random import choice
from math import log, sqrt
import numpy as np


def generate_random_steps(length):
    x_seq = np.random.choice([-1,1],length)
    x_seq[0] = 0 
    y_seq = np.random.choice([-1,1],length)
    y_seq[0] = 0 
    return np.column_stack([x_seq,y_seq])
    #return  [pygame.Vector2(x,y) for x,y in zip(x_seq,y_seq)]

def generate_path(seq):
    return np.cumsum(seq, axis = 0)

def partial_sums(original_sequence):
    cur = 0
    for value in original_sequence:
        yield cur
        cur += value

theorem_function_map = {
        'no': lambda _: 1, 
        'slln': lambda n: 1 /n,
        'clt': lambda n: 1 / np.sqrt(n),
        # 'il': lambda n:  1 if (n <= 16) else sqrt(2* n * log(log(n))) 
        'il': lambda n:  1 / ( np.sqrt(2* (n+16) * np.log(np.log(n+16)))) 
        }

theorem_label_map = {
        'no':  r"$S_n(\omega)$", 
        'slln':r"$S_n(\omega)/n$", 
        'clt': r"$S_n(\omega)/\sqrt{n}$", 
        'il':  r"$S_n(\omega)/\sqrt{2n\log\log n}$"
        }

def scale(seq, scale):
    return [(x[0] * a, x[1] * a) for x,a in zip(seq,scale)]

def generate_scaled_path(lower, upper):
    assert lower > 1
    ran = np.arange(lower,upper)
    path = generate_path(generate_random_steps(upper))
    print("generated path")
    f = theorem_function_map["no"]
    #divisor = np.frompyfunc(lambda n: f(n+1), 1, 1)(np.arange(1,len(ran)+1))
    divisor =  f(ran)
    print("generated scaling")
    scaled_path_x = path[lower:, 0] * divisor
    scaled_path_y = path[lower:, 1] * divisor
    print("scaled path")
    return np.column_stack([scaled_path_x, scaled_path_y])

def scaled_path_on_range(lower, upper, path, theorem):
    f = theorem_function_map[theorem]
    divisor =  f(np.arange(lower+1,upper+1))
    #print("generated scaling")
    scaled_path_x = path[lower:upper, 0] * divisor
    scaled_path_y = path[lower:upper, 1] * divisor
    #print("scaled path")
    return np.column_stack([scaled_path_x, scaled_path_y])

import matplotlib.pyplot as plt
from matplotlib import colormaps
import matplotlib.colors

def two_dim_plot_one(bounds, theorem, ax, colors, circle_color):
    path = generate_path(generate_random_steps(bounds[-1][1]))
    ax.set_aspect('equal')
    ax.set_adjustable('box')
    #print("generated path")
    for bound, color in zip(bounds, colors):
        s_path = scaled_path_on_range(bound[0], bound[1], path, theorem)
        ax.plot(s_path[:, 0],s_path[:, 1], "-", c = color)

    plt.rcParams['font.size'] = 14

    ax.add_patch(plt.Circle((0, 0), 1, fill=False, color=circle_color))
    # plt.text(-.8, .8, r"$\partial B_\sigma(0)$", ha='center', va='center', color=circle_color)

    #g Create the legend
    ax.set_xlabel(r"$\sigma$", fontsize=14)
    ax.set_ylabel(r"$\sigma$", rotation = 0, fontsize=14)
    ax.set_title(theorem_label_map[theorem])

theorems = ["no", "slln", "clt", "il"]

def multiplot_2d(bounds):
    colors = colormaps["viridis"](np.linspace(0.0,1.0,len(bounds)))
    circle_color = "crimson"
    fig, axs = plt.subplots(2,2)
    for ax, theorem in zip(axs.flatten(), theorems):
        two_dim_plot_one(bounds, theorem, ax, colors, circle_color)
    legend_elements = [
            plt.Line2D([], [], marker='s', color=colors[0], label=f"{bounds[0][0]}", linestyle='None'),
            plt.Line2D([], [], marker='s', color=colors[-1], label=f"{bounds[-1][1]}", linestyle='None'),
            plt.Line2D([], [], marker='s', color=circle_color, label=r"$\partial B_\sigma(0)$", linestyle='None')
            ]

    fig.legend(handles = legend_elements, loc="center", ncol=4)
    fig.tight_layout()
    plt.show()


def two_dim_plot():
    PATH_COUNT = 2
    LOWER_BOUND = 1_000_000
    UPPER_BOUND = 100_000_000

    fig, ax = plt.subplots()
    for bound in range(PATH_COUNT):
        path = generate_scaled_path(LOWER_BOUND, UPPER_BOUND)
        ax.plot(path[:, 0],path[:, 1], "-")
    ax.add_patch(plt.Circle((0, 0), 1, fill=False), label=r"S^1")
    plt.show()

        
def one_dim_plot():
    #LENGTH = 50_000_000
    #LENGTH = 5_000_000
    LENGTH = 100
    path = generate_scaled_path(1,LENGTH)
    plt.plot(np.arange(len(path)), path[:,0])
    # plt.plot(np.arange(len(path)), path[:,1])
    plt.xlabel(r"$n$")
    plt.ylabel(r"$S_n(\omega)$")

def single_two_dim_plot():
    stepsize = 1_000_000
    stepsize = 100
    bounds = [(i * stepsize , (i+1) * stepsize + 1) for i in range(1000)]
    multiplot_2d(bounds)

def cut_two_dim_plot():
    theorem = "no"
    stepsize = 1_000_000
    gapsize = 1_000
    bounds = [(i * stepsize, i * stepsize + gapsize) for i in range(2, 400)]
    two_dim_plot_one(bounds, theorem)

def main():
    single_two_dim_plot()


if __name__=="__main__":
    main()
