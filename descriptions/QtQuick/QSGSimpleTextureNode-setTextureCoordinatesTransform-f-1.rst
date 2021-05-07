.. sip:method-description::
    :status: todo
    :pysig: 931e23ab4ebcc6999191aec9f10de5c4
    :realsig: (QSGSimpleTextureNode::TextureCoordinatesTransformMode)
    :digest: 13a28380048f2781f531edc1b88b54e0

Sets the method used to generate texture coordinates to *mode*. This can be used to obtain correct orientation of the texture. This is commonly needed when using a third party OpenGL library to render to texture as OpenGL has an inverted y-axis relative to Qt Quick.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGSimpleTextureNode.textureCoordinatesTransform`.
