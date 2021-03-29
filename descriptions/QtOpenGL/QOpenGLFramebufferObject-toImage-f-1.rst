.. sip:method-description::
    :status: todo
    :pysig: 5b2d154fa95ae7b9239dd76492008597
    :realsig: (bool,int) const
    :digest: 2ea07fdb9c5703dc030f7fcac274d987

This is an overloaded function.

Returns the contents of the color attachment of index *colorAttachmentIndex* of this framebuffer object as a :sip:ref:`~PyQt6.QtGui.QImage`. This method flips the image from OpenGL coordinates to raster coordinates when *flipped* is set to ``true``.

**Note:** This overload is only fully functional when multiple render targets are supported by the OpenGL implementation. When that is not the case, only one color attachment will be set up.
