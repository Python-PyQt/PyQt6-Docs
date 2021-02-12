.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (double)
    :digest: 36b15dc64112ecfc6137faf041de1a0a

Generates one random double in the range between 0 (inclusive) and *highest* (exclusive). This function is equivalent to and is implemented as:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qrandom.py
    :lines: 116-116

If the *highest* parameter is negative, the result will be negative too; if it is infinite or NaN, the result will be infinite or NaN too (that is, not random).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generateDouble`.
