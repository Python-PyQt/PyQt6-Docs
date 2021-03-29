.. sip:class-description::
    :status: todo
    :brief: Qt3DRender::QRayCaster is used to perform ray casting tests in 3d world coordinates
    :realname: Qt3DRender::QRayCaster
    :digest: a89e8fb8f0410f2cea318d5f070f327e

:sip:ref:`~PyQt6.Qt3DRender.QRayCaster` is used to perform ray casting tests in 3d world coordinates.

The 3d ray is defined by its origin, direction and length. It will be affected by the transformations applied to the entity it belongs to.

Ray casting tests will be performed every frame as long as the component is enabled. The hits property will be updated with the list of intersections.

.. seealso:: QAbstractRayCaster, QScreenRayCaster, QNoPicking.
