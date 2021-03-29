.. sip:class-description::
    :status: todo
    :brief: Specifies whether front or back face culling is enabled
    :realname: Qt3DRender::QCullFace
    :digest: 3f53f01a7916fa57da3b495412689ee3

The :sip:ref:`~PyQt6.Qt3DRender.QCullFace` class specifies whether front or back face culling is enabled.

:sip:ref:`~PyQt6.Qt3DRender.QCullFace` sets whether the front or back facets are culled. Facets include triangles, quadrilaterals, polygons and rectangles.

It can be added by calling the addRenderState() method on a QRenderPass:

::

    // using namespace Qt3DRender;

    QRenderPass *renderPass = new QRenderPass();

    // Create a front face culling render state
    QCullFace *cullFront = new QCullFace();
    cullFront->setMode(QCullFace::Front);

    // Add the render state to the render pass
    renderPass->addRenderState(cullFront);

Or by calling the addRenderState() method on a QRenderStateSet:

::

    // using namespace Qt3DRender;

    QRenderStateSet *renderStateSet = new QRenderStateSet();

    // Create a front face culling render state
    QCullFace *cullFront = new QCullFace();
    cullFront->setMode(QCullFace::Front);

    // Add the render state to the render pass
    renderStateSet->addRenderState(cullFront);

.. seealso:: QFrontFace.
