.. sip:method-description::
    :status: todo
    :pysig: 9efb94590302b6384f870c0b26399e03
    :realsig: (const QByteArray&,QUrl::ParsingMode)
    :digest: 7a80b03a6e59b5e7a4c97ac964938498

Parses *input* and returns the corresponding :sip:ref:`~PyQt6.QtCore.QUrl`. *input* is assumed to be in encoded form, containing only ASCII characters.

Parses the URL using *parsingMode*. See :sip:ref:`~PyQt6.QtCore.QUrl.setUrl` for more information on this parameter. :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` is not permitted in this context.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`, :sip:ref:`~PyQt6.QtCore.QUrl.setUrl`.
