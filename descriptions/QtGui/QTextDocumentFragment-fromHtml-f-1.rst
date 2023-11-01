.. sip:method-description::
    :status: todo
    :pysig: 3464aaa039253e204ec424445aa1d79b
    :realsig: (const QString&, const QTextDocument*)
    :digest: 88b9966c0e793c2233ceb76a139f1d9f

Returns a :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment` based on the arbitrary piece of HTML in the given *text*. The formatting is preserved as much as possible; for example, "<b>bold</b>" will become a document fragment with the text "bold" with a bold character format.

If the provided HTML contains references to external resources such as imported style sheets, then they will be loaded through the *resourceProvider*.
