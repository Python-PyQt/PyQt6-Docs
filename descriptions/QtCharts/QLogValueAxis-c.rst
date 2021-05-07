.. sip:class-description::
    :status: todo
    :brief: Adds a logarithmic scale to a chart's axis
    :digest: bf35e1b68e1773f8463b353663641377

The :sip:ref:`~PyQt6.QtCharts.QLogValueAxis` class adds a logarithmic scale to a chart's axis.

A logarithmic scale is a nonlinear scale that is based on orders of magnitude, so that each tick mark on the axis is the previous tick mark multiplied by a value.

**Note:** If :sip:ref:`~PyQt6.QtCharts.QLogValueAxis` is attached to a series with one or more points with negative or zero values on the associated dimension, the series will not be plotted at all. This is particularly relevant when XYModelMappers are used, since empty cells in models typically contain zero values.
