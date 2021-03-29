.. sip:method-description::
    :status: todo
    :pysig: 88ef868705cc2335f9e741fe200ba116
    :digest: 7cdabfc0e828211122d474d9bc7749a0

Marks the UTF-8 encoded string literal *sourceText* for delayed translation in the given *context*. The *context* is typically a class name and also needs to be specified as a string literal.

The macro tells lupdate to collect the string, and expands to *sourceText* itself.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 405-419

.. seealso:: :sip:ref:`~PyQt6.QtCore.QT_TR_NOOP`, QT_TRANSLATE_NOOP3().
