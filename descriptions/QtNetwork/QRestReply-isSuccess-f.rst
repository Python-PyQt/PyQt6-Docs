.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 996015c1f4e1b342939f01faa3dc14b1

Returns whether the HTTP status is between 200..299 and no further errors have occurred while receiving the response (for example, abrupt disconnection while receiving the body data). This function is a convenient way to check whether the response is considered successful.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QRestReply.httpStatus`, :sip:ref:`~PyQt6.QtNetwork.QRestReply.hasError`, :sip:ref:`~PyQt6.QtNetwork.QRestReply.error`.
