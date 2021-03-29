.. sip:class-description::
    :status: todo
    :brief: Lays out widgets in a grid
    :digest: 8dab54513172e83c42620d36c8124d63

The :sip:ref:`~PyQt6.QtWidgets.QGridLayout` class lays out widgets in a grid.

:sip:ref:`~PyQt6.QtWidgets.QGridLayout` takes the space made available to it (by its parent layout or by the parentWidget()), divides it up into rows and columns, and puts each widget it manages into the correct cell.

Columns and rows behave identically; we will discuss columns, but there are equivalent functions for rows.

Each column has a minimum width and a stretch factor. The minimum width is the greatest of that set using :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setColumnMinimumWidth` and the minimum width of each widget in that column. The stretch factor is set using :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setColumnStretch` and determines how much of the available space the column will get over and above its necessary minimum.

Normally, each managed widget or layout is put into a cell of its own using :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addWidget`. It is also possible for a widget to occupy multiple cells using the row and column spanning overloads of :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addItem` and :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addWidget`. If you do this, :sip:ref:`~PyQt6.QtWidgets.QGridLayout` will guess how to distribute the size over the columns/rows (based on the stretch factors).

To remove a widget from a layout, call removeWidget(). Calling :sip:ref:`~PyQt6.QtWidgets.QWidget.hide` on a widget also effectively removes the widget from the layout until :sip:ref:`~PyQt6.QtWidgets.QWidget.show` is called.

This illustration shows a fragment of a dialog with a five-column, three-row grid (the grid is shown overlaid in magenta):

.. image:: ../../../images/qgridlayout.png

Columns 0, 2 and 4 in this dialog fragment are made up of a :sip:ref:`~PyQt6.QtWidgets.QLabel`, a :sip:ref:`~PyQt6.QtWidgets.QLineEdit`, and a QListBox. Columns 1 and 3 are placeholders made with :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setColumnMinimumWidth`. Row 0 consists of three :sip:ref:`~PyQt6.QtWidgets.QLabel` objects, row 1 of three :sip:ref:`~PyQt6.QtWidgets.QLineEdit` objects and row 2 of three QListBox objects. We used placeholder columns (1 and 3) to get the right amount of space between the columns.

Note that the columns and rows are not equally wide or tall. If you want two columns to have the same width, you must set their minimum widths and stretch factors to be the same yourself. You do this using :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setColumnMinimumWidth` and :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setColumnStretch`.

If the :sip:ref:`~PyQt6.QtWidgets.QGridLayout` is not the top-level layout (i.e. does not manage all of the widget's area and children), you must add it to its parent layout when you create it, but before you do anything with it. The normal way to add a layout is by calling :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addLayout` on the parent layout.

Once you have added your layout you can start putting widgets and other layouts into the cells of your grid layout using :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addWidget`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addItem`, and :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addLayout`.

:sip:ref:`~PyQt6.QtWidgets.QGridLayout` also includes two margin widths: the contents margin and the :sip:ref:`~PyQt6.QtWidgets.QGridLayout.spacing`. The contents margin is the width of the reserved space along each of the :sip:ref:`~PyQt6.QtWidgets.QGridLayout`'s four sides. The :sip:ref:`~PyQt6.QtWidgets.QGridLayout.spacing` is the width of the automatically allocated spacing between neighboring boxes.

The default contents margin values are provided by the :sip:ref:`~PyQt6.QtWidgets.QStyle.pixelMetric`. The default value Qt styles specify is 9 for child widgets and 11 for windows. The spacing defaults to the same as the margin width for a top-level layout, or to the same as the parent layout.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`, :sip:ref:`~PyQt6.QtWidgets.QStackedLayout`, `Layout Management <https://doc.qt.io/qt-6/layout.html>`_, `Basic Layouts Example <https://doc.qt.io/qt-6/qtwidgets-layouts-basiclayouts-example.html>`_.
