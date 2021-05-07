.. sip:class-description::
    :status: todo
    :brief: Base class for effects in a Qt 3D scene
    :realname: Qt3DRender::QEffect
    :digest: 5a360c70edb2b825390b0f5402921b3d

The base class for effects in a Qt 3D scene.

The :sip:ref:`~PyQt6.Qt3DRender.QEffect` class combines a set of techniques and parameters used by those techniques to produce a rendering effect for a material.

An :sip:ref:`~PyQt6.Qt3DRender.QEffect` instance should be shared among several QMaterial instances when possible.

**Note:** :sip:ref:`~PyQt6.Qt3DRender.QEffect` node can not be disabled.

::

    QEffect *effect = new QEffect();

    // Create technique, render pass and shader
    QTechnique *gl3Technique = new QTechnique();
    QRenderPass *gl3Pass = new QRenderPass();
    QShaderProgram *glShader = new QShaderProgram();

    // Set the shader on the render pass
    gl3Pass->setShaderProgram(glShader);

    // Add the pass to the technique
    gl3Technique->addRenderPass(gl3Pass);

    // Set the targeted GL version for the technique
    gl3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    gl3Technique->graphicsApiFilter()->setMajorVersion(3);
    gl3Technique->graphicsApiFilter()->setMinorVersion(1);
    gl3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    // Add the technique to the effect
    effect->addTechnique(gl3Technique);

A QParameter defined on a :sip:ref:`~PyQt6.Qt3DRender.QEffect` overrides parameter (of the same name) defined in QTechnique and QRenderPass, but are overridden by parameter in QRenderPassFilter, QTechniqueFilter and QMaterial.

.. seealso:: QMaterial, QTechnique, QParameter.
