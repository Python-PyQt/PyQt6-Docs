.. sip:class-description::
    :status: todo
    :brief: Used to describe the parameters for drawing a toolbar
    :digest: 2cecd0f1c3990d3670ab6ccc4a7fed65

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionToolBar` class is used to describe the parameters for drawing a toolbar.

:sip:ref:`~PyQt6.QtWidgets.QStyleOptionToolBar` contains all the information that :sip:ref:`~PyQt6.QtWidgets.QStyle` functions need to draw :sip:ref:`~PyQt6.QtWidgets.QToolBar`.

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionToolBar` class holds the lineWidth and the midLineWidth for drawing the widget. It also stores information about which area the toolbar should be located in, whether it is movable or not, which position the toolbar line should have (positionOfLine), and the toolbar's position within the line (positionWithinLine).

In addition, the class provides a couple of enums: The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionToolBar.ToolBarFeatures.ToolBarFeature` enum is used to describe whether a toolbar is movable or not, and the :sip:ref:`~PyQt6.QtWidgets.QStyleOptionToolBar.ToolBarPosition.ToolBarPosition` enum is used to describe the position of a toolbar line, as well as the toolbar's position within the line.

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

For an example demonstrating how style options can be used, see the `Styles <https://doc.qt.io/qt-6/qtwidgets-widgets-styles-example.html>`_ example.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`.
