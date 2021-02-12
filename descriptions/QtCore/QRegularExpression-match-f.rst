.. sip:method-description::
    :status: todo
    :pysig: 6edf39bee2f4a07a0fbb15262dee36e5
    :realsig: (QStringView,qsizetype,QRegularExpression::MatchType,QRegularExpression::MatchOptions) const
    :digest: 94f7eeea08885864fdbdc2e77f4cd25c

This is an overloaded function.

Attempts to match the regular expression against the given *subjectView* string view, starting at the position *offset* inside the subject, using a match of type *matchType* and honoring the given *matchOptions*.

The returned :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch` object contains the results of the match.

**Note:** The data referenced by *subjectView* must remain valid as long as there are :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch` objects using it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch`, :ref:`normal matching<qregularexpression-normal-matching>`.
