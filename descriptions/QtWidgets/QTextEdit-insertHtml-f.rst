.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 0bd4ddceb82856b80fe0ac674611cc8e

Convenience slot that inserts *text* which is assumed to be of html formatting at the current cursor position.

It is equivalent to:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qtextedit.py
    :lines: 71-71

**Note:** When using this function with a style sheet, the style sheet will only apply to the current block in the document. In order to apply a style sheet throughout a document, use :sip:ref:`~PyQt6.QtGui.QTextDocument.setDefaultStyleSheet` instead.
