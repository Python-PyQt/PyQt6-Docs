:orphan:

.. sip:class:: PyQt6.Qt3DCore.QAspectEngine
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: Qt3DCore/QAspectEngine-c.rst

    .. sip:enum:: PyQt6.Qt3DCore.QAspectEngine.RunMode
        :description: Qt3DCore/QAspectEngine-RunMode-e.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAspectEngine.RunMode.Automatic
            :description: Qt3DCore/QAspectEngine-RunMode-Automatic-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAspectEngine.RunMode.Manual
            :description: Qt3DCore/QAspectEngine-RunMode-Manual-v.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: Qt3DCore/QAspectEngine-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.aspect
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QAbstractAspect`
        :description: Qt3DCore/QAspectEngine-aspect-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.aspects
        :returns:
            List[:sip:ref:`~PyQt6.Qt3DCore.QAbstractAspect`]
        :description: Qt3DCore/QAspectEngine-aspects-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.executeCommand
        :args:
            str
        :returns:
            Any
        :description: Qt3DCore/QAspectEngine-executeCommand-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.processFrame
        :description: Qt3DCore/QAspectEngine-processFrame-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.registerAspect
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QAbstractAspect`
        :description: Qt3DCore/QAspectEngine-registerAspect-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.registerAspect
        :args:
            str
        :description: Qt3DCore/QAspectEngine-registerAspect-f-1.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.rootEntity
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QEntity`
        :description: Qt3DCore/QAspectEngine-rootEntity-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.runMode
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QAspectEngine.RunMode`
        :description: Qt3DCore/QAspectEngine-runMode-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.setRootEntity
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QEntity`
        :description: Qt3DCore/QAspectEngine-setRootEntity-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.setRunMode
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QAspectEngine.RunMode`
        :description: Qt3DCore/QAspectEngine-setRunMode-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.unregisterAspect
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QAbstractAspect`
        :description: Qt3DCore/QAspectEngine-unregisterAspect-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAspectEngine.unregisterAspect
        :args:
            str
        :description: Qt3DCore/QAspectEngine-unregisterAspect-f-1.rst
