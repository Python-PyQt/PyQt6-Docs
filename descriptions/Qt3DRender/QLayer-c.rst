.. sip:class-description::
    :status: todo
    :brief: Way of filtering which entities will be rendered
    :realname: Qt3DRender::QLayer
    :digest: 59d3df59d4ac56471f261c3ccc4195db

The :sip:ref:`~PyQt6.Qt3DRender.QLayer` class provides a way of filtering which entities will be rendered.

:sip:ref:`~PyQt6.Qt3DRender.QLayer` works in conjunction with the :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter` in the FrameGraph.

A :sip:ref:`~PyQt6.Qt3DRender.QLayer` can be applied to a subtree of entities by setting the recursive property to true.

::

     #include <Qt3DCore/QEntity>
     #include <Qt3DRender/QGeometryRenderer>
     #include <Qt3DRender/QLayer>
     #include <Qt3DRender/QLayerFilter>
     #include <Qt3DRender/QViewport>

    // Scene
    Qt3DCore::QEntity *rootEntity = new Qt3DCore::Qt3DCore::QEntity;

    Qt3DCore::QEntity *renderableEntity = new Qt3DCore::Qt3DCore::QEntity(rootEntity);
    Qt3DRender::QGeometryRenderer *geometryRenderer = new Qt3DCore::QGeometryRenderer(renderableEntity);
    Qt3DRender::QLayer *layer1 = new Qt3DCore::QLayer(renderableEntity);
    layer1->setRecursive(true);
    renderableEntity->addComponent(geometryRenderer);
    renderableEntity->addComponent(layer1);

    ...

    // FrameGraph
    Qt3DRender::QViewport *viewport = new Qt3DRender::QViewport;
    Qt3DRender::QLayerFilter *layerFilter = new Qt3DRender::QLayerFilter(viewport);
    layerFilter->addLayer(layer1);

    ...

.. seealso:: :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter`.
