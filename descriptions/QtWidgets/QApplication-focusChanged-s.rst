.. sip:signal-description::
    :status: todo
    :pysig: c461e79d01c58a5933768e435af5285d
    :realsig: (QWidget*,QWidget*)
    :digest: 6013a8789ddeb70c74a5addfd5d5eb23

This signal is emitted when the widget that has keyboard focus changed from *old* to *now*, i.e., because the user pressed the tab-key, clicked into a widget or changed the active window. Both *old* and *now* can be ``nullptr``.

The signal is emitted after both widget have been notified about the change through :sip:ref:`~PyQt6.QtGui.QFocusEvent`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocus`, :sip:ref:`~PyQt6.QtWidgets.QWidget.clearFocus`, :sip:ref:`~PyQt6.QtCore.Qt.FocusReason`.
