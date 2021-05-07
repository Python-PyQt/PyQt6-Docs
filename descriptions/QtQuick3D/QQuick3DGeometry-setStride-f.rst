.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: d53b29c8d6b488a4d45ea47cf0bb9b13

Sets the stride of the vertex buffer to *stride*, measured in bytes. This is the distance between two consecutive vertices in the buffer.

For example, a tightly packed, interleaved vertex buffer for a geometry using ``PositionSemantic``, ``IndexSemantic``, and ``ColorSemantic`` will have a stride of ``28`` (Seven floats in total: Three for position, four for color, and none for indexes, which do not go in the vertex buffer.)

**Note:** :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry` expects, and works only with, vertex data with an interleaved attribute layout.

.. seealso:: :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry.stride`, :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry.addAttribute`.
