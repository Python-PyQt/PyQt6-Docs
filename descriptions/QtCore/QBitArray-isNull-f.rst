.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: e33d1fdfabf69c6c607740cfaf6b7293

Returns ``true`` if this bit array is null; otherwise returns ``false``.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qbitarray.py
    :lines: 102-104

Qt makes a distinction between null bit arrays and empty bit arrays for historical reasons. For most applications, what matters is whether or not a bit array contains any data, and this can be determined using :sip:ref:`~PyQt6.QtCore.QBitArray.isEmpty`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBitArray.isEmpty`.
