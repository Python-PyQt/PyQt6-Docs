.. sip:method-description::
    :status: todo
    :pysig: 574920ad07b505a745cfdb141ecd3aa8
    :realsig: (const QRegularExpression&,QTextDocument::FindFlags)
    :digest: 93cab24d1d603aae65dfec8498f42906

This is an overloaded function.

Finds the next occurrence, matching the regular expression, *exp*, using the given *options*. The :sip:ref:`~PyQt6.QtGui.QTextDocument.FindFlag.FindCaseSensitively` option is ignored for this overload, use :sip:ref:`~PyQt6.QtCore.QRegularExpression.PatternOption.CaseInsensitiveOption` instead.

Returns ``true`` if a match was found and changes the cursor to select the match; otherwise returns ``false``.
