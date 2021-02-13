.. sip:enum-description::
    :status: todo
    :digest: 63fb591ad9369769c4fee4ee9496d399

The following image formats are available in Qt. See the notes after the table.

**Note:** Drawing into a :sip:ref:`~PyQt6.QtGui.QImage` with  is not supported.

**Note:** Avoid most rendering directly to most of these formats using :sip:ref:`~PyQt6.QtGui.QPainter`. Rendering is best optimized to the ``Format_RGB32`` and ``Format_ARGB32_Premultiplied`` formats, and secondarily for rendering to the ``Format_RGB16``, ``Format_RGBX8888``, ``Format_RGBA8888_Premultiplied``, ``Format_RGBX64`` and ``Format_RGBA64_Premultiplied`` formats

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.format`, :sip:ref:`~PyQt6.QtGui.QImage.convertToFormat`.
