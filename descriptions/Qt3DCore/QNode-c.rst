.. sip:class-description::
    :status: todo
    :brief: The base class of all Qt3D node classes used to build a Qt3D scene
    :realname: Qt3DCore::QNode
    :digest: 9bc8d991cafa6f553d291b9e4b308633

:sip:ref:`~PyQt6.Qt3DCore.QNode` is the base class of all Qt3D node classes used to build a Qt3D scene.

The owernship of :sip:ref:`~PyQt6.Qt3DCore.QNode` is determined by the :sip:ref:`~PyQt6.QtCore.QObject` parent/child relationship between nodes. By itself, a :sip:ref:`~PyQt6.Qt3DCore.QNode` has no visual appearance and no particular meaning, it is there as a way of building a node based tree structure.

The parent of a :sip:ref:`~PyQt6.Qt3DCore.QNode` instance can only be another :sip:ref:`~PyQt6.Qt3DCore.QNode` instance.

Each :sip:ref:`~PyQt6.Qt3DCore.QNode` instance has a unique id that allows it to be recognizable from other instances.

When properties are defined on a :sip:ref:`~PyQt6.Qt3DCore.QNode` subclass, their NOTIFY signal will automatically generate notifications that the Qt3D backend aspects will receive.

.. seealso:: QEntity, QComponent.
