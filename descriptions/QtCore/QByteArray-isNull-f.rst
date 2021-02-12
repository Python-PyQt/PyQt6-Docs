.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 563d228c3efa651b7fbf7c86b2eeba0f

Returns ``true`` if this byte array is null; otherwise returns ``false``.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 166-168

Qt makes a distinction between null byte arrays and empty byte arrays for historical reasons. For most applications, what matters is whether or not a byte array contains any data, and this can be determined using :sip:ref:`~PyQt6.QtCore.QByteArray.isEmpty`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.isEmpty`.
