.. sip:method-description::
    :status: todo
    :pysig: daf24e4b6d97e9b2024ef2d61e7e605e
    :realsig: (const QByteArray&, QJsonParseError*)
    :digest: db458357c8e6edcce2f9422500bc28ba

Parses *json* as a UTF-8 encoded JSON document, and creates a :sip:ref:`~PyQt6.QtCore.QJsonDocument` from it.

Returns a valid (non-null) :sip:ref:`~PyQt6.QtCore.QJsonDocument` if the parsing succeeds. If it fails, the returned document will be null, and the optional *error* variable will contain further details about the error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QJsonDocument.toJson`, :sip:ref:`~PyQt6.QtCore.QJsonParseError`, :sip:ref:`~PyQt6.QtCore.QJsonDocument.isNull`.
