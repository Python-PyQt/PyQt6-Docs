.. sip:class-description::
    :status: todo
    :brief: Used to describe the parameters necessary for drawing a spin box
    :digest: 354e7acae9f8cfaabb74a3fb291aaa14

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionSpinBox` class is used to describe the parameters necessary for drawing a spin box.

:sip:ref:`~PyQt6.QtWidgets.QStyleOptionSpinBox` contains all the information that :sip:ref:`~PyQt6.QtWidgets.QStyle` functions need to draw :sip:ref:`~PyQt6.QtWidgets.QSpinBox` and :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit`.

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

For an example demonstrating how style options can be used, see the `Styles <https://doc.qt.io/qt-6/qtwidgets-widgets-styles-example.html>`_ example.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`, :sip:ref:`~PyQt6.QtWidgets.QStyleOptionComplex`.
