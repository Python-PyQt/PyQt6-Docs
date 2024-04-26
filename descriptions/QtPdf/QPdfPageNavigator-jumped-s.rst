.. sip:signal-description::
    :status: todo
    :pysig: 379a087895ab5726ed0e0a646968dbfd
    :realsig: (QPdfLink)
    :digest: 2004ac5d270a4eb15a350bf9a491caae

This signal is emitted when an abrupt jump occurs, to the *current* page index, location on the page, and zoom level; but *not* when simply scrolling through the document one page at a time. That is, :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.jump`, :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.forward` and :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.back` emit this signal, but :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.update` does not.

If ``current.rectangles.length > 0``, they are rectangles that cover a specific destination area: a search result that should be made visible; otherwise, ``current.location`` is the destination location on the ``page`` (a hyperlink destination, or during forward/back navigation).
