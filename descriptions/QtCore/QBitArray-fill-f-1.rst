.. sip:method-description::
    :status: todo
    :pysig: 1d564629261b4e6291e96f2cc52ac538
    :realsig: (bool,qsizetype,qsizetype)
    :digest: 3836eccc820dfe1d802f38fceb8768a5

Sets bits at index positions *begin* up to (but not including) *end* to *value*.

*begin* must be a valid index position in the bit array (0 <= *begin* < :sip:ref:`~PyQt6.QtCore.QBitArray.size`).

*end* must be either a valid index position or equal to :sip:ref:`~PyQt6.QtCore.QBitArray.size`, in which case the fill operation runs until the end of the array (0 <= *end* <= :sip:ref:`~PyQt6.QtCore.QBitArray.size`).

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qbitarray.py
    :lines: 191-194
