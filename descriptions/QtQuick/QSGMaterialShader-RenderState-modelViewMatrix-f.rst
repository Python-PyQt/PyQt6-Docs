.. sip:method-description::
    :status: todo
    :pysig: f7702f3ac6e67cbda38e195e36b612a6
    :realsig: () const
    :digest: 0077f0bd6be9b426a40c1ecdc98a2083

Returns the model view matrix.

If the material has the RequiresFullMatrix flag set, this is guaranteed to be the complete transform matrix calculated from the scenegraph.

However, if this flag is not set, the renderer may choose to alter this matrix. For example, it may pre-transform vertices on the CPU and set this matrix to identity.

In a situation such as the above, it is still possible to retrieve the actual matrix determinant by setting the RequiresDeterminant flag in the material and calling the :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.RenderState.determinant` accessor.
