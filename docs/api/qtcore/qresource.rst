:orphan:

.. sip:class:: PyQt6.QtCore.QResource
    :description: QtCore/QResource-c.rst

    .. sip:enum:: PyQt6.QtCore.QResource.Compression
        :description: QtCore/QResource-Compression-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QResource.Compression.NoCompression
            :description: QtCore/QResource-Compression-NoCompression-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QResource.Compression.ZlibCompression
            :description: QtCore/QResource-Compression-ZlibCompression-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QResource.Compression.ZstdCompression
            :description: QtCore/QResource-Compression-ZstdCompression-v.rst

    .. sip:method:: PyQt6.QtCore.QResource.__init__
        :args:
            fileName: str = ''
            locale: :sip:ref:`~PyQt6.QtCore.QLocale` = QLocale()
        :description: QtCore/QResource-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.absoluteFilePath
        :returns:
            str
        :description: QtCore/QResource-absoluteFilePath-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.children
        :returns:
            List[str]
        :description: QtCore/QResource-children-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.compressionAlgorithm
        :returns:
            :sip:ref:`~PyQt6.QtCore.QResource.Compression`
        :description: QtCore/QResource-compressionAlgorithm-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.data
        :returns:
            bytes
        :description: QtCore/QResource-data-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.fileName
        :returns:
            str
        :description: QtCore/QResource-fileName-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.isDir
        :returns:
            bool
        :description: QtCore/QResource-isDir-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.isFile
        :returns:
            bool
        :description: QtCore/QResource-isFile-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.isValid
        :returns:
            bool
        :description: QtCore/QResource-isValid-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.lastModified
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QResource-lastModified-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.locale
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtCore/QResource-locale-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.registerResource
        :args:
            str
            mapRoot: str = ''
        :returns:
            bool
        :static:
        :description: QtCore/QResource-registerResource-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.registerResourceData
        :args:
            bytes
            mapRoot: str = ''
        :returns:
            bool
        :static:
        :description: QtCore/QResource-registerResourceData-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.setFileName
        :args:
            str
        :description: QtCore/QResource-setFileName-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.setLocale
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtCore/QResource-setLocale-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.size
        :returns:
            int
        :description: QtCore/QResource-size-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.uncompressedData
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QResource-uncompressedData-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.uncompressedSize
        :returns:
            int
        :description: QtCore/QResource-uncompressedSize-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.unregisterResource
        :args:
            str
            mapRoot: str = ''
        :returns:
            bool
        :static:
        :description: QtCore/QResource-unregisterResource-f.rst

    .. sip:method:: PyQt6.QtCore.QResource.unregisterResourceData
        :args:
            bytes
            mapRoot: str = ''
        :returns:
            bool
        :static:
        :description: QtCore/QResource-unregisterResourceData-f.rst
