.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 5fdae370330c1524755599dc5fcf6394

Sets the stride of the vertex buffer to *stride*, measured in bytes. This is the distance between two consecutive vertices in the buffer.

For example, a tightly packed vertex buffer for a geometry using ``PositionSemantic``, ``IndexSemantic``, and ``ColorSemantic`` will have stride ``28`` (Seven floats in total: Three for position, four for color, and none for indexes, which do not go in the vertex buffer.)

.. seealso:: :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry.stride`, :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry.addAttribute`.
