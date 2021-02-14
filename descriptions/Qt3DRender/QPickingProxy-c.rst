.. sip:class-description::
    :status: todo
    :brief: Can be used to provide an alternate QGeometryView used only for picking
    :realname: Qt3DRender::QPickingProxy
    :digest: 8345ebd7eb41498cfcc527680956e132

Can be used to provide an alternate QGeometryView used only for picking.

Picking can be an expensive operation, especially if the mesh has a lot of vertices. QPickProxy can be used to provide an alternative geometry, usually with fewer primitives, which will be used for picking, while the `GeometryRenderer <https://doc.qt.io/qt-6/qt3drender-geometry.html#geometryrenderer>`_ instance will be used for rendering.

**Note:** Do not use a :sip:ref:`~PyQt6.Qt3DRender.QPickingProxy` if the application requires picking coordinates to match the rendered mesh.

**Note:** The picking algorithm uses a bounding volume hierarchy to optimize out entities who's bounding volume does not intersect the picking ray. For that hierarchy, the bounding volume of the renderered entity is used (or one explicitly set using a QBoundingVolume component) will be used rather than the one of the proxy.
