.. sip:method-description::
    :status: todo
    :pysig: 5a6e30521ff6150b2e0a693194e10d98
    :realsig: ()
    :digest: 55402039ec445a3697e4d5f879a808f7

Returns the active popup widget.

A popup widget is a special top-level widget that sets the ``Qt::WType_Popup`` widget flag, e.g. the :sip:ref:`~PyQt6.QtWidgets.QMenu` widget. When the application opens a popup widget, all events are sent to the popup. Normal widgets and modal widgets cannot be accessed before the popup widget is closed.

Only other popup widgets may be opened when a popup widget is shown. The popup widgets are organized in a stack. This function returns the active popup widget at the top of the stack.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.activeModalWidget`, :sip:ref:`~PyQt6.QtWidgets.QApplication.topLevelWidgets`.
