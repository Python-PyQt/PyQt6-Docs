.. sip:class-description::
    :status: todo
    :brief: Describes the parameters for drawing a group box
    :digest: 0442ad0c3776d75a619a5f9ace378f0a

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionGroupBox` class describes the parameters for drawing a group box.

:sip:ref:`~PyQt6.QtWidgets.QStyleOptionButton` contains all the information that :sip:ref:`~PyQt6.QtWidgets.QStyle` functions need the various graphical elements of a group box.

It holds the lineWidth and the midLineWidth for drawing the panel, the group box's title and the title's alignment and color.

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

For an example demonstrating how style options can be used, see the `Styles <https://doc.qt.io/qt-6/qtwidgets-widgets-styles-example.html>`_ example.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`, :sip:ref:`~PyQt6.QtWidgets.QStyleOptionComplex`, :sip:ref:`~PyQt6.QtWidgets.QGroupBox`.
