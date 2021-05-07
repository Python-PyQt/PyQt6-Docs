.. sip:method-description::
    :status: todo
    :pysig: 564aed94125708679935a93f47ac92b5
    :realsig: (QStringView,QRegularExpression::WildcardConversionOptions)
    :digest: e65d9aef933da3b4e60ad435ce464a2d

Returns a regular expression representation of the given glob *pattern*. The transformation is targeting file path globbing, which means in particular that path separators receive special treatment. This implies that it is not just a basic translation from "\*" to ".\*".

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qregularexpression.py
    :lines: 344-348

By default, the returned regular expression is fully anchored. In other words, there is no need of calling :sip:ref:`~PyQt6.QtCore.QRegularExpression.anchoredPattern` again on the result. To get an a regular expression that is not anchored, pass :sip:ref:`~PyQt6.QtCore.QRegularExpression.WildcardConversionOption.UnanchoredWildcardConversion` as the conversion *options*.

This implementation follows closely the definition of wildcard for glob patterns:

+------------+---------------------------------------------------------------------------------------------------------------------+
| **c**      | Any character represents itself apart from those mentioned below. Thus **c** matches the character *c*.             |
+------------+---------------------------------------------------------------------------------------------------------------------+
| **?**      | Matches any single character. It is the same as **.** in full regexps.                                              |
+------------+---------------------------------------------------------------------------------------------------------------------+
| **\***     | Matches zero or more of any characters. It is the same as **.\*** in full regexps.                                  |
+------------+---------------------------------------------------------------------------------------------------------------------+
| **[abc]**  | Matches one character given in the bracket.                                                                         |
+------------+---------------------------------------------------------------------------------------------------------------------+
| **[a-c]**  | Matches one character from the range given in the bracket.                                                          |
+------------+---------------------------------------------------------------------------------------------------------------------+
| **[!abc]** | Matches one character that is not given in the bracket. It is the same as **[^abc]** in full regexp.                |
+------------+---------------------------------------------------------------------------------------------------------------------+
| **[!a-c]** | Matches one character that is not from the range given in the bracket. It is the same as **[^a-c]** in full regexp. |
+------------+---------------------------------------------------------------------------------------------------------------------+

**Note:** The backslash (\\) character is *not* an escape char in this context. In order to match one of the special characters, place it in square brackets (for example, ``[?]``).

More information about the implementation can be found in:

* `The Wikipedia Glob article <https://en.wikipedia.org/wiki/Glob_(programming)>`_

* ``man 7 glob``

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpression.escape`.
