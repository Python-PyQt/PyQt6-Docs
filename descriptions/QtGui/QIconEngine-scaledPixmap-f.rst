.. sip:method-description::
    :status: todo
    :pysig: adeb7cb8398528142f99c0fbb08aac29
    :realsig: (const QSize&,QIcon::Mode,QIcon::State,qreal)
    :digest: aba4b1bf72fe11f3f09315bbe619953d

Returns a pixmap for the given *size*, *mode*, *state* and *scale*.

The *scale* argument is typically equal to the `device pixel ratio <https://doc.qt.io/qt-6/qtquick-visualcanvas-adaptations-software.html#high-dpi>`_ of the display. The size is given in device-independent pixels.

**Note:** If the icon engine does not reimplement this function, the actual work is done by the virtual_hook() method, hence this method depends on icon engine support and may not work with all icon engines.

**Note:** Some engines may cast *scale* to an integer.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIconEngine.ScaledPixmapArgument`.
