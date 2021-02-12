.. sip:class-description::
    :status: todo
    :brief: The results of a matching a QRegularExpression against a string
    :digest: 194f18faa2a96e21516443aef9c06c35

The :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch` class provides the results of a matching a `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_ against a string.

A :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch` object can be obtained by calling the :sip:ref:`~PyQt6.QtCore.QRegularExpression.match` function, or as a single result of a global match from a :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator`.

The success or the failure of a match attempt can be inspected by calling the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.hasMatch` function. :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch` also reports a successful partial match through the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.hasPartialMatch` function.

In addition, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch` returns the substrings captured by the capturing groups in the pattern string. The implicit capturing group with index 0 captures the result of the whole match. The :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.captured` function returns each substring captured, either by the capturing group's index or by its name:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qregularexpression.py
    :lines: 320-325

For each captured substring it is possible to query its starting and ending offsets in the subject string by calling the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedStart` and the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedEnd` function, respectively. The length of each captured substring is available using the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedLength` function.

The convenience function :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedTexts` will return *all* the captured substrings at once (including the substring matched by the entire pattern) in the order they have been captured by capturing groups; that is, ``captured(i) == capturedTexts().at(i)``.

You can retrieve the `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_ object the subject string was matched against by calling the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.regularExpression` function; the match type and the match options are available as well by calling the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.matchType` and the :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.matchOptions` respectively.

Please refer to the `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_ documentation for more information about the Qt regular expression classes.

.. seealso:: `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_.
