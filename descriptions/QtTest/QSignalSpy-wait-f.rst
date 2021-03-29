.. sip:method-description::
    :status: todo
    :pysig: 3693397ff4e0cae2d0a0152cd1722150
    :realsig: (int)
    :digest: 80eb36c8ad1d6bd4ae554ae38c778112

Starts an event loop that runs until the given signal is received. Optionally the event loop can return earlier on a *timeout* (in milliseconds).

Returns ``true`` if the signal was emitted at least once in *timeout* milliseconds, otherwise returns ``false``.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-doc_src_qsignalspy.py
    :lines: 96-96
