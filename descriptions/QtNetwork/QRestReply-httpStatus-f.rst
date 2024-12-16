.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 726e45ba68400e219bfe7a7e1238863a

Returns the HTTP status received in the server response. The value is *0* if not available (the status line has not been received, yet).

**Note:** The HTTP status is reported as indicated by the received HTTP response. An :sip:ref:`~PyQt6.QtNetwork.QRestReply.error` may occur after receiving the status, for instance due to network disconnection while receiving a long response. These potential subsequent errors are not represented by the reported HTTP status.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QRestReply.isSuccess`, :sip:ref:`~PyQt6.QtNetwork.QRestReply.hasError`, :sip:ref:`~PyQt6.QtNetwork.QRestReply.error`.
