.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: ()
    :digest: 2f842baca502a2cc7a7bc80e1540006a

Returns a pointer to the data for the uniform (constant) buffer in the shader. Uniform data must only be updated from :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.updateUniformData`. The return value is null in the other reimplementable functions, such as, :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.updateSampledImage`.

**Note:** It is strongly recommended to declare the uniform block with ``std140`` in the shader, and to carefully study the standard uniform block layout as described in section 7.6.2.2 of the OpenGL specification. It is up to the :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` implementation to ensure data gets placed at the right location in this :sip:ref:`~PyQt6.QtCore.QByteArray`, taking alignment requirements into account. Shader code translated to other shading languages is expected to use the same offsets for block members, even when the target language uses different packing rules by default.

**Note:** Avoid copying from C++ POD types, such as, structs, in order to update multiple members at once, unless it has been verified that the layouts of the C++ struct and the GLSL uniform block match.
