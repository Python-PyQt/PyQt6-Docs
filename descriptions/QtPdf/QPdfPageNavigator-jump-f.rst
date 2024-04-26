.. sip:method-description::
    :status: todo
    :pysig: 379a087895ab5726ed0e0a646968dbfd
    :realsig: (QPdfLink)
    :digest: 9714495ddee01bf224fa7a8aa649d704

Adds the given *destination* to the history of visited locations.

In this case, PDF views respond to the :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.jumped` signal by scrolling to place ``destination.rectangles`` in the viewport, as opposed to placing ``destination.location`` in the viewport. So it's appropriate to call this method to jump to a search result from :sip:ref:`~PyQt6.QtPdf.QPdfSearchModel` (because the rectangles cover the region of text found). To jump to a hyperlink destination, call jump(page, location, zoom) instead, because in that case the :sip:ref:`~PyQt6.QtPdf.QPdfLink` object's ``rectangles`` cover the hyperlink origin location rather than the destination.
