.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b597c0265ce370d5b1b863c17c697e33

This signal is emitted when the socket is about to close. Connect this signal if you have operations that need to be performed before the socket closes (e.g., if you have data in a separate buffer that needs to be written to the device).

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.close`.
