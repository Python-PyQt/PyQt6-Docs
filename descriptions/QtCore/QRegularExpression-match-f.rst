.. sip:method-description::
    :status: todo
    :pysig: 845efc29fe55534c6e6b83532eb64b29
    :realsig: (const QString&, qsizetype, QRegularExpression::MatchType, QRegularExpression::MatchOptions) const
    :digest: 8dd5e2fafb4e8f61211892de4e9c28cc

Attempts to match the regular expression against the given *subject* string, starting at the position *offset* inside the subject, using a match of type *matchType* and honoring the given *matchOptions*.

The returned :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch` object contains the results of the match.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch`, :ref:`normal matching<qregularexpression-normal-matching>`.
