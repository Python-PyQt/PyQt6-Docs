.. sip:method-description::
    :status: todo
    :pysig: 5dc0d8d7ed8f48ef9bfdc2c628b1c5b0
    :realsig: (const QSize&,qreal,QIcon::Mode,QIcon::State) const
    :digest: bdd46ed936f0151fe6206d0cef90ebc4

Returns a pixmap with the requested *size*, *devicePixelRatio*, *mode*, and *state*, generating one with the given *mode* and *state* if necessary. The pixmap might be smaller than requested, but never larger, unless the device-pixel ratio of the returned pixmap is larger than 1.

**Note:** The requested devicePixelRatio might not match the returned one. This delays the scaling of the :sip:ref:`~PyQt6.QtGui.QPixmap` until it is drawn later on.

**Note:** Prior to Qt 6.8 this function wronlgy passed the device dependent pixmap size to :sip:ref:`~PyQt6.QtGui.QIconEngine.scaledPixmap`, since Qt 6.8 it's the device independent size (not scaled with the *devicePixelRatio*).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.actualSize`, :sip:ref:`~PyQt6.QtGui.QIcon.paint`.
