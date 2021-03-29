.. sip:class-description::
    :status: todo
    :brief: Used to describe the parameters used to draw an item in a view widget
    :digest: 0acccce31702cabbed2316018e8ffc04

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem` class is used to describe the parameters used to draw an item in a view widget.

:sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem` contains all the information that :sip:ref:`~PyQt6.QtWidgets.QStyle` functions need to draw the items for Qt's model/view classes.

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

For an example demonstrating how style options can be used, see the `Styles <https://doc.qt.io/qt-6/qtwidgets-widgets-styles-example.html>`_ example.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_.
