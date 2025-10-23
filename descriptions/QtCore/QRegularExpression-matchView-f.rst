.. sip:method-description::
    :status: todo
    :pysig: 1e6a49623b88925bdd39deeb3f360072
    :realsig: (QStringView,qsizetype,QRegularExpression::MatchType,QRegularExpression::MatchOptions) const
    :digest: 955b26b448f6602ee281239c5a07a681

Attempts to match the regular expression against the given *subjectView* string view, starting at the position *offset* inside the subject, using a match of type *matchType* and honoring the given *matchOptions*.

The returned :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch` object contains the results of the match.

**Note:** The data referenced by *subjectView* must remain valid as long as there are :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch` objects using it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch`, :ref:`normal matching<qregularexpression-normal-matching>`.
