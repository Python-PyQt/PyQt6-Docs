.. sip:method-description::
    :status: todo
    :pysig: 6d9e86d6265c094209e963eda0bdf7eb
    :realsig: (int,QSize,QPdfDocumentRenderOptions)
    :digest: 82821c949c112644bef105ba472b5c01

Renders the *page* into a :sip:ref:`~PyQt6.QtGui.QImage` of size *imageSize* according to the provided *renderOptions*.

Returns the rendered page or an empty image in case of an error.

Note: If the *imageSize* does not match the aspect ratio of the page in the PDF document, the page is rendered scaled, so that it covers the complete *imageSize*.
