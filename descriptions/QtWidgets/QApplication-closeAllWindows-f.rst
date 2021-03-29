.. sip:method-description::
    :status: todo
    :pysig: a81259cef8e959c624df1d456e5d3297
    :realsig: ()
    :digest: f979c4bf9bb7dc02f5b58d96568559fa

Closes all top-level windows.

This function is particularly useful for applications with many top-level windows.

The windows are closed in random order, until one window does not accept the close event. The application quits when the last window was successfully closed, unless quitOnLastWindowClosed is set to false. To trigger application termination from e.g. a menu, use :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit` instead of this function.

.. seealso:: quitOnLastWindowClosed, lastWindowClosed(), :sip:ref:`~PyQt6.QtWidgets.QWidget.close`, :sip:ref:`~PyQt6.QtWidgets.QWidget.closeEvent`, lastWindowClosed(), :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`, :sip:ref:`~PyQt6.QtWidgets.QApplication.topLevelWidgets`, :sip:ref:`~PyQt6.QtWidgets.QWidget.isWindow`.
