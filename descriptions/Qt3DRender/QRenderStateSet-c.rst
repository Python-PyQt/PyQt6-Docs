.. sip:class-description::
    :status: todo
    :brief: FrameGraph node offers a way of specifying a set of QRenderState objects to be applied during the execution of a framegraph branch
    :realname: Qt3DRender::QRenderStateSet
    :digest: 5eb2422977f4c8620405094e0d6b4582

The :sip:ref:`~PyQt6.Qt3DRender.QRenderStateSet` FrameGraph node offers a way of specifying a set of QRenderState objects to be applied during the execution of a framegraph branch.

States set on a :sip:ref:`~PyQt6.Qt3DRender.QRenderStateSet` are set globally, contrary to the per-material states that can be set on a QRenderPass. By default, an empty :sip:ref:`~PyQt6.Qt3DRender.QRenderStateSet` will result in all render states being disabled when executed. Adding a QRenderState state explicitly enables that render state at runtime.

The `RenderStateSet <https://doc.qt.io/qt-6/qml-qt3d-render-renderstateset.html>`_ is enabled when added to the active frame graph:

::

    // using namespace Qt3DRender;

    Qt3DCore::QEntity *rootEntity = new Qt3DCore::QEntity();

    QRenderSettings *renderSettings = new QRenderSettings();

    QViewport *viewport = new QViewport();
    QCameraSelector *cameraSelector = new QCameraSelector(viewport);

    QClearBuffers *clearBuffers = new QClearBuffers(cameraSelector);
    clearBuffers->setBuffers(QClearBuffers::ColorDepthBuffer);

    QRenderStateSet *renderStateSet = new QRenderStateSet(cameraSelector);
    QCullFace *cullFace = new QCullFace(renderStateSet);
    cullFace->setMode(QCullFace::Front);
    renderStateSet->addRenderState(cullFace);

    renderSettings->setActiveFrameGraph(viewport);

    rootEntity->addComponent(renderSettings);

.. seealso:: QRenderState, QRenderPass.
