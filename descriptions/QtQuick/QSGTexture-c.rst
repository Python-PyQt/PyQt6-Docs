.. sip:class-description::
    :status: todo
    :brief: The base class for textures used in the scene graph
    :digest: da458ee05440fba4ffb45fa4d060fbfa

The :sip:ref:`~PyQt6.QtQuick.QSGTexture` class is the base class for textures used in the scene graph.

Users can freely implement their own texture classes to support arbitrary input textures, such as YUV video frames or 8 bit alpha masks. The scene graph provides a default implementation for RGBA textures.The default implementation is not instantiated directly, rather they are constructed via factory functions, such as :sip:ref:`~PyQt6.QtQuick.QQuickWindow.createTextureFromImage`.

With the default implementation, each :sip:ref:`~PyQt6.QtQuick.QSGTexture` is backed by a QRhiTexture, which in turn contains a native texture object, such as an OpenGL texture or a Vulkan image.

The size in pixels is given by :sip:ref:`~PyQt6.QtQuick.QSGTexture.textureSize`. :sip:ref:`~PyQt6.QtQuick.QSGTexture.hasAlphaChannel` reports if the texture contains opacity values and :sip:ref:`~PyQt6.QtQuick.QSGTexture.hasMipmaps` reports if the texture contains mipmap levels.

:sip:ref:`~PyQt6.QtQuick.QSGMaterial` that work with textures reimplement :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.updateSampledImage` to provide logic that decides which :sip:ref:`~PyQt6.QtQuick.QSGTexture`'s underlying native texture should be exposed at a given shader resource binding point.

:sip:ref:`~PyQt6.QtQuick.QSGTexture` does not separate image (texture) and sampler objects. The parameters for filtering and wrapping can be specified with :sip:ref:`~PyQt6.QtQuick.QSGTexture.setMipmapFiltering`, :sip:ref:`~PyQt6.QtQuick.QSGTexture.setFiltering`, :sip:ref:`~PyQt6.QtQuick.QSGTexture.setHorizontalWrapMode` and :sip:ref:`~PyQt6.QtQuick.QSGTexture.setVerticalWrapMode`. The scene graph and Qt's graphics abstraction takes care of creating separate sampler objects, when applicable.

.. _qsgtexture-texture-atlases:

Texture Atlases
---------------

Some scene graph backends use texture atlasses, grouping multiple small textures into one large texture. If this is the case, the function :sip:ref:`~PyQt6.QtQuick.QSGTexture.isAtlasTexture` will return true. Atlases are used to aid the rendering algorithm to do better sorting which increases performance. Atlases are also essential for batching (merging together geometry to reduce the number of draw calls), because two instances of the same material using two different QSGTextures are not batchable, whereas if both QSGTextures refer to the same atlas, batching can happen, assuming the materials are otherwise compatible.

The location of the texture inside the atlas is given with the :sip:ref:`~PyQt6.QtQuick.QSGTexture.normalizedTextureSubRect` function.

If the texture is used in such a way that atlas is not preferable, the function removedFromAtlas() can be used to extract a non-atlased copy.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.
