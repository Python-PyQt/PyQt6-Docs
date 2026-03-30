.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: bb61a9fa9f3b8157c6ce1cc4123940e6

Returns ``true`` if an error occurred while trying to write data.

If the error is :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.Error.IO`, subsequent writes to the underlying :sip:ref:`~PyQt6.QtCore.QIODevice` will fail. In other cases malformed data might be written to the document.

The error status is never reset. Writes happening after the error occurred may be ignored, even if the error condition is cleared.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.error`, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.errorString`, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.raiseError`.
