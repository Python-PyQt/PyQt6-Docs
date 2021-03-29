.. sip:class-description::
    :status: todo
    :brief: Enable alpha-to-coverage multisampling mode
    :realname: Qt3DRender::QAlphaCoverage
    :digest: 44dfd7e7ac4a51eb55a0d8f9431985f4

Enable alpha-to-coverage multisampling mode.

A :sip:ref:`~PyQt6.Qt3DRender.QAlphaCoverage` class enables alpha-to-coverage multisampling mode. When enabled, the fragment alpha value is used as a coverage for the sample and combined with fragment coverage value. :sip:ref:`~PyQt6.Qt3DRender.QAlphaCoverage` does nothing if multisampling is disabled. Alpha-to-coverage is most useful when order independent blending is required, for example when rendering leaves, grass and other rich vegetation.

It can be added to a QRenderPass by calling QRenderPass::addRenderState():

::

    QRenderPass *renderPass = new QRenderPass();

    // Create a alpha coverage render state
    QAlphaCoverage *alphaCoverage = new QAlphaCoverage();
    QMultiSampleAntiAliasing *multiSampleAntialiasing = new QMultiSampleAntiAliasing();

    // Add the render states to the render pass
    renderPass->addRenderState(alphaCoverage);
    renderPass->addRenderState(multiSampleAntialiasing);

Or to a QRenderStateSet by calling QRenderStateSet::addRenderState():

::

    QRenderStateSet *renderStateSet = new QRenderStateSet();

    // Create a alpha coverage render state
    QAlphaCoverage *alphaCoverage = new QAlphaCoverage();
    QMultiSampleAntiAliasing *multiSampleAntialiasing = new QMultiSampleAntiAliasing();

    // Add the render states to the render state set
    renderStateSet->addRenderState(alphaCoverage);
    renderStateSet->addRenderState(multiSampleAntialiasing);

.. seealso:: :sip:ref:`~PyQt6.Qt3DRender.QMultiSampleAntiAliasing`.
