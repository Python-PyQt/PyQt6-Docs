.. sip:method-description::
    :status: todo
    :pysig: 6c3af436f7ed26d8ee765e3f649873e6
    :realsig: (QByteArray*,QObject*)
    :digest: 9b90659a3a1a9a1be349e778463228c5

Constructs a :sip:ref:`~PyQt6.QtCore.QBuffer` that uses the :sip:ref:`~PyQt6.QtCore.QByteArray` pointed to by *byteArray* as its internal buffer, and with the given *parent*. The caller is responsible for ensuring that *byteArray* remains valid until the :sip:ref:`~PyQt6.QtCore.QBuffer` is destroyed, or until :sip:ref:`~PyQt6.QtCore.QBuffer.setBuffer` is called to change the buffer. :sip:ref:`~PyQt6.QtCore.QBuffer` doesn't take ownership of the :sip:ref:`~PyQt6.QtCore.QByteArray`.

If you open the buffer in write-only mode or read-write mode and write something into the :sip:ref:`~PyQt6.QtCore.QBuffer`, *byteArray* will be modified.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-buffer-buffer.py
    :lines: 102-108

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBuffer.open`, :sip:ref:`~PyQt6.QtCore.QBuffer.setBuffer`, :sip:ref:`~PyQt6.QtCore.QBuffer.setData`.
