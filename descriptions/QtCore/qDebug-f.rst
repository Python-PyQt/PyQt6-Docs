.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const char*)
    :digest: 46fff97ab88a43b11842fd6426390297

Returns a QDebug object that logs a debug message to the central message handler.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 322-322

Using qDebug() is an alternative to qDebug(const char *, ...), which follows the printf paradigm.

Note that QDebug and the type specific stream operators do add various formatting to make the debug message easier to read. See the :ref:`qdebug-formatting-options` documentation for more details.

This function does nothing if ``QT_NO_DEBUG_OUTPUT`` was defined during compilation.

.. seealso:: qDebug(const char *, ...), qCDebug().
