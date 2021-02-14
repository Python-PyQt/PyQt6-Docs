.. sip:class-description::
    :status: todo
    :brief: Responsible for handling all the QAbstractAspect subclasses that have been registered with the scene
    :realname: Qt3DCore::QAspectEngine
    :digest: f9e9304fcced6fa5a55d525b01327b7b

Responsible for handling all the QAbstractAspect subclasses that have been registered with the scene.

The Qt3D run loop is controlled by the Qt3DRender::QAspectEngine.

:sip:ref:`~PyQt6.Qt3DCore.QAbstractAspect` subclasses can be registered by calling Qt3DCore::QAspectEngine::registerAspect() which will take care of registering the aspect and in turn that will call Qt3DCore::QAbstractAspect::onRegistered();

The simulation loop is launched as soon as a root :sip:ref:`~PyQt6.Qt3DCore.QEntity` is set on the :sip:ref:`~PyQt6.Qt3DCore.QAspectEngine`. This is followed by a call to onEngineStartup() on each aspect so that they can start their simulation work.

The simulation loop is stopped when the root entity is set to Qt3DCore::QEntityPtr(). This calls onEngineShutdown() on each aspect so that they can stop performing their simulation work.

Setting a new valid root entity would restart the simulation loop again.
