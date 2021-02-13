.. sip:method-description::
    :status: todo
    :pysig: 78c2ee29b9f6bed2b9f05a748c095133
    :realsig: (QEvent*)
    :digest: f9127c19a2075975c7c61d520151df3a

The main event handler for the scrolling area (the :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.viewport` widget). It handles the *event* specified, and can be called by subclasses to provide reasonable default behavior.

Returns ``true`` to indicate to the event system that the event has been handled, and needs no further processing; otherwise returns ``false`` to indicate that the event should be propagated further.

You can reimplement this function in a subclass, but we recommend using one of the specialized event handlers instead.

Specialized handlers for viewport events are: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.paintEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.mouseReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.mouseDoubleClickEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.mouseMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.wheelEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.dragEnterEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.dragMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.dragLeaveEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.dropEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.contextMenuEvent`, and :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.resizeEvent`.
