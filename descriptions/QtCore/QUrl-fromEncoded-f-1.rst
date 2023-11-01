.. sip:method-description::
    :status: todo
    :pysig: a3133265c5644235b78fc1ef26e622b2
    :realsig: (const QByteArray&, QUrl::ParsingMode)
    :digest: 253973a4b2bbf13b74ed6fb0d6b200ec

Parses *input* and returns the corresponding :sip:ref:`~PyQt6.QtCore.QUrl`. *input* is assumed to be in encoded form, containing only ASCII characters.

Parses the URL using *mode*. See :sip:ref:`~PyQt6.QtCore.QUrl.setUrl` for more information on this parameter. :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` is not permitted in this context.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`, :sip:ref:`~PyQt6.QtCore.QUrl.setUrl`.
