.. sip:class-description::
    :status: todo
    :brief: Convenient way of rendering textured geometry in the scene graph
    :digest: fab0fdae77e2949e33ced0ed6ce2110f

The :sip:ref:`~PyQt6.QtQuick.QSGOpaqueTextureMaterial` class provides a convenient way of rendering textured geometry in the scene graph.

**Warning:** This utility class is only functional when running with the default backend of the Qt Quick scenegraph.

The opaque textured material will fill every pixel in a geometry with the supplied texture. The material does not respect the opacity of the :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.RenderState`, so opacity nodes in the parent chain of nodes using this material, have no effect.

The geometry to be rendered with an opaque texture material requires vertices in attribute location 0 and texture coordinates in attribute location 1. The texture coordinate is a 2-dimensional floating-point tuple. The :sip:ref:`~PyQt6.QtQuick.QSGGeometry.defaultAttributes_TexturedPoint2D` returns an attribute set compatible with this material.

The texture to be rendered can be set using :sip:ref:`~PyQt6.QtQuick.QSGOpaqueTextureMaterial.setTexture`. How the texture should be rendered can be specified using :sip:ref:`~PyQt6.QtQuick.QSGOpaqueTextureMaterial.setMipmapFiltering`, :sip:ref:`~PyQt6.QtQuick.QSGOpaqueTextureMaterial.setFiltering`, :sip:ref:`~PyQt6.QtQuick.QSGOpaqueTextureMaterial.setHorizontalWrapMode` and :sip:ref:`~PyQt6.QtQuick.QSGOpaqueTextureMaterial.setVerticalWrapMode`. The rendering state is set on the texture instance just before it is bound.

The opaque textured material respects the current matrix and the alpha channel of the texture. It will disregard the accumulated opacity in the scenegraph.

A texture material must have a texture set before it is used as a material in the scene graph.
