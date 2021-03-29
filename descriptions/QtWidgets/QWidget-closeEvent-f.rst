.. sip:method-description::
    :status: todo
    :pysig: d0c7c12c60c6b02dfcb8f6e6277451bf
    :realsig: (QCloseEvent*)
    :digest: dfce056a8cc805b325038d9c817f7b8b

This event handler is called with the given *event* when Qt receives a window close request for a top-level widget from the window system.

By default, the event is accepted and the widget is closed. You can reimplement this function to change the way the widget responds to window close requests. For example, you can prevent the window from closing by calling :sip:ref:`~PyQt6.QtCore.QEvent.ignore` on all events.

Main window applications typically use reimplementations of this function to check whether the user's work has been saved and ask for permission before closing. For example, the `Qt Widgets - Application Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-application-example.html>`_ uses a helper function to determine whether or not to close the window:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-mainwindows-application-mainwindow.py
    :lines: 85-85

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-mainwindows-application-mainwindow.py
    :lines: 87-94

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtWidgets.QWidget.hide`, :sip:ref:`~PyQt6.QtWidgets.QWidget.close`, :sip:ref:`~PyQt6.QtGui.QCloseEvent`, `Qt Widgets - Application Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-application-example.html>`_.
