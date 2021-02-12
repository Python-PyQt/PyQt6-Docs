.. sip:method-description::
    :status: todo
    :pysig: 1afe59e58c16db6bcfee93505f94567b
    :realname: QRandomGenerator::global
    :realsig: ()
    :digest: 6754ee37a9b3a40ef2d73b1311337e0a

Returns a pointer to a shared :sip:ref:`~PyQt6.QtCore.QRandomGenerator` that was seeded using :sip:ref:`~PyQt6.QtCore.QRandomGenerator.securelySeeded`. This function should be used to create random data without the expensive creation of a securely-seeded :sip:ref:`~PyQt6.QtCore.QRandomGenerator` for a specific use or storing the rather large :sip:ref:`~PyQt6.QtCore.QRandomGenerator` object.

For example, the following creates a random RGB color:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qrandom.py
    :lines: 128-128

Accesses to this object are thread-safe and it may therefore be used in any thread without locks. The object may also be copied and the sequence produced by the copy will be the same as the shared object will produce. Note, however, that if there are other threads accessing the global object, those threads may obtain samples at unpredictable intervals.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRandomGenerator.securelySeeded`, :sip:ref:`~PyQt6.QtCore.QRandomGenerator.system`.
