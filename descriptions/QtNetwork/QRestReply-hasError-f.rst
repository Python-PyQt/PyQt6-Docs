.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: c1498f9c05cff6522def6c5760761c88

Returns whether an error has occurred. This includes errors such as network and protocol errors, but excludes cases where the server successfully responded with an HTTP error status (for example ``500 Internal Server Error``). Use :sip:ref:`~PyQt6.QtNetwork.QRestReply.httpStatus` or :sip:ref:`~PyQt6.QtNetwork.QRestReply.isHttpStatusSuccess` to get the HTTP status information.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QRestReply.httpStatus`, :sip:ref:`~PyQt6.QtNetwork.QRestReply.isSuccess`, :sip:ref:`~PyQt6.QtNetwork.QRestReply.error`, :sip:ref:`~PyQt6.QtNetwork.QRestReply.errorString`.
