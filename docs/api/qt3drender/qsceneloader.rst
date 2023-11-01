:orphan:

.. sip:class:: PyQt6.Qt3DRender.QSceneLoader
    :inherits: :sip:ref:`~PyQt6.Qt3DCore.QComponent`
    :description: Qt3DRender/QSceneLoader-c.rst

    .. sip:enum:: PyQt6.Qt3DRender.QSceneLoader.ComponentType
        :description: Qt3DRender/QSceneLoader-ComponentType-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QSceneLoader.ComponentType.CameraLensComponent
            :description: Qt3DRender/QSceneLoader-ComponentType-CameraLensComponent-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QSceneLoader.ComponentType.GeometryRendererComponent
            :description: Qt3DRender/QSceneLoader-ComponentType-GeometryRendererComponent-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QSceneLoader.ComponentType.LightComponent
            :description: Qt3DRender/QSceneLoader-ComponentType-LightComponent-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QSceneLoader.ComponentType.MaterialComponent
            :description: Qt3DRender/QSceneLoader-ComponentType-MaterialComponent-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QSceneLoader.ComponentType.TransformComponent
            :description: Qt3DRender/QSceneLoader-ComponentType-TransformComponent-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QSceneLoader.ComponentType.UnknownComponent
            :description: Qt3DRender/QSceneLoader-ComponentType-UnknownComponent-v.rst

    .. sip:enum:: PyQt6.Qt3DRender.QSceneLoader.Status
        :description: Qt3DRender/QSceneLoader-Status-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QSceneLoader.Status.Error
            :description: Qt3DRender/QSceneLoader-Status-Error-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QSceneLoader.Status.Loading
            :description: Qt3DRender/QSceneLoader-Status-Loading-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QSceneLoader.Status.None_
            :description: Qt3DRender/QSceneLoader-Status-None_-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QSceneLoader.Status.Ready
            :description: Qt3DRender/QSceneLoader-Status-Ready-v.rst

    .. sip:method:: PyQt6.Qt3DRender.QSceneLoader.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DRender/QSceneLoader-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QSceneLoader.component
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.Qt3DRender.QSceneLoader.ComponentType`
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QComponent`
        :description: Qt3DRender/QSceneLoader-component-f-1.rst

    .. sip:method:: PyQt6.Qt3DRender.QSceneLoader.entity
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QEntity`
        :description: Qt3DRender/QSceneLoader-entity-f-1.rst

    .. sip:method:: PyQt6.Qt3DRender.QSceneLoader.entityNames
        :returns:
            List[str]
        :description: Qt3DRender/QSceneLoader-entityNames-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QSceneLoader.setSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: Qt3DRender/QSceneLoader-setSource-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QSceneLoader.source
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: Qt3DRender/QSceneLoader-source-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QSceneLoader.status
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QSceneLoader.Status`
        :description: Qt3DRender/QSceneLoader-status-f.rst

    .. sip:signal:: PyQt6.Qt3DRender.QSceneLoader.sourceChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: Qt3DRender/QSceneLoader-sourceChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QSceneLoader.statusChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QSceneLoader.Status`
        :description: Qt3DRender/QSceneLoader-statusChanged-s.rst
