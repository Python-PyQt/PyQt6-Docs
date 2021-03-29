.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (QByteArray*)
    :digest: b640ba8f90daa9e530b2623d24b9028c

Makes :sip:ref:`~PyQt6.QtCore.QBuffer` uses the :sip:ref:`~PyQt6.QtCore.QByteArray` pointed to by *byteArray* as its internal buffer. The caller is responsible for ensuring that *byteArray* remains valid until the :sip:ref:`~PyQt6.QtCore.QBuffer` is destroyed, or until  is called to change the buffer. :sip:ref:`~PyQt6.QtCore.QBuffer` doesn't take ownership of the :sip:ref:`~PyQt6.QtCore.QByteArray`.

Does nothing if isOpen() is true.

If you open the buffer in write-only mode or read-write mode and write something into the :sip:ref:`~PyQt6.QtCore.QBuffer`, *byteArray* will be modified.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-buffer-buffer.py
    :lines: 115-122

If *byteArray* is ``nullptr``, the buffer creates its own internal :sip:ref:`~PyQt6.QtCore.QByteArray` to work on. This byte array is initially empty.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBuffer.buffer`, :sip:ref:`~PyQt6.QtCore.QBuffer.setData`, :sip:ref:`~PyQt6.QtCore.QBuffer.open`.
