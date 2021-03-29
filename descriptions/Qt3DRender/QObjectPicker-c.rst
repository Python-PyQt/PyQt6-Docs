.. sip:class-description::
    :status: todo
    :brief: Instantiates a component that can be used to interact with a QEntity by a process known as picking
    :realname: Qt3DRender::QObjectPicker
    :digest: dc109c88cf8e35cbca47406702a014d8

The :sip:ref:`~PyQt6.Qt3DRender.QObjectPicker` class instantiates a component that can be used to interact with a QEntity by a process known as picking.

For every combination of viewport and camera, picking casts a ray through the scene to find entities who's bounding volume intersects the ray. The bounding volume is computed using the values in the attribute buffer specified by the boundingVolumePositionAttribute of the geometry.

The signals :sip:ref:`~PyQt6.Qt3DRender.QObjectPicker.pressed`, :sip:ref:`~PyQt6.Qt3DRender.QObjectPicker.released`, :sip:ref:`~PyQt6.Qt3DRender.QObjectPicker.clicked`, :sip:ref:`~PyQt6.Qt3DRender.QObjectPicker.moved`, :sip:ref:`~PyQt6.Qt3DRender.QObjectPicker.entered`, and :sip:ref:`~PyQt6.Qt3DRender.QObjectPicker.exited` are emitted when the bounding volume defined by the pickAttribute property intersects with a ray.

Most signals carry a QPickEvent instance. If QPickingSettings::pickMode() is set to :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings.PickMethod.TrianglePicking`, the actual type of the pick parameter will be QPickTriangleEvent.

Pick queries are performed on mouse press and mouse release. If drag is enabled, queries also happen on each mouse move while any button is pressed. If hover is enabled, queries happen on every mouse move even if no button is pressed.

For generalised ray casting queries, see :sip:ref:`~PyQt6.Qt3DRender.QRayCaster` and :sip:ref:`~PyQt6.Qt3DRender.QScreenRayCaster`.

**Note:** Instances of this component shouldn't be shared, not respecting that condition will most likely result in undefined behavior.

**Note:** The camera far plane value affects picking and produces incorrect results due to floating-point precision if it is greater than ~100 000.

.. seealso:: :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings`, :sip:ref:`~PyQt6.Qt3DCore.QGeometry`, :sip:ref:`~PyQt6.Qt3DCore.QAttribute`, :sip:ref:`~PyQt6.Qt3DRender.QPickEvent`, :sip:ref:`~PyQt6.Qt3DRender.QPickTriangleEvent`, :sip:ref:`~PyQt6.Qt3DRender.QNoPicking`.
