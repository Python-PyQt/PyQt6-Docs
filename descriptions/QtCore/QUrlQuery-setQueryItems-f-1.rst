.. sip:method-description::
    :status: todo
    :pysig: 616d13a4e4ac909330749ec93e64db5d
    :realsig: (const QList<std::pair<QString, QString>>&)
    :digest: 139cb9dce9305c3b04ccb0a5ce433702

Sets the items in this :sip:ref:`~PyQt6.QtCore.QUrlQuery` object to *query*. The order of the elements in *query* is preserved.

**Note:** This method does not treat spaces (ASCII 0x20) and plus ("+") signs as the same, like HTML forms do. If you need spaces to be represented as plus signs, use actual plus signs.

**Note:** The keys and values are expected to be in percent-encoded form.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrlQuery.queryItems`, :sip:ref:`~PyQt6.QtCore.QUrlQuery.isEmpty`.
