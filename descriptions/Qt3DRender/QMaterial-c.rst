.. sip:class-description::
    :status: todo
    :brief: Provides an abstract class that should be the base of all material component classes in a scene
    :realname: Qt3DRender::QMaterial
    :digest: 41289cde511d445600c268aeefa8dcb2

Provides an abstract class that should be the base of all material component classes in a scene.

:sip:ref:`~PyQt6.Qt3DRender.QMaterial` provides a way to specify the rendering of an :sip:ref:`~PyQt6.Qt3DCore.QEntity`. Any aspect can define its own subclass of :sip:ref:`~PyQt6.Qt3DRender.QMaterial` so that a Material can be used to describe a visual element; for example, the way sound should reflect off an element, the temperature of a surface, and so on.

In itself, a :sip:ref:`~PyQt6.Qt3DRender.QMaterial` doesn't do anything. It's only when it references a QEffect node that a :sip:ref:`~PyQt6.Qt3DRender.QMaterial` becomes useful.

In practice, it often happens that a single QEffect is being referenced by several :sip:ref:`~PyQt6.Qt3DRender.QMaterial` components. This allows to only create the effect, techniques, passes and shaders once while allowing to specify the material by adding QParameter instances.

A QParameter defined on a :sip:ref:`~PyQt6.Qt3DRender.QMaterial` is overridden by a QParameter (of the same name) defined in a QTechniqueFilter or a QRenderPassFilter.

::

    QMaterial *material1 = new QMaterial();
    QMaterial *material2 = new QMaterial();

    // Create effect, technique, render pass and shader
    QEffect *effect = new QEffect();
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

    // Set the effect on the materials
    material1->setEffect(effect);
    material2->setEffect(effect);

    // Set different parameters on the materials
    const QString parameterName = QStringLiteral("color");
    material1->addParameter(new QParameter(parameterName, QColor::fromRgbF(0.0f, 1.0f, 0.0f, 1.0f);
    material2->addParameter(new QParameter(parameterName, QColor::fromRgbF(1.0f, 1.0f, 1.0f, 1.0f);

.. seealso:: QEffect, QTechnique, QParameter.
