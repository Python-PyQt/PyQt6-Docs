.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 2d7c5d45366c60a3c72b5260ddeb8cc4

Returns ``true`` if the brush is fully opaque otherwise false. A brush is considered opaque if:

* The alpha component of the :sip:ref:`~PyQt6.QtGui.QBrush.color` is 255.

* Its :sip:ref:`~PyQt6.QtGui.QBrush.texture` does not have an alpha channel and is not a `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_.

* The colors in the :sip:ref:`~PyQt6.QtGui.QBrush.gradient` all have an alpha component that is 255.

* It is an extended radial gradient.
