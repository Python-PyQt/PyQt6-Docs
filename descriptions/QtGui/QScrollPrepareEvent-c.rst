.. sip:class-description::
    :status: todo
    :brief: Sent in preparation of scrolling
    :digest: 4fff414048171569d2ec7565c5beeaf8

The :sip:ref:`~PyQt6.QtGui.QScrollPrepareEvent` class is sent in preparation of scrolling.

The scroll prepare event is sent before scrolling (usually by :sip:ref:`~PyQt6.QtWidgets.QScroller`) is started. The object receiving this event should set :sip:ref:`~PyQt6.QtGui.QScrollPrepareEvent.viewportSize`, maxContentPos and :sip:ref:`~PyQt6.QtGui.QScrollPrepareEvent.contentPos`. It also should accept this event to indicate that scrolling should be started.

It is not guaranteed that a :sip:ref:`~PyQt6.QtGui.QScrollEvent` will be sent after an accepted :sip:ref:`~PyQt6.QtGui.QScrollPrepareEvent`, e.g. in a case where the maximum content position is (0, 0).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QScrollEvent`, :sip:ref:`~PyQt6.QtWidgets.QScroller`.
