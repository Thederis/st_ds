import re

import matplotlib.pyplot as plt


def parse_asymptote(file_path: str, dict_of_lists: dict):
    with open(file_path, "r") as f:
        contents = f.read()
    pattern = "(?<= draw figures \*\/\n).*(?= /\* end of picture)"
    matches = re.findall(pattern, contents, re.DOTALL)
    for el in matches[0].strip().split("\n"):

        # круги
        if "circle" in el:
            pattern = "(?<=circle).*?(?=, linewidth)"
            coords_radius = eval(re.findall(pattern, el)[0])
            if not "circles" in dict_of_lists:
                dict_of_lists["circles"] = [coords_radius]
            else:
                dict_of_lists["circles"].append(coords_radius)
        # линии
        if "draw((" in el and "xmin" not in el:
            pattern = "(?<=draw\().*?(?=, linewidth)"
            segment_coords = eval(re.findall(pattern, el)[0].replace("--", ","))
            if not "lines" in dict_of_lists:
                dict_of_lists["lines"] = [segment_coords]
            else:
                dict_of_lists["lines"].append(segment_coords)

    pattern = "(?<= dots and labels \*\/\n).*(?= /\* end of picture)"
    matches = re.findall(pattern, contents, re.DOTALL)
    for el in matches[0].strip().split("\n"):
        # точки
        if "dot((" in el:
            pattern = "(?<=dot\().*?(?=,dotstyle)"
            if len(re.findall(pattern, el)):
                point_coords = eval(re.findall(pattern, el)[0])
                if not "dots" in dict_of_lists:
                    dict_of_lists["dots"] = [[point_coords[0]], [point_coords[1]]]
                else:
                    dict_of_lists["dots"][0].append(point_coords[0])
                    dict_of_lists["dots"][1].append(point_coords[1])


def set_fig_ax(figsize_x=10,
               figsize_y=10,
               y_x_start_mark=-1,
               y_x_end_mark=11,
               use_quadratic_picture=True,
               x_start_mark=-1,
               x_end_mark=11,
               y_start_mark=-1,
               y_end_mark=11,
               use_y_x_marks=True,
               use_grid=True,
               use_coord_arrows=True,
               width=0.05,
               head_width=0.3,
               xlabel="x",
               ylabel="y"
               ):
    fig, ax = plt.subplots(figsize=(figsize_x, figsize_y))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.tick_params(axis='both', which='minor', labelsize=10)
    plt.style.use('fivethirtyeight')
    plt.axis('equal')
    ax.grid(use_grid)

    if use_quadratic_picture:
        ax.set_xticks(list(range(y_x_start_mark, y_x_end_mark)))
        ax.set_yticks(list(range(y_x_start_mark, y_x_end_mark)))
        ax.set_xlim(y_x_start_mark, y_x_end_mark)
        ax.set_ylim(y_x_start_mark, y_x_end_mark)
        if use_coord_arrows:
            ax.set_xlabel('x', fontsize=32)
            ax.set_ylabel('y', fontsize=32)
            shift = abs(y_x_start_mark) + y_x_end_mark
            ax.arrow(y_x_start_mark, 0, shift, 0, width=width, head_width=head_width, head_length=head_width,
                     length_includes_head=True, color="black")
            ax.arrow(0, y_x_start_mark, 0, shift, width=width, head_width=head_width, head_length=head_width,
                     length_includes_head=True, color="black")

    else:
        ax.set_xticks(list(range(x_start_mark, x_end_mark)))
        ax.set_yticks(list(range(y_start_mark, y_end_mark)))
        ax.set_xlim(x_start_mark, x_end_mark)
        ax.set_ylim(y_start_mark, y_end_mark)
        if use_coord_arrows:
            ax.set_xlabel(xlabel, fontsize=32)
            ax.set_ylabel(ylabel, fontsize=32)
            x_shift = abs(x_start_mark) + x_end_mark
            y_shift = abs(y_start_mark) + y_end_mark
            ax.arrow(x_start_mark, 0, x_shift, 0, width=width, head_width=head_width, head_length=head_width,
                     length_includes_head=True, color="black")
            ax.arrow(0, y_start_mark, 0, y_shift, width=width, head_width=head_width, head_length=head_width,
                     length_includes_head=True, color="black")

    if not use_y_x_marks:
        plt.xticks([])
        plt.yticks([])

    return fig, ax


def draw_matrix(x_0, y_0, matrix, text_shift=0, fontsize=10):
    num_col = matrix.shape[1]
    num_rows = matrix.shape[0]
    x_1 = x_0 + num_col
    y_1 = y_0 + num_rows
    list_of_lines = []
    dict_of_text = {}

    for x_i, x in enumerate(range(x_0, x_1 + 1)):
        lines = []
        for y_i, y in enumerate(range(y_0, y_1 + 1)):
            lines.append((x, y))
            if x_i < num_col and y_i < num_rows:
                text = matrix[num_rows - y_i - 1][x_i]
                dict_of_text[(x, y)] = {"x": x + text_shift,
                                        "y": y + text_shift,
                                        "s": text,
                                        "fontsize": fontsize}
        list_of_lines.append(lines)

    for y in range(y_0, y_1 + 1):
        lines = []
        for x in range(x_0, x_1 + 1):
            lines.append((x, y))
        list_of_lines.append(lines)

    return list_of_lines, dict_of_text

if __name__ == '__main__':
    dict_of_lists = {}

    parse_asymptote("../images04/logregression.txt", dict_of_lists)
    print(dict_of_lists)