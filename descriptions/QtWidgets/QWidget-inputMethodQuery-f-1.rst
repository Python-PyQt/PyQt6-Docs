.. sip:method-description::
    :status: todo
    :pysig: 22b190e0cc06856e372faf7011c0a854
    :realsig: (Qt::InputMethodQuery) const
    :digest: 0e87f80b9fdb1415f7bd90a342b91ada

This method is only relevant for input widgets. It is used by the input method to query a set of properties of the widget to be able to support complex input method operations as support for surrounding text and reconversions.

*query* specifies which property is queried.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.inputMethodEvent`, :sip:ref:`~PyQt6.QtGui.QInputMethodEvent`, :sip:ref:`~PyQt6.QtGui.QInputMethodQueryEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.inputMethodHints`.
