.. sip:class-description::
    :status: todo
    :brief: Container for text blocks within a QTextDocument
    :digest: 321830739ba723e5b40b22068dd2d2cc

The :sip:ref:`~PyQt6.QtGui.QTextBlockGroup` class provides a container for text blocks within a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

Block groups can be used to organize blocks of text within a document. They maintain an up-to-date list of the text blocks that belong to them, even when text blocks are being edited.

Each group has a parent document which is specified when the group is constructed.

Text blocks can be inserted into a group with :sip:ref:`~PyQt6.QtGui.QTextBlockGroup.blockInserted`, and removed with :sip:ref:`~PyQt6.QtGui.QTextBlockGroup.blockRemoved`. If a block's format is changed, :sip:ref:`~PyQt6.QtGui.QTextBlockGroup.blockFormatChanged` is called.

The list of blocks in the group is returned by :sip:ref:`~PyQt6.QtGui.QTextBlockGroup.blockList`. Note that the blocks in the list are not necessarily adjacent elements in the document; for example, the top-level items in a multi-level list will be separated by the items in lower levels of the list.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextBlock`, :sip:ref:`~PyQt6.QtGui.QTextDocument`.
