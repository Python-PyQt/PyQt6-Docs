.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: cf9117b3873c3f741230d2963236c12b

Returns ``true`` if an error occurred while trying to write data.

If the error is :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.Error.IO`, subsequent writes to the underlying :sip:ref:`~PyQt6.QtCore.QIODevice` will fail. In other cases malformed data might be written to the document.

The error status is never reset. Writes happening after the error occurred may be ignored, even if the error condition is cleared.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.error`, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.errorString`.
