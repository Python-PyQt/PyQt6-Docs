.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :digest: f6262435988e56a12c9dc8f965048347

Marks the UTF-8 encoded string literal *sourceText* for delayed translation in the current context (class).

The macro tells lupdate to collect the string, and expands to *sourceText* itself.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 393-400

The macro QT_TR_NOOP_UTF8() is identical and obsolete; this applies to all other _UTF8 macros as well.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QT_TRANSLATE_NOOP`.
