.. sip:method-description::
    :status: todo
    :pysig: b7889c66a16f0ef536c962e011e6640d
    :realsig: (const QList<QImage*>&)
    :digest: 93f1a95a843ba12ee8aa9135ac403bb0

Creates a new texture data array from an array of *images* and sets it as :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.textureData` for this volume object. The texture dimensions are also set according to image and array dimensions. All of the images in the array must be the same size. If the images are not all in the :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Indexed8` format, all texture data will be converted into the :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_ARGB32` format. If the images are in the :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Indexed8` format, the :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.colorTable` value for the entire volume will be taken from the first image.

Returns a pointer to the newly created array.

.. seealso:: :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.textureData`, :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.textureWidth`, :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.textureHeight`, :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.textureDepth`, :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.setTextureFormat`.
