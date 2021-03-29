.. sip:class-description::
    :status: todo
    :brief: Container for text fragments in a QTextDocument
    :digest: a7fd19e18a407585214529f1efa8be56

The :sip:ref:`~PyQt6.QtGui.QTextBlock` class provides a container for text fragments in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

A text block encapsulates a block or paragraph of text in a :sip:ref:`~PyQt6.QtGui.QTextDocument`. :sip:ref:`~PyQt6.QtGui.QTextBlock` provides read-only access to the block/paragraph structure of QTextDocuments. It is mainly of use if you want to implement your own layouts for the visual representation of a :sip:ref:`~PyQt6.QtGui.QTextDocument`, or if you want to iterate over a document and write out the contents in your own custom format.

Text blocks are created by their parent documents. If you need to create a new text block, or modify the contents of a document while examining its contents, use the cursor-based interface provided by :sip:ref:`~PyQt6.QtGui.QTextCursor` instead.

Each text block is located at a specific :sip:ref:`~PyQt6.QtGui.QTextBlock.position` in a :sip:ref:`~PyQt6.QtGui.QTextBlock.document`. The contents of the block can be obtained by using the :sip:ref:`~PyQt6.QtGui.QTextBlock.text` function. The :sip:ref:`~PyQt6.QtGui.QTextBlock.length` function determines the block's size within the document (including formatting characters). The visual properties of the block are determined by its text :sip:ref:`~PyQt6.QtGui.QTextBlock.layout`, its :sip:ref:`~PyQt6.QtGui.QTextBlock.charFormat`, and its :sip:ref:`~PyQt6.QtGui.QTextBlock.blockFormat`.

The :sip:ref:`~PyQt6.QtGui.QTextBlock.next` and :sip:ref:`~PyQt6.QtGui.QTextBlock.previous` functions enable iteration over consecutive valid blocks in a document under the condition that the document is not modified by other means during the iteration process. Note that, although blocks are returned in sequence, adjacent blocks may come from different places in the document structure. The validity of a block can be determined by calling :sip:ref:`~PyQt6.QtGui.QTextBlock.isValid`.

:sip:ref:`~PyQt6.QtGui.QTextBlock` provides comparison operators to make it easier to work with blocks: operator==() compares two block for equality, operator!=() compares two blocks for inequality, and operator<() determines whether a block precedes another in the same document.

.. image:: ../../../images/qtextblock-sequence.png

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextBlockFormat`, :sip:ref:`~PyQt6.QtGui.QTextCharFormat`, :sip:ref:`~PyQt6.QtGui.QTextFragment`.
