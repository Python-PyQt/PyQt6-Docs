.. sip:method-description::
    :status: todo
    :pysig: cee98fe43dc8075e66ab581de263b9c6
    :realsig: (QSGTexture*)
    :digest: d367dd3193c50d806fc5416ef2fea225

Sets the texture of this texture node to *texture*.

Use :sip:ref:`~PyQt6.QtQuick.QSGSimpleTextureNode.setOwnsTexture` to set whether the node should take ownership of the texture. By default, the node does not take ownership.

**Warning:** A texture node must have a texture before being added to the scenegraph to be rendered.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGSimpleTextureNode.texture`.
