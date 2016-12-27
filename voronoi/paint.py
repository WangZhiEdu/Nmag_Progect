import matplotlib
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np


def read_points(file_name='geo/Point.txt'):
    point_list = []
    with open(file_name, 'r', encoding='utf-8') as f:
        first_line = True
        for line in f:
            if first_line:
                first_line = False
                continue
            line_token = line.split(',')
            point_list.append((float(line_token[0].strip()), float(line_token[1].strip())))
    return point_list


def read_regions(file_name='geo/Region.txt'):
    region_point_list = []
    with open(file_name, 'r', encoding='utf-8') as f:
        first_line = True
        for line in f:
            if first_line:
                first_line = False
                continue
            point_list = []
            line_token = line.split('\t')
            for token in line_token:
                if token == '\n':
                    continue
                tokens = token.split(',')
                point_list.append((float(tokens[0].strip()), float(tokens[1].strip())))
            region_point_list.append(point_list)
    return region_point_list


def read_results(file_name='Result.txt', stage_index=2):
    result_list = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            line_token = line.split('\t')
            stage_value = line_token[2]
            stage_value = float(stage_value.strip())
            result_list.append(stage_value)
    return result_list

point_list = read_points()
region_list = read_regions()
result_list = read_results()
print('point_list: %d, region_list: %d, result_list: %d' % (len(point_list), len(region_list), len(result_list)))
fig = plt.figure()
ax = fig.gca()
plt.axis((-15, 15, -15, 15))
#
Greys = cm.get_cmap('Greys')
Up_color = Greys(0)
Down_color = Greys(192)
color_list = np.zeros((len(point_list), 4))
for i in range(len(point_list)):
    result = result_list[i*2]
    if result > 0:
        color_list[i] = Up_color
    else:
        color_list[i] = Down_color
# region_list
poly_coll = matplotlib.collections.PolyCollection(region_list, facecolors=color_list)
ax.add_collection(poly_coll)
# point_list
for i in range(len(point_list)):
    point = point_list[i]
    ax.text(point[0], point[1], str(i + 1), fontsize=10)
    ax.plot(point[0], point[1], 'r.')
plt.savefig('result.png')
plt.close()