.. sip:class-description::
    :status: todo
    :brief: Can be used to override the bounding volume of an entity
    :realname: Qt3DCore::QBoundingVolume
    :digest: d1e1177bcbc34676f603e69cd630172e

can be used to override the bounding volume of an entity.

An entity's bounding volume is used for many operations such as picking or view frustum culling. It is normally computed by traversing the rendered geometry.

:sip:ref:`~PyQt6.Qt3DCore.QBoundingVolume` can be used when the extent of the geometry is known to the application so that Qt 3D does not have to compute it.

A bounding volume can be provided either as minimum and maximum extent coordinates, or a separate, usually simpler, geometry that approximates the rendered mesh.

When using minimum and maximum extents, these are considered to be the opposite corners of an axis aligned bounding box, in the geometry's local coordinate system.

:sip:ref:`~PyQt6.Qt3DCore.QBoundingVolume` can also be used to query the computed bounding volume of a `GeometryView <https://doc.qt.io/qt-6/qt3drender-geometry.html#geometryview>`_. The :sip:ref:`~PyQt6.Qt3DCore.QBoundingVolume.implicitMinPoint` and :sip:ref:`~PyQt6.Qt3DCore.QBoundingVolume.implicitMaxPoint` properties will be updated if the geometry changes. Note that this is done asynchronously on a background thread so you should check the value of implicitPointsValid before reading them.

You can force the implicit extents to be updated by calling :sip:ref:`~PyQt6.Qt3DCore.QBoundingVolume.updateImplicitBounds`. This will block on the calling thread until the results are available.

**Note:** `GeometryRenderer <https://doc.qt.io/qt-6/qt3drender-geometry.html#geometryrenderer>`_ inherits `BoundingVolume <https://doc.qt.io/qt-6/qml-qt3d-core-boundingvolume.html>`_ and thus supports reading implicit bounds or setting explicit bounds also.
