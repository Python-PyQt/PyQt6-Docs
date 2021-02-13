.. sip:class-description::
    :status: todo
    :brief: Convenient way of rendering solid colored geometry in the scene graph
    :digest: 755f3039cbebb9133a889d6840e23391

The :sip:ref:`~PyQt6.QtQuick.QSGFlatColorMaterial` class provides a convenient way of rendering solid colored geometry in the scene graph.

**Warning:** This utility class is only functional when running with the default backend of the Qt Quick scenegraph.

The flat color material will fill every pixel in a geometry using a solid color. The color can contain transparency.

The geometry to be rendered with a flat color material requires vertices in attribute location 0 in the :sip:ref:`~PyQt6.QtQuick.QSGGeometry` object to render correctly. The :sip:ref:`~PyQt6.QtQuick.QSGGeometry.defaultAttributes_Point2D` returns an attribute set compatible with this material.

The flat color material respects both current opacity and current matrix when updating its rendering state.
