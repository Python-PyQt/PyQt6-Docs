.. sip:class-description::
    :status: todo
    :brief: Sent when scrolling
    :digest: 339814a097a3a78ae477bcf27b1ffab6

The :sip:ref:`~PyQt6.QtGui.QScrollEvent` class is sent when scrolling.

The scroll event is sent to indicate that the receiver should be scrolled. Usually the receiver should be something visual like `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ or :sip:ref:`~PyQt6.QtWidgets.QGraphicsObject`.

Some care should be taken that no conflicting QScrollEvents are sent from two sources. Using :sip:ref:`~PyQt6.QtWidgets.QScroller.scrollTo` is save however.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QScrollPrepareEvent`, :sip:ref:`~PyQt6.QtWidgets.QScroller`.
