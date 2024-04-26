.. sip:method-description::
    :status: todo
    :pysig: e09cdfe938d3fdbbc78159a3b275f7b5
    :realsig: (QQuick3DGeometry::Attribute::Semantic,int,QQuick3DGeometry::Attribute::ComponentType)
    :digest: e3b0e0dbb47e604bc9e75cf61a83f330

Adds vertex attribute description. Each attribute has a *semantic*, which specifies the usage of the attribute and the number of components it has, an *offset* from the beginning to the vertex to the attribute location inside a vertex and a *componentType* specifying the datatype and size of the attribute.

The semantic can be one of the following:

+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Constant               | Description                                                                                                                                      |
+========================+==================================================================================================================================================+
| PositionSemantic       | The attribute is a position. 3 components: *x*, *y*, and *z*                                                                                     |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| NormalSemantic         | The attribute is a normal vector. 3 components: *x*, *y*, and *z*                                                                                |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| TexCoord0Semantic      | The attribute is a texture coordinate. 2 components: *u* and *v*                                                                                 |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| TexCoord1Semantic      | The attribute is a texture coordinate. 2 components: *u* and *v*                                                                                 |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| TangentSemantic        | The attribute is a tangent vector. 3 components: *x*, *y*, and *z*                                                                               |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| BinormalSemantic       | The attribute is a binormal vector. 3 components: *x*, *y*, and *z*                                                                              |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| JointSemantic          | The attribute is a joint index vector for `skinning <https://doc.qt.io/qt-6/quick3d-vertex-skinning.html>`_. 4 components: joint index 1-4       |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| WeightSemantic         | The attribute is a weight vector for `skinning <https://doc.qt.io/qt-6/quick3d-vertex-skinning.html>`_. 4 components: joint weight 1-4           |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ColorSemantic          | The attribute is a vertex color vector. 4 components: *r*, *g*, *b*, and *a*                                                                     |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| TargetPositionSemantic | The attribute is a position for the first `morph target <https://doc.qt.io/qt-6/quick3d-morphing.html>`_. 3 components: *x*, *y*, and *z*        |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| TargetNormalSemantic   | The attribute is a normal vector for the first `morph target <https://doc.qt.io/qt-6/quick3d-morphing.html>`_. 3 components: *x*, *y*, and *z*   |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| TargetTangentSemantic  | The attribute is a tangent vector for the first `morph target <https://doc.qt.io/qt-6/quick3d-morphing.html>`_. 3 components: *x*, *y*, and *z*  |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| TargetBinormalSemantic | The attribute is a binormal vector for the first `morph target <https://doc.qt.io/qt-6/quick3d-morphing.html>`_. 3 components: *x*, *y*, and *z* |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

In addition, *semantic* can be ``IndexSemantic``. In this case the attribute does not represent an entry in the vertex buffer, but rather describes the index data in the index buffer. Since there is always just one index per vertex, *offset* makes no sense for the index buffer, and should be left at zero.

The component type can be one of the following:

+----------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Constant | Description                                                                                                                                 |
+==========+=============================================================================================================================================+
| U16Type  | The index component type is unsigned 16-bit integer. Only supported for ``IndexSemantic``.                                                  |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------+
| U32Type  | The attribute (or index component) is an unsigned 32-bit integer.                                                                           |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------+
| I32Type  | The attribute is a signed 32-bit integer. Be aware that old OpenGL versions (such as, 2.1 or OpenGL ES 2.0) may not support this data type. |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------+
| F32Type  | The attribute is a single-precision float.                                                                                                  |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** The joint index data is typically ``I32Type``. ``F32Type`` is also supported in order to enable functioning with APIs, such as OpenGL ES 2.0, that do not support integer vertex input attributes.

**Note:** For index data (``IndexSemantic``) only U16Type and U32Type are sensible and supported.

**Note:** TargetXXXSemantics will be deprecated. :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry.addTargetAttribute` can be used for the morph targets. Now these semantics are just supported for backward compatibility. If they are mixed-used with :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry.addTargetAttribute` and :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry.setTargetData`, the result cannot be quaranteed.
