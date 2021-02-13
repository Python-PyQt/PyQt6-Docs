.. sip:class-description::
    :status: todo
    :brief: Default model/view implementation of a table view
    :digest: b199e70d3ab9307567842627a112b466

The :sip:ref:`~PyQt6.QtWidgets.QTableView` class provides a default model/view implementation of a table view.

.. image:: ../../../images/windows-tableview.png

A :sip:ref:`~PyQt6.QtWidgets.QTableView` implements a table view that displays items from a model. This class is used to provide standard tables that were previously provided by the QTable class, but using the more flexible approach provided by Qt's model/view architecture.

The :sip:ref:`~PyQt6.QtWidgets.QTableView` class is one of the `Model/View Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-view-classes>`_ and is part of Qt's `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_.

:sip:ref:`~PyQt6.QtWidgets.QTableView` implements the interfaces defined by the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` class to allow it to display data provided by models derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class.

.. _qtableview-navigation:

Navigation
----------

You can navigate the cells in the table by clicking on a cell with the mouse, or by using the arrow keys. Because :sip:ref:`~PyQt6.QtWidgets.QTableView` enables :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.tabKeyNavigation` by default, you can also hit Tab and Backtab to move from cell to cell.

.. _qtableview-visual-appearance:

Visual Appearance
-----------------

The table has a vertical header that can be obtained using the :sip:ref:`~PyQt6.QtWidgets.QTableView.verticalHeader` function, and a horizontal header that is available through the :sip:ref:`~PyQt6.QtWidgets.QTableView.horizontalHeader` function. The height of each row in the table can be found by using :sip:ref:`~PyQt6.QtWidgets.QTableView.rowHeight`; similarly, the width of columns can be found using :sip:ref:`~PyQt6.QtWidgets.QTableView.columnWidth`. Since both of these are plain widgets, you can hide either of them using their hide() functions.

Rows and columns can be hidden and shown with :sip:ref:`~PyQt6.QtWidgets.QTableView.hideRow`, :sip:ref:`~PyQt6.QtWidgets.QTableView.hideColumn`, :sip:ref:`~PyQt6.QtWidgets.QTableView.showRow`, and :sip:ref:`~PyQt6.QtWidgets.QTableView.showColumn`. They can be selected with :sip:ref:`~PyQt6.QtWidgets.QTableView.selectRow` and :sip:ref:`~PyQt6.QtWidgets.QTableView.selectColumn`. The table will show a grid depending on the :sip:ref:`~PyQt6.QtWidgets.QTableView.showGrid` property.

The items shown in a table view, like those in the other item views, are rendered and edited using standard :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`. However, for some tasks it is sometimes useful to be able to insert widgets in a table instead. Widgets are set for particular indexes with the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setIndexWidget` function, and later retrieved with :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.indexWidget`.

+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-qtableview-resized-png| | By default, the cells in a table do not expand to fill the available space.                                                                                                                                                                                                                                                        |
|                                |                                                                                                                                                                                                                                                                                                                                    |
|                                | You can make the cells fill the available space by stretching the last header section. Access the relevant header using :sip:ref:`~PyQt6.QtWidgets.QTableView.horizontalHeader` or :sip:ref:`~PyQt6.QtWidgets.QTableView.verticalHeader` and set the header's :sip:ref:`~PyQt6.QtWidgets.QHeaderView.stretchLastSection` property. |
|                                |                                                                                                                                                                                                                                                                                                                                    |
|                                | To distribute the available space according to the space requirement of each column or row, call the view's :sip:ref:`~PyQt6.QtWidgets.QTableView.resizeColumnsToContents` or :sip:ref:`~PyQt6.QtWidgets.QTableView.resizeRowsToContents` functions.                                                                               |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _qtableview-coordinate-systems:

Coordinate Systems
------------------

For some specialized forms of tables it is useful to be able to convert between row and column indexes and widget coordinates. The :sip:ref:`~PyQt6.QtWidgets.QTableView.rowAt` function provides the y-coordinate within the view of the specified row; the row index can be used to obtain a corresponding y-coordinate with :sip:ref:`~PyQt6.QtWidgets.QTableView.rowViewportPosition`. The :sip:ref:`~PyQt6.QtWidgets.QTableView.columnAt` and :sip:ref:`~PyQt6.QtWidgets.QTableView.columnViewportPosition` functions provide the equivalent conversion operations between x-coordinates and column indexes.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTableWidget`, `View Classes <https://doc.qt.io/qt-6/model-view-programming.html#view-classes>`_, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`, `Chart Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-chart-example.html>`_, `Pixelator Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-pixelator-example.html>`_.

.. |image-qtableview-resized-png| image:: ../../../images/qtableview-resized.png
