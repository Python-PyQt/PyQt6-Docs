.. sip:class-description::
    :status: todo
    :brief: A QAbstractTextureImage that can be written through a QPainter
    :realname: Qt3DRender::QPaintedTextureImage
    :digest: c4bc74a2231da77c105760959a18e022

A QAbstractTextureImage that can be written through a :sip:ref:`~PyQt6.QtGui.QPainter`.

A :sip:ref:`~PyQt6.Qt3DRender.QPaintedTextureImage` provides a way to specify a texture image (and thus an OpenGL texture) through a :sip:ref:`~PyQt6.QtGui.QPainter`. The width and height of the texture image can be specified through the width and height or size properties.

A :sip:ref:`~PyQt6.Qt3DRender.QPaintedTextureImage` must be subclassed and the virtual :sip:ref:`~PyQt6.Qt3DRender.QPaintedTextureImage.paint` function implemented. Each time :sip:ref:`~PyQt6.Qt3DRender.QPaintedTextureImage.update` is called on the :sip:ref:`~PyQt6.Qt3DRender.QPaintedTextureImage`, the :sip:ref:`~PyQt6.Qt3DRender.QPaintedTextureImage.paint` function is invoked and the resulting image is uploaded.

The :sip:ref:`~PyQt6.Qt3DRender.QPaintedTextureImage` must be attached to some QAbstractTexture.
