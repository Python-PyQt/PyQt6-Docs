.. sip:method-description::
    :status: todo
    :pysig: d0c7c12c60c6b02dfcb8f6e6277451bf
    :realsig: (QCloseEvent*)
    :digest: 4394ba009b1a4b9d5fccc136dd15e5a0

This event handler is called with the given *event* when Qt receives a window close request for a top-level widget from the window system.

By default, the event is accepted and the widget is closed. You can reimplement this function to change the way the widget responds to window close requests. For example, you can prevent the window from closing by calling :sip:ref:`~PyQt6.QtCore.QEvent.ignore` on all events.

Main window applications typically use reimplementations of this function to check whether the user's work has been saved and ask for permission before closing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtWidgets.QWidget.hide`, :sip:ref:`~PyQt6.QtWidgets.QWidget.close`, :sip:ref:`~PyQt6.QtGui.QCloseEvent`.
