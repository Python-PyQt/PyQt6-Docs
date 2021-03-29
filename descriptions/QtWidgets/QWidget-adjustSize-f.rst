.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 4d34d034658958ec41e4f56abd7bf1fc

Adjusts the size of the widget to fit its contents.

This function uses :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint` if it is valid, i.e., the size hint's width and height are >= 0. Otherwise, it sets the size to the children rectangle that covers all child widgets (the union of all child widget rectangles).

For windows, the screen size is also taken into account. If the :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint` is less than (200, 100) and the size policy is :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.Policy.Expanding`, the window will be at least (200, 100). The maximum size of a window is 2/3 of the screen's width and height.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint`, :sip:ref:`~PyQt6.QtWidgets.QWidget.childrenRect`.
