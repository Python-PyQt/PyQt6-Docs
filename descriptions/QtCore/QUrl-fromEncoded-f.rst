.. sip:method-description::
    :status: todo
    :pysig: 9efb94590302b6384f870c0b26399e03
    :realsig: (const QByteArray&,QUrl::ParsingMode)
    :digest: 253973a4b2bbf13b74ed6fb0d6b200ec

Parses *input* and returns the corresponding :sip:ref:`~PyQt6.QtCore.QUrl`. *input* is assumed to be in encoded form, containing only ASCII characters.

Parses the URL using *mode*. See :sip:ref:`~PyQt6.QtCore.QUrl.setUrl` for more information on this parameter. :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` is not permitted in this context.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`, :sip:ref:`~PyQt6.QtCore.QUrl.setUrl`.
