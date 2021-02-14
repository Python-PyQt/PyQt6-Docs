.. sip:class-description::
    :status: todo
    :brief: Enable frustum culling for the FrameGraph
    :realname: Qt3DRender::QFrustumCulling
    :digest: 908b2bad35d799f9aa582a1d40b2d042

Enable frustum culling for the FrameGraph.

A :sip:ref:`~PyQt6.Qt3DRender.QFrustumCulling` class enables frustum culling of the drawable entities based on the camera view and QGeometry bounds of the entities. If :sip:ref:`~PyQt6.Qt3DRender.QFrustumCulling` is present in the FrameGraph, only the entities whose QGeometry bounds intersect with the camera frustum, i.e. the view of the camera, are drawn. If :sip:ref:`~PyQt6.Qt3DRender.QFrustumCulling` is not present, all drawable entities will be drawn. The camera is selected by a QCameraSelector frame graph node in the current hierarchy. Frustum culling can save a lot of GPU processing time when the rendered scene is complex.

.. seealso:: QCameraSelector.
