.. sip:class-description::
    :status: todo
    :brief: Way to iterate over the items in a QTreeWidget instance
    :digest: e1bd32b792ca27118c291f01e32d49bb

The :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItemIterator` class provides a way to iterate over the items in a :sip:ref:`~PyQt6.QtWidgets.QTreeWidget` instance.

The iterator will walk the items in a pre-order traversal order, thus visiting the parent node *before* it continues to the child nodes.

For example, the following code examples each item in a tree, checking the text in the first column against a user-specified search string:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qtreewidgetitemiterator-using-mainwindow.py
    :lines: 135-140

It is also possible to filter out certain types of node by passing certain :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItemIterator.IteratorFlags.IteratorFlag` to the constructor of :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItemIterator`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidget`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`.
