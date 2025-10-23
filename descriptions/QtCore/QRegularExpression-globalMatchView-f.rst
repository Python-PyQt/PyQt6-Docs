.. sip:method-description::
    :status: todo
    :pysig: 00157086923d3b5f50d97a3528869435
    :realsig: (QStringView,qsizetype,QRegularExpression::MatchType,QRegularExpression::MatchOptions) const
    :digest: 0ea801319ba48785d12eed10f4867f34

Attempts to perform a global match of the regular expression against the given *subjectView* string view, starting at the position *offset* inside the subject, using a match of type *matchType* and honoring the given *matchOptions*.

The returned :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator` is positioned before the first match result (if any).

**Note:** The data referenced by *subjectView* must remain valid as long as there are :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator` or :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch` objects using it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator`, :ref:`global matching<qregularexpression-global-matching>`.
