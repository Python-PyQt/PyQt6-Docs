.. sip:class-description::
    :status: todo
    :brief: Sent when scrolling
    :digest: 9e36900a1b238e4a2be5a3c87ff7b451

The :sip:ref:`~PyQt6.QtGui.QScrollEvent` class is sent when scrolling.

The scroll event is sent to indicate that the receiver should be scrolled. Usually the receiver should be something visual like QWidget or QGraphicsObject.

Some care should be taken that no conflicting QScrollEvents are sent from two sources. Using QScroller::scrollTo is save however.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QScrollPrepareEvent`.
