.. sip:method-description::
    :status: todo
    :pysig: 6308226628f112b3e39232e4bd31fe63
    :realsig: (const char*,const char*,int)
    :digest: 4a64b7eb1988573936306d5d66889d01

Returns a translated version of *sourceText*, optionally based on a *disambiguation* string and value of *n* for strings containing plurals; otherwise returns QString::fromUtf8(\ *sourceText*) if no appropriate translated string is available.

Example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-itemviews-spreadsheet-spreadsheet.py
    :lines: 112-114

If the same *sourceText* is used in different roles within the same context, an additional identifying string may be passed in *disambiguation* (``nullptr`` by default). In Qt 4.4 and earlier, this was the preferred way to pass comments to translators.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 248-251

See Writing Source Code for Translation for a detailed description of Qt's translation mechanisms in general, and the Disambiguate Identical Text section for information on disambiguation.

**Warning:** This method is reentrant only if all translators are installed *before* calling this method. Installing or removing translators while performing translations is not supported. Doing so will probably result in crashes or other undesirable behavior.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.translate`.
