:orphan:

.. sip:class:: PyQt6.Qt3DCore.QBuffer
    :inherits: :sip:ref:`~PyQt6.Qt3DCore.QNode`
    :description: Qt3DCore/QBuffer-c.rst

    .. sip:enum:: PyQt6.Qt3DCore.QBuffer.AccessType
        :description: Qt3DCore/QBuffer-AccessType-e.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.AccessType.Read
            :description: Qt3DCore/QBuffer-AccessType-Read-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.AccessType.ReadWrite
            :description: Qt3DCore/QBuffer-AccessType-ReadWrite-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.AccessType.Write
            :description: Qt3DCore/QBuffer-AccessType-Write-v.rst

    .. sip:enum:: PyQt6.Qt3DCore.QBuffer.UsageType
        :description: Qt3DCore/QBuffer-UsageType-e.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.UsageType.DynamicCopy
            :description: Qt3DCore/QBuffer-UsageType-DynamicCopy-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.UsageType.DynamicDraw
            :description: Qt3DCore/QBuffer-UsageType-DynamicDraw-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.UsageType.DynamicRead
            :description: Qt3DCore/QBuffer-UsageType-DynamicRead-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.UsageType.StaticCopy
            :description: Qt3DCore/QBuffer-UsageType-StaticCopy-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.UsageType.StaticDraw
            :description: Qt3DCore/QBuffer-UsageType-StaticDraw-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.UsageType.StaticRead
            :description: Qt3DCore/QBuffer-UsageType-StaticRead-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.UsageType.StreamCopy
            :description: Qt3DCore/QBuffer-UsageType-StreamCopy-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.UsageType.StreamDraw
            :description: Qt3DCore/QBuffer-UsageType-StreamDraw-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QBuffer.UsageType.StreamRead
            :description: Qt3DCore/QBuffer-UsageType-StreamRead-v.rst

    .. sip:method:: PyQt6.Qt3DCore.QBuffer.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DCore/QBuffer-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QBuffer.accessType
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QBuffer.AccessType`
        :description: Qt3DCore/QBuffer-accessType-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QBuffer.data
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DCore/QBuffer-data-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QBuffer.setAccessType
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QBuffer.AccessType`
        :description: Qt3DCore/QBuffer-setAccessType-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QBuffer.setData
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: Qt3DCore/QBuffer-setData-f-1.rst

    .. sip:method:: PyQt6.Qt3DCore.QBuffer.setUsage
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QBuffer.UsageType`
        :description: Qt3DCore/QBuffer-setUsage-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QBuffer.updateData
        :args:
            int
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: Qt3DCore/QBuffer-updateData-f-1.rst

    .. sip:method:: PyQt6.Qt3DCore.QBuffer.usage
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QBuffer.UsageType`
        :description: Qt3DCore/QBuffer-usage-f.rst

    .. sip:signal:: PyQt6.Qt3DCore.QBuffer.accessTypeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QBuffer.AccessType`
        :description: Qt3DCore/QBuffer-accessTypeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QBuffer.dataAvailable
        :description: Qt3DCore/QBuffer-dataAvailable-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QBuffer.dataChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: Qt3DCore/QBuffer-dataChanged-s-1.rst

    .. sip:signal:: PyQt6.Qt3DCore.QBuffer.usageChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QBuffer.UsageType`
        :description: Qt3DCore/QBuffer-usageChanged-s.rst
