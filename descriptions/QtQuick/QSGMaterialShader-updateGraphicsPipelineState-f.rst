.. sip:method-description::
    :status: todo
    :pysig: d47cbdd9b333af77ddf48646d5dff74a
    :realsig: (QSGMaterialShader::RenderState&,QSGMaterialShader::GraphicsPipelineState*,QSGMaterial*,QSGMaterial*)
    :digest: c3bfc403dbe08703696b8ee48ba0d10d

This function is called by the scene graph to enable the material to provide a custom set of graphics state. The set of states that are customizable by material is limited to blending and related settings.

**Note:** This function is only called when the :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.Flags.UpdatesGraphicsPipelineState` flag was enabled via :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.setFlags`. By default it is not set, and so this function is never called.

The return value must be ``true`` whenever a change was made to any of the members in *ps*.

**Note:** The contents of *ps* is not persistent between invocations of this function.

The current rendering *state* is passed from the scene graph.

The subclass specific state can be extracted from *newMaterial*. When *oldMaterial* is null, this shader was just activated.
