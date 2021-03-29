.. sip:method-description::
    :status: todo
    :pysig: 65d6dd068a328f907829c02cdc2c0dde
    :realsig: (QQuick3DGeometry::PrimitiveType)
    :digest: ffce804d40f7d8bd97a78eb6af7d1aef

Sets the primitive type used for rendering to *type*.

+---------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Constant      | Description                                                                                                                                    |
+===============+================================================================================================================================================+
| Points        | The primitives are points.                                                                                                                     |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| LineStrip     | The primitives are lines in a strip.                                                                                                           |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Lines         | The primitives are lines in a list.                                                                                                            |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| TriangleStrip | The primitives are triangles in a strip.                                                                                                       |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| TriangleFan   | The primitives are triangles in a fan. Be aware that triangle fans may not be supported at run time, depending on the underlying graphics API. |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Triangles     | The primitives are triangles in a list.                                                                                                        |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------+

The initial value is ``Triangles``.

**Note:** Be aware that triangle fans () may not be supported at run time, depending on the underlying graphics API. For example, with Direct 3D this topology will not be functional at all.

**Note:** The point size for Points and the line width for Lines and  are controlled by the `material <https://doc.qt.io/qt-6/qml-qtquick3d-principledmaterial.html#pointSize-prop>`_. Be aware however that sizes other than 1 may not be supported at run time, depending on the underlying graphics API.

.. seealso:: :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry.primitiveType`.
