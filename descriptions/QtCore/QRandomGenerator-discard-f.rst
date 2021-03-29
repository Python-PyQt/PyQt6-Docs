.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (unsigned long long)
    :digest: c56eb6b7441a1b95b77eb5df32716201

Discards the next *z* entries from the sequence. This method is equivalent to calling :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generate` *z* times and discarding the result, as in:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qrandom.py
    :lines: 87-88
