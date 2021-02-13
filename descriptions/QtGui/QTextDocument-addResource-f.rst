.. sip:method-description::
    :status: todo
    :pysig: 6d0326a171f9010df7bb3ffa33de1b6a
    :realsig: (int,const QUrl&,const QVariant&)
    :digest: f0a286b30aa05874a4b3dd87b10c8af5

Adds the resource *resource* to the resource cache, using *type* and *name* as identifiers. *type* should be a value from :sip:ref:`~PyQt6.QtGui.QTextDocument.ResourceType`.

For example, you can add an image as a resource in order to reference it from within the document:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-textdocument-resources-main.py
    :lines: 72-73

The image can be inserted into the document using the :sip:ref:`~PyQt6.QtGui.QTextCursor` API:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-textdocument-resources-main.py
    :lines: 77-79

Alternatively, you can insert images using the HTML ``img`` tag:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-textdocument-resources-main.py
    :lines: 91-91
