.. sip:class-description::
    :status: todo
    :brief: Used to describe the parameter necessary for drawing a menu item
    :digest: 89335df437446e8f3c6290445c794edd

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionMenuItem` class is used to describe the parameter necessary for drawing a menu item.

:sip:ref:`~PyQt6.QtWidgets.QStyleOptionMenuItem` contains all the information that :sip:ref:`~PyQt6.QtWidgets.QStyle` functions need to draw the menu items from :sip:ref:`~PyQt6.QtWidgets.QMenu`. It is also used for drawing other menu-related widgets.

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

For an example demonstrating how style options can be used, see the `Styles <https://doc.qt.io/qt-6/qtwidgets-widgets-styles-example.html>`_ example.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`.
