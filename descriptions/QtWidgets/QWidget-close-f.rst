.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 3e6a7f0f7e99a48cc225c7609ec0a8d7

Closes this widget. Returns ``true`` if the widget was closed; otherwise returns ``false``.

First it sends the widget a :sip:ref:`~PyQt6.QtGui.QCloseEvent`. The widget is :sip:ref:`~PyQt6.QtWidgets.QWidget.hide` if it :sip:ref:`~PyQt6.QtCore.QEvent.accept` the close event. If it :sip:ref:`~PyQt6.QtCore.QEvent.ignore` the event, nothing happens. The default implementation of :sip:ref:`~PyQt6.QtWidgets.QWidget.closeEvent` accepts the close event.

If the widget has the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_DeleteOnClose` flag, the widget is also deleted. A close events is delivered to the widget no matter if the widget is visible or not.

The :sip:ref:`~PyQt6.QtGui.QGuiApplication.lastWindowClosed` signal is emitted when the last visible primary window (i.e. window with no parent) with the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_QuitOnClose` attribute set is closed. By default this attribute is set for all widgets except transient windows such as splash screens, tool windows, and popup menus.
