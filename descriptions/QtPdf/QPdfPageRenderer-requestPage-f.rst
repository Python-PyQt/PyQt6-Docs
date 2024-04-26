.. sip:method-description::
    :status: todo
    :pysig: ef79cda67b31dbb99d947c5c346f5d02
    :realsig: (int,QSize,QPdfDocumentRenderOptions)
    :digest: ce20e971740bc63306521f5855d28572

Requests the renderer to render the page *pageNumber* into a :sip:ref:`~PyQt6.QtGui.QImage` of size *imageSize* according to the provided *options*.

Once the rendering is done the pageRendered() signal is emitted with the result as parameters.

The return value is an ID that uniquely identifies the render request. If a request with the same parameters is still in the queue, the ID of that queued request is returned.
