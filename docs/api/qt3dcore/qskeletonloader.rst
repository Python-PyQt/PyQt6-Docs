:orphan:

.. sip:class:: PyQt6.Qt3DCore.QSkeletonLoader
    :inherits: :sip:ref:`~PyQt6.Qt3DCore.QAbstractSkeleton`
    :description: Qt3DCore/QSkeletonLoader-c.rst

    .. sip:enum:: PyQt6.Qt3DCore.QSkeletonLoader.Status
        :description: Qt3DCore/QSkeletonLoader-Status-e.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QSkeletonLoader.Status.Error
            :description: Qt3DCore/QSkeletonLoader-Status-Error-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QSkeletonLoader.Status.NotReady
            :description: Qt3DCore/QSkeletonLoader-Status-NotReady-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QSkeletonLoader.Status.Ready
            :description: Qt3DCore/QSkeletonLoader-Status-Ready-v.rst

    .. sip:method:: PyQt6.Qt3DCore.QSkeletonLoader.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DCore/QSkeletonLoader-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QSkeletonLoader.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DCore/QSkeletonLoader-__init__-f-1.rst

    .. sip:method:: PyQt6.Qt3DCore.QSkeletonLoader.isCreateJointsEnabled
        :returns:
            bool
        :description: Qt3DCore/QSkeletonLoader-isCreateJointsEnabled-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QSkeletonLoader.rootJoint
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QJoint`
        :description: Qt3DCore/QSkeletonLoader-rootJoint-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QSkeletonLoader.setCreateJointsEnabled
        :args:
            bool
        :description: Qt3DCore/QSkeletonLoader-setCreateJointsEnabled-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QSkeletonLoader.setSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: Qt3DCore/QSkeletonLoader-setSource-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QSkeletonLoader.source
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: Qt3DCore/QSkeletonLoader-source-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QSkeletonLoader.status
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QSkeletonLoader.Status`
        :description: Qt3DCore/QSkeletonLoader-status-f.rst

    .. sip:signal:: PyQt6.Qt3DCore.QSkeletonLoader.createJointsEnabledChanged
        :args:
            bool
        :description: Qt3DCore/QSkeletonLoader-createJointsEnabledChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QSkeletonLoader.rootJointChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QJoint`
        :description: Qt3DCore/QSkeletonLoader-rootJointChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QSkeletonLoader.sourceChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: Qt3DCore/QSkeletonLoader-sourceChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QSkeletonLoader.statusChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QSkeletonLoader.Status`
        :description: Qt3DCore/QSkeletonLoader-statusChanged-s.rst
