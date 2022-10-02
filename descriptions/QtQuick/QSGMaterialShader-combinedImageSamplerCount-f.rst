.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int) const
    :digest: d480e3ca535b48ae82df61ed43d75b15

Returns the number of elements in the combined image sampler variable at *binding*. This value is introspected from the shader code. The variable may be an array, and may have more than one dimension.

The count reflects the total number of combined image sampler items in the variable. In the following example, the count for ``srcA`` is 1, ``srcB`` is 4, and ``srcC`` is 6.

::

    layout (binding = 0) uniform sampler2D srcA;
    layout (binding = 1) uniform sampler2D srcB[4];
    layout (binding = 2) uniform sampler2D srcC[2][3];

This count is the number of :sip:ref:`~PyQt6.QtQuick.QSGTexture` pointers in the texture parameter of :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.updateSampledImage`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.updateSampledImage`.
