.. sip:class-description::
    :status: todo
    :brief: Formatting information for lists in a QTextDocument
    :digest: b992ec9a3777c5f4851915e605c99d8f

The :sip:ref:`~PyQt6.QtGui.QTextListFormat` class provides formatting information for lists in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

A list is composed of one or more items, represented as text blocks. The list's format specifies the appearance of items in the list. In particular, it determines the indentation and the style of each item.

The indentation of the items is an integer value that causes each item to be offset from the left margin by a certain amount. This value is read with :sip:ref:`~PyQt6.QtGui.QTextListFormat.indent` and set with :sip:ref:`~PyQt6.QtGui.QTextListFormat.setIndent`.

The style used to decorate each item is set with :sip:ref:`~PyQt6.QtGui.QTextListFormat.setStyle` and can be read with the :sip:ref:`~PyQt6.QtGui.QTextListFormat.style` function. The style controls the type of bullet points and numbering scheme used for items in the list. Note that lists that use the decimal numbering scheme begin counting at 1 rather than 0, unless it has been overridden via :sip:ref:`~PyQt6.QtGui.QTextListFormat.setStart`.

Style properties can be set to further configure the appearance of list items; for example, the ListNumberPrefix and ListNumberSuffix properties can be used to customize the numbers used in an ordered list so that they appear as (1), (2), (3), etc.:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-textdocument-listitemstyles-mainwindow.py
    :lines: 87-93

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextList`.
