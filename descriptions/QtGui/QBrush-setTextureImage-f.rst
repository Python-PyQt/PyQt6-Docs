.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: (const QImage&)
    :digest: 111e8fb08a0b747dcc813458d0000dae

Sets the brush image to *image*. The style is set to :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.TexturePattern`.

Note the current brush color will *not* have any affect on monochrome images, as opposed to calling :sip:ref:`~PyQt6.QtGui.QBrush.setTexture` with a `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_. If you want to change the color of monochrome image brushes, either convert the image to `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ with ``QBitmap::fromImage()`` and set the resulting `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ as a texture, or change the entries in the color table for the image.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QBrush.textureImage`, :sip:ref:`~PyQt6.QtGui.QBrush.setTexture`.
