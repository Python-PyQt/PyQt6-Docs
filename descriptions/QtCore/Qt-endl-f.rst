.. sip:method-description::
    :status: todo
    :pysig: 6a92baff980461b7259f7ddc2e7ccd95
    :realsig: (QTextStream&)
    :digest: bb3a023f222cc3606f38f99c517eb578

Writes '\\n' to the *stream* and flushes the stream.

Equivalent to

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qtextstream.py
    :lines: 134-134

Note: On Windows, all '\\n' characters are written as '\\r\\n' if :sip:ref:`~PyQt6.QtCore.QTextStream`'s device or string is opened using the QIODevice::Text flag.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.flush`, :sip:ref:`~PyQt6.QtCore.Qt.reset`, QTextStream manipulators.
