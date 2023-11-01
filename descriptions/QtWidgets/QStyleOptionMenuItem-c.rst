.. sip:class-description::
    :status: todo
    :brief: Used to describe the parameter necessary for drawing a menu item
    :digest: 1df515ac814de4008d90f4c2b6276f13

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionMenuItem` class is used to describe the parameter necessary for drawing a menu item.

:sip:ref:`~PyQt6.QtWidgets.QStyleOptionMenuItem` contains all the information that :sip:ref:`~PyQt6.QtWidgets.QStyle` functions need to draw the menu items from :sip:ref:`~PyQt6.QtWidgets.QMenu`. It is also used for drawing other menu-related widgets.

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`.
