.. sip:method-description::
    :status: todo
    :pysig: 564aed94125708679935a93f47ac92b5
    :realsig: (QStringView,QRegularExpression::WildcardConversionOptions)
    :digest: 2187d7b48dbad372dd64280a5c242234

Returns a regular expression representation of the given glob *pattern*.

There are two transformations possible, one that targets file path globbing, and another one which is more generic.

By default, the transformation is targeting file path globbing, which means in particular that path separators receive special treatment. This implies that it is not just a basic translation from "\*" to ".\*" and similar.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qregularexpression.py
    :lines: 344-348

The more generic globbing transformation is available by passing ``NonPathWildcardConversion`` in the conversion *options*.

This implementation follows closely the definition of wildcard for glob patterns:

+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **c**      | Any character represents itself apart from those mentioned below. Thus **c** matches the character *c*.                                                       |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **?**      | Matches any single character, except for a path separator (in case file path globbing has been selected). It is the same as b{.} in full regexps.             |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\***     | Matches zero or more of any characters, except for path separators (in case file path globbing has been selected). It is the same as **.\*** in full regexps. |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[abc]**  | Matches one character given in the bracket.                                                                                                                   |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[a-c]**  | Matches one character from the range given in the bracket.                                                                                                    |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[!abc]** | Matches one character that is not given in the bracket. It is the same as **[^abc]** in full regexp.                                                          |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[!a-c]** | Matches one character that is not from the range given in the bracket. It is the same as **[^a-c]** in full regexp.                                           |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** For historical reasons, a backslash (\\) character is *not* an escape char in this context. In order to match one of the special characters, place it in square brackets (for example, ``[?]``).

More information about the implementation can be found in:

* `The Wikipedia Glob article <https://en.wikipedia.org/wiki/Glob_(programming)>`_

* ``man 7 glob``

By default, the returned regular expression is fully anchored. In other words, there is no need of calling :sip:ref:`~PyQt6.QtCore.QRegularExpression.anchoredPattern` again on the result. To get a regular expression that is not anchored, pass :sip:ref:`~PyQt6.QtCore.QRegularExpression.WildcardConversionOption.UnanchoredWildcardConversion` in the conversion *options*.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpression.escape`.
