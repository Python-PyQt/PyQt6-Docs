.. sip:class-description::
    :status: todo
    :brief: Monochrome (1-bit depth) pixmaps
    :digest: 4f847150c0ba2608fe0fc8fffd62c699

The `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ class provides monochrome (1-bit depth) pixmaps.

The `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ class is a monochrome off-screen paint device used mainly for creating custom `QCursor <https://doc.qt.io/qt-6/gui-changes-qt6.html#qcursor>`_ and :sip:ref:`~PyQt6.QtGui.QBrush` objects, constructing :sip:ref:`~PyQt6.QtGui.QRegion` objects, and for setting masks for pixmaps and widgets.

`QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ is a :sip:ref:`~PyQt6.QtGui.QPixmap` subclass ensuring a depth of 1, except for null objects which have a depth of 0. If a pixmap with a depth greater than 1 is assigned to a bitmap, the bitmap will be dithered automatically.

Use the :sip:ref:`~PyQt6.QtGui.QColor` objects :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.color0` and :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.color1` when drawing on a `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ object (or a :sip:ref:`~PyQt6.QtGui.QPixmap` object with depth 1).

Painting with :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.color0` sets the bitmap bits to 0, and painting with :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.color1` sets the bits to 1. For a bitmap, 0-bits indicate background (or transparent pixels) and 1-bits indicate foreground (or opaque pixels). Use the :sip:ref:`~PyQt6.QtGui.QBitmap.clear` function to set all the bits to :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.color0`. Note that using the :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.black` and :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.white` colors make no sense because the QColor::pixel() value is not necessarily 0 for black and 1 for white.

The `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ class provides the :sip:ref:`~PyQt6.QtGui.QBitmap.transformed` function returning a transformed copy of the bitmap; use the :sip:ref:`~PyQt6.QtGui.QTransform` argument to translate, scale, shear, and rotate the bitmap. In addition, `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ provides the static :sip:ref:`~PyQt6.QtGui.QBitmap.fromData` function which returns a bitmap constructed from the given ``uchar`` data, and the static :sip:ref:`~PyQt6.QtGui.QBitmap.fromImage` function returning a converted copy of a :sip:ref:`~PyQt6.QtGui.QImage` object.

Just like the :sip:ref:`~PyQt6.QtGui.QPixmap` class, `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ is optimized by the use of implicit data sharing. For more information, see the `Implicit Data Sharing <https://doc.qt.io/qt-6/implicit-sharing.html>`_ documentation.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap`, :sip:ref:`~PyQt6.QtGui.QImage`, :sip:ref:`~PyQt6.QtGui.QImageReader`, :sip:ref:`~PyQt6.QtGui.QImageWriter`.
