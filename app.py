# scratch.py
from bashplotlib.scatterplot import plot_scatter
from bashplotlib.histogram import plot_hist

x_coords = [0,20,30, 5]
y_coords = [-10,20,30, 0]
width = 20
char = 'x'
color = 'default'
title = 'My Test Graph'

print(plot_scatter(
    None,
    x_coords,
    y_coords,
    width,
    char,
    color,
    title))
plot_hist(x_coords, 20.0, None, None, "o", "default", title, None, True, False)