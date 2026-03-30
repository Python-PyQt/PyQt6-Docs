.. sip:method-description::
    :status: todo
    :pysig: f1ebda0f8399d374cad42c476e4ee5da
    :realsig: (QByteArrayView, QJsonParseError*)
    :digest: 570b3260c5fddb29ab2bbe5de6725b42

Parses *json* as a UTF-8 encoded JSON value, and creates a :sip:ref:`~PyQt6.QtCore.QJsonValue` from it.

Returns a valid :sip:ref:`~PyQt6.QtCore.QJsonValue` if the parsing succeeds. If it fails, the returned value will be :sip:ref:`~PyQt6.QtCore.QJsonValue.isUndefined`, and the optional *error* variable will contain further details about the error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QJsonParseError`, :sip:ref:`~PyQt6.QtCore.QJsonValue.isUndefined`, :sip:ref:`~PyQt6.QtCore.QJsonValue.toJson`.
