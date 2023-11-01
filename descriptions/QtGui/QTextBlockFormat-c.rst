.. sip:class-description::
    :status: todo
    :brief: Formatting information for blocks of text in a QTextDocument
    :digest: 49235f1bd318b39cd466ef076aa31206

The :sip:ref:`~PyQt6.QtGui.QTextBlockFormat` class provides formatting information for blocks of text in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

A document is composed of a list of blocks, represented by :sip:ref:`~PyQt6.QtGui.QTextBlock` objects. Each block can contain an item of some kind, such as a paragraph of text, a table, a list, or an image. Every block has an associated :sip:ref:`~PyQt6.QtGui.QTextBlockFormat` that specifies its characteristics.

To cater for left-to-right and right-to-left languages you can set a block's direction with setLayoutDirection(). Paragraph alignment is set with :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.setAlignment`. Margins are controlled by :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.setTopMargin`, :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.setBottomMargin`, :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.setLeftMargin`, :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.setRightMargin`. Overall indentation is set with :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.setIndent`, the indentation of the first line with :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.setTextIndent`.

Line spacing is set with :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.setLineHeight` and retrieved via :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.lineHeight` and :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.lineHeightType`. The types of line spacing available are in the :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.LineHeightTypes.LineHeightTypes` enum.

Line breaking can be enabled and disabled with :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.setNonBreakableLines`.

The brush used to paint the paragraph's background is set with :sip:ref:`~PyQt6.QtGui.QTextFormat.setBackground`, and other aspects of the text's appearance can be customized by using the :sip:ref:`~PyQt6.QtGui.QTextFormat.setProperty` function with the ``OutlinePen``, ``ForegroundBrush``, and ``BackgroundBrush`` :sip:ref:`~PyQt6.QtGui.QTextFormat.Property` values.

If a text block is part of a list, it can also have a list format that is accessible with the listFormat() function.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextBlock`, :sip:ref:`~PyQt6.QtGui.QTextCharFormat`.
