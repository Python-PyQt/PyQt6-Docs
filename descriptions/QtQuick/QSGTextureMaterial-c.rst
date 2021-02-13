.. sip:class-description::
    :status: todo
    :brief: Convenient way of rendering textured geometry in the scene graph
    :digest: dffe734c3d6685c878a3ca5428a88838

The :sip:ref:`~PyQt6.QtQuick.QSGTextureMaterial` class provides a convenient way of rendering textured geometry in the scene graph.

**Warning:** This utility class is only functional when running with the default backend of the Qt Quick scenegraph.

The textured material will fill every pixel in a geometry with the supplied texture.

The geometry to be rendered with a texture material requires vertices in attribute location 0 and texture coordinates in attribute location 1. The texture coordinate is a 2-dimensional floating-point tuple. The :sip:ref:`~PyQt6.QtQuick.QSGGeometry.defaultAttributes_TexturedPoint2D` returns an attribute set compatible with this material.

The texture to be rendered can be set using setTexture(). How the texture should be rendered can be specified using setMipmapFiltering(), setFiltering(), setHorizontalWrapMode() and setVerticalWrapMode(). The rendering state is set on the texture instance just before it is bound.

The textured material respects the current matrix and the alpha channel of the texture. It will also respect the accumulated opacity in the scenegraph.

A texture material must have a texture set before it is used as a material in the scene graph.
