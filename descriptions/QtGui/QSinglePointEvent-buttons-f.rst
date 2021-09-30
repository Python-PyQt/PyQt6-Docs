.. sip:method-description::
    :status: todo
    :pysig: 0222541eefb25af4386c5601c68ff978
    :realsig: () const
    :digest: d797e7df60005af0419e946470f95474

Returns the button state when the event was generated.

The button state is a combination of :sip:ref:`~PyQt6.QtCore.Qt.MouseButton.LeftButton`, :sip:ref:`~PyQt6.QtCore.Qt.MouseButton.RightButton`, and :sip:ref:`~PyQt6.QtCore.Qt.MouseButton.MiddleButton` using the OR operator.

For mouse move or :sip:ref:`~PyQt6.QtCore.QEvent.Type.TabletMove` events, this is all buttons that are pressed down.

For mouse press, double click, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.TabletPress` events, this includes the button that caused the event.

For mouse release or :sip:ref:`~PyQt6.QtCore.QEvent.Type.TabletRelease` events, this excludes the button that caused the event.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSinglePointEvent.button`.
