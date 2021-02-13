.. sip:class-description::
    :status: todo
    :brief: Decorated list of items in a QTextDocument
    :digest: 27ed20aa933e73ca88077bed27092dfc

The :sip:ref:`~PyQt6.QtGui.QTextList` class provides a decorated list of items in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

A list contains a sequence of text blocks, each of which is marked with a bullet point or other symbol. Multiple levels of lists can be used, and the automatic numbering feature provides support for ordered numeric and alphabetical lists.

Lists are created by using a text cursor to insert an empty list at the current position or by moving existing text into a new list. The :sip:ref:`~PyQt6.QtGui.QTextCursor.insertList` function inserts an empty block into the document at the cursor position, and makes it the first item in a list.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-textdocument-lists-mainwindow.py
    :lines: 70-77

The :sip:ref:`~PyQt6.QtGui.QTextCursor.createList` function takes the contents of the cursor's current block and turns it into the first item of a new list.

The cursor's current list is found with :sip:ref:`~PyQt6.QtGui.QTextCursor.currentList`.

The number of items in a list is given by :sip:ref:`~PyQt6.QtGui.QTextList.count`. Each item can be obtained by its index in the list with the :sip:ref:`~PyQt6.QtGui.QTextList.item` function. Similarly, the index of a given item can be found with :sip:ref:`~PyQt6.QtGui.QTextList.itemNumber`. The text of each item can be found with the :sip:ref:`~PyQt6.QtGui.QTextList.itemText` function.

Note that the items in the list may not be adjacent elements in the document. For example, the top-level items in a multi-level list will be separated by the items in lower levels of the list.

List items can be deleted by index with the :sip:ref:`~PyQt6.QtGui.QTextList.removeItem` function. :sip:ref:`~PyQt6.QtGui.QTextList.remove` deletes the specified item in the list.

The list's format is set with :sip:ref:`~PyQt6.QtGui.QTextList.setFormat` and read with :sip:ref:`~PyQt6.QtGui.QTextList.format`. The format describes the decoration of the list itself, and not the individual items.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextBlock`, :sip:ref:`~PyQt6.QtGui.QTextListFormat`, :sip:ref:`~PyQt6.QtGui.QTextCursor`.
