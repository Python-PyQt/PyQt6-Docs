.. sip:method-description::
    :status: todo
    :pysig: 54325e9368999a85b6b186618ee81876
    :realsig: () const
    :digest: 3a59645b7815d28b355345c420165d0f

Returns the button state when the event was generated.

The button state is a combination of :sip:ref:`~PyQt6.QtCore.Qt.MouseButton.LeftButton`, :sip:ref:`~PyQt6.QtCore.Qt.MouseButton.RightButton`, and Qt::MidButton using the OR operator.

For mouse move or :sip:ref:`~PyQt6.QtCore.QEvent.Type.TabletMove` events, this is all buttons that are pressed down.

For mouse press, double click, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.TabletPress` events, this includes the button that caused the event.

For mouse release or :sip:ref:`~PyQt6.QtCore.QEvent.Type.TabletRelease` events, this excludes the button that caused the event.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSinglePointEvent.button`.
