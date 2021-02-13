.. sip:method-description::
    :status: todo
    :pysig: cf1d98f4399d47c563dcede96e2df423
    :realsig: (Qt::InputMethodQuery) const
    :digest: 0e87f80b9fdb1415f7bd90a342b91ada

This method is only relevant for input widgets. It is used by the input method to query a set of properties of the widget to be able to support complex input method operations as support for surrounding text and reconversions.

*query* specifies which property is queried.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.inputMethodEvent`, :sip:ref:`~PyQt6.QtGui.QInputMethodEvent`, :sip:ref:`~PyQt6.QtGui.QInputMethodQueryEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.inputMethodHints`.
