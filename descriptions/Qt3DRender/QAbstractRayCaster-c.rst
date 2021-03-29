.. sip:class-description::
    :status: todo
    :brief: An abstract base class for ray casting in 3d scenes
    :realname: Qt3DRender::QAbstractRayCaster
    :digest: 9bf073f9bc063bdff437cd245e299e9d

An abstract base class for ray casting in 3d scenes.

:sip:ref:`~PyQt6.Qt3DRender.QAbstractRayCaster` is an abstract base class for casting rays into a 3d scene. :sip:ref:`~PyQt6.Qt3DRender.QAbstractRayCaster` can not be directly instantiated, but rather through its subclasses. :sip:ref:`~PyQt6.Qt3DRender.QAbstractRayCaster` specifies common properties for all ray casters, such as run mode and layer handling, while leaving the actual ray casting details to the subclasses.

Ray castings differs from picking (using :sip:ref:`~PyQt6.Qt3DRender.QObjectPicker`) in that it does not require mouse events to trigger.

By default, the instances of :sip:ref:`~PyQt6.Qt3DRender.QAbstractRayCaster` are disabled. When enabled, the specified ray will be tested for intersecting objects at every frame. The QAbstractRayCaster::hits property will be updated with the results of the ray casting, even if no objects are found.

The :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings` can be used to control the ray casting, such as which primitives are tested and how the results are returned.

Furthermore, :sip:ref:`~PyQt6.Qt3DRender.QLayer` components can be used to control how entities, or entity sub-graphs, react to ray casting.

**Note:** Components derived from :sip:ref:`~PyQt6.Qt3DRender.QAbstractRayCaster` should not be shared amount multiple entities.

.. seealso:: :sip:ref:`~PyQt6.Qt3DRender.QRayCaster`, :sip:ref:`~PyQt6.Qt3DRender.QScreenRayCaster`, :sip:ref:`~PyQt6.Qt3DRender.QObjectPicker`, :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings`, :sip:ref:`~PyQt6.Qt3DRender.QNoPicking`.
