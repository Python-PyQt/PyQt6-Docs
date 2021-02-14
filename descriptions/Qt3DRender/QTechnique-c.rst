.. sip:class-description::
    :status: todo
    :brief: Encapsulates a Technique
    :realname: Qt3DRender::QTechnique
    :digest: f42f9b1b6deee7f02fa05c262c2a75fd

Encapsulates a Technique.

A :sip:ref:`~PyQt6.Qt3DRender.QTechnique` specifies a set of :sip:ref:`~PyQt6.Qt3DRender.QRenderPass` objects, :sip:ref:`~PyQt6.Qt3DRender.QFilterKey` objects, :sip:ref:`~PyQt6.Qt3DRender.QParameter` objects and a :sip:ref:`~PyQt6.Qt3DRender.QGraphicsApiFilter`, which together define a rendering technique the given graphics API can render. The filter keys are used by :sip:ref:`~PyQt6.Qt3DRender.QTechniqueFilter` to select specific techniques at specific parts of the FrameGraph. If two QParameter instances with the same name are specified in a :sip:ref:`~PyQt6.Qt3DRender.QTechnique` and a QRenderPass, the one in Technique overrides the one used in the QRenderPass.

When creating an QEffect that targets several versions of a graphics API, it is useful to create several :sip:ref:`~PyQt6.Qt3DRender.QTechnique` nodes each with a :sip:ref:`~PyQt6.Qt3DRender.QTechnique.graphicsApiFilter` set to match one of the targeted GL versions. At runtime, the Qt3D renderer will select the most appropriate :sip:ref:`~PyQt6.Qt3DRender.QTechnique` based on which graphics API versions are supported and (if specified) the QFilterKey nodes that satisfy a given QTechniqueFilter in the FrameGraph.

**Note:** When using OpenGL as the graphics API for rendering, Qt3D relies on the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` returned by :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.defaultFormat` at runtime to decide what is the most appropriate GL version available. If you need to customize the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat`, do not forget to apply it with :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setDefaultFormat`. Setting the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` on the view will likely have no effect on Qt3D related rendering.

**Note:** :sip:ref:`~PyQt6.Qt3DRender.QTechnique` node can not be disabled.

::

    QTechnique *gl3Technique = new QTechnique();

    // Create the render passes
    QRenderPass *firstPass = new QRenderPass();
    QRenderPass *secondPass = new QRenderPass();

    // Add the passes to the technique
    gl3Technique->addRenderPass(firstPass);
    gl3Technique->addRenderPass(secondPass);

    // Set the targeted GL version for the technique
    gl3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    gl3Technique->graphicsApiFilter()->setMajorVersion(3);
    gl3Technique->graphicsApiFilter()->setMinorVersion(1);
    gl3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    // Create a FilterKey
    QFilterKey *filterKey = new QFilterKey();
    filterKey->setName(QStringLiteral("name"));
    fitlerKey->setValue(QStringLiteral("zFillPass"));

    // Add the FilterKey to the Technique
    gl3Technique->addFilterKey(filterKey);

    // Create a QParameter
    QParameter *colorParameter = new QParameter(QStringLiteral("color"), QColor::fromRgbF(0.0f, 0.0f, 1.0f, 1.0f));

    // Add parameter to technique
    gl3Technique->addParameter(colorParameter);

.. seealso:: QEffect, QRenderPass, QTechniqueFilter.
