.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: fddd4d789b604e4071a783d8f8a189aa

Returns a list of :sip:ref:`~PyQt6.QtCore.QRegularExpression.captureCount` + 1 elements, containing the names of the named capturing groups in the pattern string. The list is sorted such that the element of the list at position ``i`` is the name of the ``i``-th capturing group, if it has a name, or an empty string if that capturing group is unnamed.

For instance, given the regular expression

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qregularexpression.py
    :lines: 353-353

namedCaptureGroups() will return the following list:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qregularexpression.py
    :lines: 357-357

which corresponds to the fact that the capturing group #0 (corresponding to the whole match) has no name, the capturing group #1 has name "day", the capturing group #2 has name "month", etc.

If the regular expression is not valid, returns an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpression.isValid`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.captured`, QString::isEmpty().
