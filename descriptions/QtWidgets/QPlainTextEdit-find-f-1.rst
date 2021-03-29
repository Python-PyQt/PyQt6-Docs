.. sip:method-description::
    :status: todo
    :pysig: 5eeb452c08aeeb1be8587dfbd7ec8a21
    :realsig: (const QRegularExpression&,QTextDocument::FindFlags)
    :digest: 93cab24d1d603aae65dfec8498f42906

This is an overloaded function.

Finds the next occurrence, matching the regular expression, *exp*, using the given *options*. The :sip:ref:`~PyQt6.QtGui.QTextDocument.FindFlags.FindCaseSensitively` option is ignored for this overload, use :sip:ref:`~PyQt6.QtCore.QRegularExpression.PatternOptions.CaseInsensitiveOption` instead.

Returns ``true`` if a match was found and changes the cursor to select the match; otherwise returns ``false``.
