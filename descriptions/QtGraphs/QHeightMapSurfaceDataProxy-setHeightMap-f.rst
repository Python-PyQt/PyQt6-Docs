.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: (const QImage&)
    :digest: b2097ca224c76d96f0dc935c7b43d903

Replaces current data with the height map data specified by *image*.

There are several formats the *image* can be given in, but if it is not in a directly usable format, a conversion is made.

**Note:** If the result seems wrong, the automatic conversion failed and you should try converting the *image* yourself before setting it. Preferred format is :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGB32` in grayscale.

The height of the *image* is read from the red component of the pixels if the *image* is in grayscale. Otherwise it is an average calculated from the red, green, and blue components of the pixels. Using grayscale images may improve data conversion speed for large images.

Not recommended formats: all mono formats (for example :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Mono`).

The height map is resolved asynchronously. :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataProxy.arrayReset` is emitted when the data has been resolved.

.. seealso:: :sip:ref:`~PyQt6.QtGraphs.QHeightMapSurfaceDataProxy.heightMap`.
