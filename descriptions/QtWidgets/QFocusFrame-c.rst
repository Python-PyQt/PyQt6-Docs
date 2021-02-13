.. sip:class-description::
    :status: todo
    :brief: Focus frame which can be outside of a widget's normal paintable area
    :digest: c6a1d8a26ce3042605c3a70d7121c2d6

The :sip:ref:`~PyQt6.QtWidgets.QFocusFrame` widget provides a focus frame which can be outside of a widget's normal paintable area.

Normally an application will not need to create its own :sip:ref:`~PyQt6.QtWidgets.QFocusFrame` as :sip:ref:`~PyQt6.QtWidgets.QStyle` will handle this detail for you. A style writer can optionally use a :sip:ref:`~PyQt6.QtWidgets.QFocusFrame` to have a focus area outside of the widget's paintable geometry. In this way space need not be reserved for the widget to have focus but only set on a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ with :sip:ref:`~PyQt6.QtWidgets.QFocusFrame.setWidget`. It is, however, legal to create your own :sip:ref:`~PyQt6.QtWidgets.QFocusFrame` on a custom widget and set its geometry manually via :sip:ref:`~PyQt6.QtWidgets.QWidget.setGeometry` however you will not get auto-placement when the focused widget changes size or placement.
