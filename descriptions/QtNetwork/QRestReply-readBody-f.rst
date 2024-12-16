.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: ()
    :digest: d172e2807851cc7877d1aaab81425433

Returns the received data as a :sip:ref:`~PyQt6.QtCore.QByteArray`.

Calling this function consumes the data received so far, and any further calls to get response data will return empty until further data has been received.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QRestReply.readJson`, :sip:ref:`~PyQt6.QtNetwork.QRestReply.readText`, QNetworkReply::bytesAvailable(), QNetworkReply::readyRead().
