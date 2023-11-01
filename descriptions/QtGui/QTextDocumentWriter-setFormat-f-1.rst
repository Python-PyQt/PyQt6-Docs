.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: a761ea022fce63d61051bf0daccaebc4

Sets the format used to write documents to the *format* specified. *format* is a case insensitive text string. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qtextdocumentwriter.py
    :lines: 58-59

You can call :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter.supportedDocumentFormats` for the full list of formats :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter` supports.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter.format`.
