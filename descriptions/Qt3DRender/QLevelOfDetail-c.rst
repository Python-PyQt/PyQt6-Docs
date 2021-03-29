.. sip:class-description::
    :status: todo
    :brief: Way of controlling the complexity of rendered entities based on their size on the screen
    :realname: Qt3DRender::QLevelOfDetail
    :digest: d039fd9f4a4f8d2fcb36740c31b050eb

The :sip:ref:`~PyQt6.Qt3DRender.QLevelOfDetail` class provides a way of controlling the complexity of rendered entities based on their size on the screen.

:sip:ref:`~PyQt6.Qt3DRender.QLevelOfDetail` can be used to control the representation of an entity based on distance from the observer or size on the screen.

In order to improve rendering performance, objects that are very small can be rendered using far fewer details, in geometry or texture.

The component is controlled by specifying thresholds of values which are interpreted as either distances from the camera or screen size.

As the point of view changes, the :sip:ref:`~PyQt6.Qt3DRender.QLevelOfDetail.currentIndex` property will change to reflect matching value in the range array.

The :sip:ref:`~PyQt6.Qt3DRender.QLevelOfDetail.currentIndex` property can then be used, for example, to enable or disable entities, change material, etc.

The `LevelOfDetail <https://doc.qt.io/qt-6/qml-qt3d-render-levelofdetail.html>`_ component is not shareable between multiple `entities <https://doc.qt.io/qt-6/qml-qt3d-core-entity.html>`_.

::

     #include <Qt3DCore/QEntity>
     #include <Qt3DRender/QGeometryRenderer>
     #include <Qt3DRender/QLevelOfDetail>

    // Scene
    Qt3DCore::QEntity *rootEntity = new Qt3DCore::Qt3DCore::QEntity;

    Qt3DCore::QEntity *renderableEntity = new Qt3DCore::QEntity(rootEntity);
    Qt3DRender::QGeometryRenderer *geometryRenderer = new Qt3DCore::QGeometryRenderer(renderableEntity);
    renderableEntity->addComponent(geometryRenderer);
    Qt3DRender::QLevelOfDetail* lod = new Qt3Render::QLevelOfDetail(renderableEntity);
    QList<qreal> thresholds = {20, 35, 50, 65};
    lod->setThresholds(thresholds);
    lod->setCamera(mainCamera);
    renderableEntity->addComponent(lod);

    // connect to QLevelOfDetail::currentIndexChanged to toggle rendering
    ...
