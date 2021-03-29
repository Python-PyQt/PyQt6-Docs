.. sip:method-description::
    :status: todo
    :pysig: 14951241e2147d3b74807a2b723f4bec
    :realsig: (QEventLoop::ProcessEventsFlags)
    :digest: c4f17f2a1c9e4199e61a7505ae1af4fc

Enters the main event loop and waits until :sip:ref:`~PyQt6.QtCore.QEventLoop.exit` is called. Returns the value that was passed to :sip:ref:`~PyQt6.QtCore.QEventLoop.exit`.

If *flags* are specified, only events of the types allowed by the *flags* will be processed.

It is necessary to call this function to start event handling. The main event loop receives events from the window system and dispatches these to the application widgets.

Generally speaking, no user interaction can take place before calling . As a special case, modal widgets like :sip:ref:`~PyQt6.QtWidgets.QMessageBox` can be used before calling , because modal widgets use their own local event loop.

To make your application perform idle processing (i.e. executing a special function whenever there are no pending events), use a :sip:ref:`~PyQt6.QtCore.QTimer` with 0 timeout. More sophisticated idle processing schemes can be achieved using :sip:ref:`~PyQt6.QtCore.QEventLoop.processEvents`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`, :sip:ref:`~PyQt6.QtCore.QEventLoop.exit`, :sip:ref:`~PyQt6.QtCore.QEventLoop.processEvents`.
