.. sip:class-description::
    :status: todo
    :brief: Encapsulates a Render Pass
    :realname: Qt3DRender::QRenderPass
    :digest: 3ac62a9031e029d585736087b71f0a2d

Encapsulates a Render Pass.

A :sip:ref:`~PyQt6.Qt3DRender.QRenderPass` specifies a single rendering pass - an instance of shader program execution - used by :sip:ref:`~PyQt6.Qt3DRender.QTechnique`. Render pass consists of a :sip:ref:`~PyQt6.Qt3DRender.QShaderProgram` and a list of :sip:ref:`~PyQt6.Qt3DRender.QFilterKey` objects, a list of :sip:ref:`~PyQt6.Qt3DRender.QRenderState` objects and a list of :sip:ref:`~PyQt6.Qt3DRender.QParameter` objects.

:sip:ref:`~PyQt6.Qt3DRender.QRenderPass` executes the QShaderProgram using the given QRenderState and QParameter nodes when at least one of QFilterKey nodes being referenced matches any of the QFilterKey nodes in QRenderPassFilter or when no QFilterKey nodes are specified and no QRenderPassFilter is present in the FrameGraph.

If the :sip:ref:`~PyQt6.Qt3DRender.QRenderPass` defines a QParameter, it will be overridden by a QParameter with the same name if it exists in any of the QTechnique, QEffect, QMaterial, QTechniqueFilter, QRenderPassFilter associated with the pass at runtime. This still can be useful to define sane default values.

At render time, for each leaf node of the FrameGraph a base render state is recorded by accumulating states defined by all QRenderStateSet nodes in the FrameGraph branch. Each :sip:ref:`~PyQt6.Qt3DRender.QRenderPass` can overload this base render state by specifying its own QRenderState nodes.

::

    // Create the render passes
    QRenderPass *pass = new QRenderPass();

    // Create shader program
    QShaderProgram *glShader = new QShaderProgram();

    // Set the shader on the render pass
    pass->setShaderProgram(glShader);

    // Create a FilterKey
    QFilterKey *filterKey = new QFilterKey();
    filterKey->setName(QStringLiteral("name"));
    fitlerKey->setValue(QStringLiteral("zFillPass"));

    // Add the FilterKey to the pass
    pass->addFilterKey(filterKey);

    // Create a QParameter
    QParameter *colorParameter = new QParameter(QStringLiteral("color"), QColor::fromRgbF(0.0f, 0.0f, 1.0f, 1.0f));

    // Add parameter to pass
    pass->addParameter(colorParameter);

    // Create a QRenderState
    QDepthTest *depthTest = new QDepthTest();

    // Add the render state to the pass
    pass->addRenderState(depthTest);

.. seealso:: QRenderPassFilter, QFilterKey, QParameter, QRenderState, QEffect, QTechnique.
