:orphan:

.. sip:class:: PyQt6.QtQuick.QSGMaterialShader
    :description: QtQuick/QSGMaterialShader-c.rst

    .. sip:enum:: PyQt6.QtQuick.QSGMaterialShader.Flag
        :description: QtQuick/QSGMaterialShader-Flag-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGMaterialShader.Flag.UpdatesGraphicsPipelineState
            :description: QtQuick/QSGMaterialShader-Flag-UpdatesGraphicsPipelineState-v.rst

    .. sip:enum:: PyQt6.QtQuick.QSGMaterialShader.Stage
        :description: QtQuick/QSGMaterialShader-Stage-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGMaterialShader.Stage.FragmentStage
            :description: QtQuick/QSGMaterialShader-Stage-FragmentStage-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGMaterialShader.Stage.VertexStage
            :description: QtQuick/QSGMaterialShader-Stage-VertexStage-v.rst

    .. sip:method:: PyQt6.QtQuick.QSGMaterialShader.__init__
        :description: QtQuick/QSGMaterialShader-__init__-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGMaterialShader.combinedImageSamplerCount
        :args:
            int
        :returns:
            int
        :description: QtQuick/QSGMaterialShader-combinedImageSamplerCount-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGMaterialShader.flags
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.Flag`
        :description: QtQuick/QSGMaterialShader-flags-f-1.rst

    .. sip:method:: PyQt6.QtQuick.QSGMaterialShader.setFlag
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.Flag`
            on: bool = True
        :description: QtQuick/QSGMaterialShader-setFlag-f-1.rst

    .. sip:method:: PyQt6.QtQuick.QSGMaterialShader.setFlags
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.Flag`
        :description: QtQuick/QSGMaterialShader-setFlags-f-1.rst

    .. sip:method:: PyQt6.QtQuick.QSGMaterialShader.setShaderFileName
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.Stage`
            Optional[str]
        :description: QtQuick/QSGMaterialShader-setShaderFileName-f-1.rst

    .. sip:method:: PyQt6.QtQuick.QSGMaterialShader.setShaderFileName
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.Stage`
            Optional[str]
            int
        :description: QtQuick/QSGMaterialShader-setShaderFileName-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGMaterialShader.updateGraphicsPipelineState
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.RenderState`
            :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.GraphicsPipelineState`
            :sip:ref:`~PyQt6.QtQuick.QSGMaterial`
            :sip:ref:`~PyQt6.QtQuick.QSGMaterial`
        :returns:
            bool
        :description: QtQuick/QSGMaterialShader-updateGraphicsPipelineState-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGMaterialShader.updateSampledImage
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.RenderState`
            int
            :sip:ref:`~PyQt6.QtQuick.QSGMaterial`
            :sip:ref:`~PyQt6.QtQuick.QSGMaterial`
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGTexture`
        :description: QtQuick/QSGMaterialShader-updateSampledImage-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGMaterialShader.updateUniformData
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.RenderState`
            :sip:ref:`~PyQt6.QtQuick.QSGMaterial`
            :sip:ref:`~PyQt6.QtQuick.QSGMaterial`
        :returns:
            bool
        :description: QtQuick/QSGMaterialShader-updateUniformData-f.rst
