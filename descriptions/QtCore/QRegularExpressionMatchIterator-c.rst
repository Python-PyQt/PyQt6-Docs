.. sip:class-description::
    :status: todo
    :brief: Iterator on the results of a global match of a QRegularExpression object against a string
    :digest: ec36ce6f589d2b0ac966235e92475605

The :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator` class provides an iterator on the results of a global match of a `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_ object against a string.

A :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator` object is a forward only Java-like iterator; it can be obtained by calling the :sip:ref:`~PyQt6.QtCore.QRegularExpression.globalMatch` function. A new :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator` will be positioned before the first result. You can then call the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator.hasNext` function to check if there are more results available; if so, the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator.next` function will return the next result and advance the iterator.

Each result is a :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch` object holding all the information for that result (including captured substrings).

For instance:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qregularexpression.py
    :lines: 331-338

Moreover, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator` offers a :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator.peekNext` function to get the next result *without* advancing the iterator.

Starting with Qt 6.0, it is also possible to simply use the result of :sip:ref:`~PyQt6.QtCore.QRegularExpression.globalMatch` in a range-based for loop, for instance like this:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qregularexpression.py
    :lines: 362-368

You can retrieve the `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_ object the subject string was matched against by calling the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator.regularExpression` function; the match type and the match options are available as well by calling the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator.matchType` and the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator.matchOptions` respectively.

Please refer to the `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_ documentation for more information about the Qt regular expression classes.

.. seealso:: `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch`.
