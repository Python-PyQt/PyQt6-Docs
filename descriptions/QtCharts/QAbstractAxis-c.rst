.. sip:class-description::
    :status: todo
    :brief: Base class used for specialized axis classes
    :digest: 5f14905412fea2c33f89e652b10fff83

The :sip:ref:`~PyQt6.QtCharts.QAbstractAxis` class is a base class used for specialized axis classes.

Each series can be bound to one or more horizontal and vertical axes, but mixing axis types that would result in different domains is not supported, such as specifying :sip:ref:`~PyQt6.QtCharts.QValueAxis` and :sip:ref:`~PyQt6.QtCharts.QLogValueAxis` on the same orientation.

The properties and visibility of various axis elements, such as axis line, title, labels, grid lines, and shades, can be individually controlled.
