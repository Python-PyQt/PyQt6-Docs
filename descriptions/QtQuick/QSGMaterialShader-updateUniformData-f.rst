.. sip:method-description::
    :status: todo
    :pysig: f42419c96c762e3fff05df0a51021ae5
    :realsig: (QSGMaterialShader::RenderState&,QSGMaterial*,QSGMaterial*)
    :digest: 1cb591e91e68fba3e86cba117904d524

This function is called by the scene graph to get the contents of the shader program's uniform buffer updated. The implementation is not expected to perform any real graphics operations, it is merely responsible for copying data to the :sip:ref:`~PyQt6.QtCore.QByteArray` returned from :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.RenderState.uniformData`. The scene graph takes care of making that buffer visible in the shaders.

The current rendering *state* is passed from the scene graph. If the state indicates that any relevant state is dirty, the implementation must update the appropriate region in the buffer data that is accessible via :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.RenderState.uniformData`. When a state, such as, matrix or opacity, is not dirty, there is no need to touch the corresponding region since the data is persistent.

The return value must be ``true`` whenever any change was made to the uniform data.

The subclass specific state, such as the color of a flat color material, should be extracted from *newMaterial* to update the relevant regions in the buffer accordingly.

*oldMaterial* can be used to minimize buffer changes (which are typically memcpy calls) when updating material states. When *oldMaterial* is null, this shader was just activated.
