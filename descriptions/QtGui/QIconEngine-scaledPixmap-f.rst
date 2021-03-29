.. sip:method-description::
    :status: todo
    :pysig: adeb7cb8398528142f99c0fbb08aac29
    :realsig: (const QSize&,QIcon::Mode,QIcon::State,qreal)
    :digest: f7ef27056e7affb1675aa27cb3c6abc9

Returns a pixmap for the given *size*, *mode*, *state* and *scale*.

The *scale* argument is typically equal to the device pixel ratio of the display.

**Note:** This is a helper method and the actual work is done by the virtual_hook() method, hence this method depends on icon engine support and may not work with all icon engines.

**Note:** Some engines may cast *scale* to an integer.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIconEngine.ScaledPixmapArgument`.
