.. sip:method-description::
    :status: todo
    :pysig: 33390e4334a6fb93c6219ad7577f46cf
    :realsig: (bool,qsizetype)
    :digest: 398381cd8904eda01f3a2cda1157c964

Sets every bit in the bit array to *value*, returning true if successful; otherwise returns ``false``. If *size* is different from -1 (the default), the bit array is resized to *size* beforehand.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qbitarray.py
    :lines: 109-114

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBitArray.resize`.
