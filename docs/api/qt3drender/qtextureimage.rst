:orphan:

.. sip:class:: PyQt6.Qt3DRender.QTextureImage
    :inherits: :sip:ref:`~PyQt6.Qt3DRender.QAbstractTextureImage`
    :description: Qt3DRender/QTextureImage-c.rst

    .. sip:enum:: PyQt6.Qt3DRender.QTextureImage.Status
        :description: Qt3DRender/QTextureImage-Status-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QTextureImage.Status.Error
            :description: Qt3DRender/QTextureImage-Status-Error-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QTextureImage.Status.Loading
            :description: Qt3DRender/QTextureImage-Status-Loading-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QTextureImage.Status.None_
            :description: Qt3DRender/QTextureImage-Status-None_-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QTextureImage.Status.Ready
            :description: Qt3DRender/QTextureImage-Status-Ready-v.rst

    .. sip:method:: PyQt6.Qt3DRender.QTextureImage.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DRender/QTextureImage-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QTextureImage.isMirrored
        :returns:
            bool
        :description: Qt3DRender/QTextureImage-isMirrored-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QTextureImage.setMirrored
        :args:
            bool
        :description: Qt3DRender/QTextureImage-setMirrored-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QTextureImage.setSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: Qt3DRender/QTextureImage-setSource-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QTextureImage.setStatus
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QTextureImage.Status`
        :description: Qt3DRender/QTextureImage-setStatus-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QTextureImage.source
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: Qt3DRender/QTextureImage-source-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QTextureImage.status
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QTextureImage.Status`
        :description: Qt3DRender/QTextureImage-status-f.rst

    .. sip:signal:: PyQt6.Qt3DRender.QTextureImage.mirroredChanged
        :args:
            bool
        :description: Qt3DRender/QTextureImage-mirroredChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QTextureImage.sourceChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: Qt3DRender/QTextureImage-sourceChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QTextureImage.statusChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QTextureImage.Status`
        :description: Qt3DRender/QTextureImage-statusChanged-s.rst
