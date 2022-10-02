.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 8b4fbd104dffd7134d00bbf35fd51b51

Returns ``true`` if the reader has read until the end of the XML document, or if an :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.error` has occurred and reading has been aborted. Otherwise, it returns ``false``.

When atEnd() and :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.hasError` return true and :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.error` returns :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.Error.PrematureEndOfDocumentError`, it means the XML has been well-formed so far, but a complete XML document has not been parsed. The next chunk of XML can be added with :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.addData`, if the XML is being read from a :sip:ref:`~PyQt6.QtCore.QByteArray`, or by waiting for more data to arrive if the XML is being read from a :sip:ref:`~PyQt6.QtCore.QIODevice`. Either way, atEnd() will return false once more data is available.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.hasError`, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.error`, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.device`, :sip:ref:`~PyQt6.QtCore.QIODevice.atEnd`.
