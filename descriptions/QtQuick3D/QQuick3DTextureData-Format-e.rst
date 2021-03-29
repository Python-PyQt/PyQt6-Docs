.. sip:enum-description::
    :status: todo
    :digest: af10e0a613941281c7d2aa981c6676f0

Returns the color format of the texture data assigned in :sip:ref:`~PyQt6.QtQuick3D.QQuick3DTextureData.textureData` property.

**Note:** With the exception of ``RGBA8``, not every format is supported at runtime as this depends on which backend is being used as well which hardware is being used.

**Note:** ``RGBE`` is internally represented as an ``RGBA8`` but is intepreted as described when used as a lightProbe or skybox texture.

**Note:** Using the value ``None`` will assume the default value of ``RGBA8``
