.. sip:method-description::
    :status: todo
    :pysig: 3e8150521b21f66410f90d106bb4b0fb
    :realsig: (QByteArrayView, QJsonParseError*)
    :digest: 570b3260c5fddb29ab2bbe5de6725b42

Parses *json* as a UTF-8 encoded JSON value, and creates a :sip:ref:`~PyQt6.QtCore.QJsonValue` from it.

Returns a valid :sip:ref:`~PyQt6.QtCore.QJsonValue` if the parsing succeeds. If it fails, the returned value will be :sip:ref:`~PyQt6.QtCore.QJsonValue.isUndefined`, and the optional *error* variable will contain further details about the error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QJsonParseError`, :sip:ref:`~PyQt6.QtCore.QJsonValue.isUndefined`, :sip:ref:`~PyQt6.QtCore.QJsonValue.toJson`.
