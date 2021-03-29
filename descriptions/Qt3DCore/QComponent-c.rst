.. sip:class-description::
    :status: todo
    :brief: Base class of scene nodes that can be aggregated by Qt3DCore::QEntity instances as a component
    :realname: Qt3DCore::QComponent
    :digest: f9902bdc7abcb87abc51a64c53c0f517

The base class of scene nodes that can be aggregated by :sip:ref:`~PyQt6.Qt3DCore.QEntity` instances as a component.

A :sip:ref:`~PyQt6.Qt3DCore.QComponent` provides a vertical slice of behavior that can be assigned to and sometimes shared across :sip:ref:`~PyQt6.Qt3DCore.QEntity` instances.

:sip:ref:`~PyQt6.Qt3DCore.QComponent` subclasses are often aggregated in groups that impart useful behavior to the aggregating entity. For example, to have an Entity that gets drawn by the Qt3D renderer aspect, an entity would most likely aggregate :sip:ref:`~PyQt6.Qt3DCore.QTransform`, :sip:ref:`~PyQt6.Qt3DRender.QMesh`, and :sip:ref:`~PyQt6.Qt3DRender.QMaterial` components.

.. seealso:: :sip:ref:`~PyQt6.Qt3DCore.QEntity`.
