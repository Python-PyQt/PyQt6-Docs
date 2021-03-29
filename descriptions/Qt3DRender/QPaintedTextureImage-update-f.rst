.. sip:method-description::
    :status: todo
    :pysig: 773223d7a97bc727764204f49d6f1d58
    :realname: Qt3DRender::QPaintedTextureImage::update
    :realsig: (const QRect&)
    :digest: e0ce5f8b96552ccdeff1faa7439ed728

Immediately triggers the painted texture's :sip:ref:`~PyQt6.Qt3DRender.QPaintedTextureImage.paint` function, which in turn uploads the new image to the GPU. If you are making multiple changes to a painted texture, consider waiting until all changes are complete before calling update, in order to minimize the number of repaints required.

Parameter *rect* is currently unused.
