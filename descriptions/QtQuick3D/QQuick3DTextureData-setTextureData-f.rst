.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: bdab61aa2da9961c18ef77179d5e4cf7

Sets the texture data. The contents of *data* must respect the :sip:ref:`~PyQt6.QtQuick3D.QQuick3DTextureData.size` and :sip:ref:`~PyQt6.QtQuick3D.QQuick3DTextureData.format` properties as the backend will try and upload and use the data as if it were a texture of size and format, and if there is any deviation the result will be somewhere between incorrect rendering of the texture, or potentially a crash.

.. seealso:: :sip:ref:`~PyQt6.QtQuick3D.QQuick3DTextureData.textureData`.
