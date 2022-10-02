.. sip:enum-description::
    :status: todo
    :digest: db84f119bdd326d3cfcd0a0388d99a3d

The following image formats are available in Qt. See the notes after the table.

**Note:** Drawing into a :sip:ref:`~PyQt6.QtGui.QImage` with QImage::Format_Indexed8 is not supported.

**Note:** Avoid most rendering directly to most of these formats using :sip:ref:`~PyQt6.QtGui.QPainter`. Rendering is best optimized to the ``Format_RGB32`` and ``Format_ARGB32_Premultiplied`` formats, and secondarily for rendering to the ``Format_RGB16``, ``Format_RGBX8888``, ``Format_RGBA8888_Premultiplied``, ``Format_RGBX64`` and ``Format_RGBA64_Premultiplied`` formats

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.format`, :sip:ref:`~PyQt6.QtGui.QImage.convertToFormat`.
