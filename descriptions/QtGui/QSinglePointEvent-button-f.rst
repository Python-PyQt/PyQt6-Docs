.. sip:method-description::
    :status: todo
    :pysig: 0222541eefb25af4386c5601c68ff978
    :realsig: () const
    :digest: 5565795dbe8bd5c0493b8e665b7f97b2

Returns the button that caused the event.

The returned value is always :sip:ref:`~PyQt6.QtCore.Qt.MouseButtons.NoButton` for mouse move events, as well as :sip:ref:`~PyQt6.QtCore.QEvent.Type.TabletMove`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.TabletEnterProximity`, and :sip:ref:`~PyQt6.QtCore.QEvent.Type.TabletLeaveProximity` events.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSinglePointEvent.buttons`.
