.. sip:class-description::
    :status: todo
    :brief: Convenient way of rendering per-vertex colored geometry in the scene graph
    :digest: fbc8914276edf1282b40877c04ef04bc

The :sip:ref:`~PyQt6.QtQuick.QSGVertexColorMaterial` class provides a convenient way of rendering per-vertex colored geometry in the scene graph.

**Warning:** This utility class is only functional when running with the default backend of the Qt Quick scenegraph.

The vertex color material will give each vertex in a geometry a color. Pixels between vertices will be linearly interpolated. The colors can contain transparency.

The geometry to be rendered with vertex color must have the following layout. Attribute position 0 must contain vertices. Attribute position 1 must contain colors, a tuple of 4 values with RGBA layout. Both floats in the range of 0 to 1 and unsigned bytes in the range 0 to 255 are valid for the color values.

**Note:** The rendering pipeline expects pixels with premultiplied alpha.

:sip:ref:`~PyQt6.QtQuick.QSGGeometry.defaultAttributes_ColoredPoint2D` can be used to construct an attribute set that is compatible with this material.

The vertex color material respects both current opacity and current matrix when updating it's rendering state.
