.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: ()
    :digest: 3e7f76d93d3140a3e8790a4df1445e76

Returns the received data as a QString.

The received data is decoded into a QString (UTF-16). If available, the decoding uses the *Content-Type* header's *charset* parameter to determine the source encoding. If the encoding information is not available or not supported by :sip:ref:`~PyQt6.QtCore.QStringConverter`, UTF-8 is used by default.

Calling this function consumes the data received so far. Returns a default constructed value if no new data is available, or if the decoding is not supported by :sip:ref:`~PyQt6.QtCore.QStringConverter`, or if the decoding has errors (for example invalid characters).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QRestReply.readJson`, :sip:ref:`~PyQt6.QtNetwork.QRestReply.readBody`, QNetworkReply::readyRead().
