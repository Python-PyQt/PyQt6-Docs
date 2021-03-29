.. sip:class-description::
    :status: todo
    :brief: Contains parameters that describe a close event
    :digest: dff914c8e2c53f317175a39bc96e19ae

The :sip:ref:`~PyQt6.QtGui.QCloseEvent` class contains parameters that describe a close event.

Close events are sent to widgets that the user wants to close, usually by choosing "Close" from the window menu, or by clicking the X title bar button. They are also sent when you call :sip:ref:`~PyQt6.QtWidgets.QWidget.close` to close a widget programmatically.

Close events contain a flag that indicates whether the receiver wants the widget to be closed or not. When a widget accepts the close event, it is hidden (and destroyed if it was created with the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_DeleteOnClose` flag). If it refuses to accept the close event nothing happens. (Under X11 it is possible that the window manager will forcibly close the window; but at the time of writing we are not aware of any window manager that does this.)

The event handler :sip:ref:`~PyQt6.QtWidgets.QWidget.closeEvent` receives close events. The default implementation of this event handler accepts the close event. If you do not want your widget to be hidden, or want some special handling, you should reimplement the event handler and ignore() the event.

The `closeEvent() in the Application example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-application-example.html#close-event-handler>`_ shows a close event handler that asks whether to save a document before closing.

If you want the widget to be deleted when it is closed, create it with the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_DeleteOnClose` flag. This is very useful for independent top-level windows in a multi-window application.

:sip:ref:`~PyQt6.QtCore.QObject`\ s emits the :sip:ref:`~PyQt6.QtCore.QObject.destroyed` signal when they are deleted.

If the last top-level window is closed, the :sip:ref:`~PyQt6.QtGui.QGuiApplication.lastWindowClosed` signal is emitted.

The isAccepted() function returns ``true`` if the event's receiver has agreed to close the widget; call accept() to agree to close the widget and call ignore() if the receiver of this event does not want the widget to be closed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.close`, :sip:ref:`~PyQt6.QtWidgets.QWidget.hide`, :sip:ref:`~PyQt6.QtCore.QObject.destroyed`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.lastWindowClosed`.
