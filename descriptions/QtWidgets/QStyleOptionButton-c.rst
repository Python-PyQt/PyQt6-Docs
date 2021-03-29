.. sip:class-description::
    :status: todo
    :brief: Used to describe the parameters for drawing buttons
    :digest: 25355001b44415c064289b3c30323071

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionButton` class is used to describe the parameters for drawing buttons.

:sip:ref:`~PyQt6.QtWidgets.QStyleOptionButton` contains all the information that :sip:ref:`~PyQt6.QtWidgets.QStyle` functions need to draw graphical elements like :sip:ref:`~PyQt6.QtWidgets.QPushButton`, :sip:ref:`~PyQt6.QtWidgets.QCheckBox`, and :sip:ref:`~PyQt6.QtWidgets.QRadioButton`.

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

For an example demonstrating how style options can be used, see the `Styles <https://doc.qt.io/qt-6/qtwidgets-widgets-styles-example.html>`_ example.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`, :sip:ref:`~PyQt6.QtWidgets.QStyleOptionToolButton`.
