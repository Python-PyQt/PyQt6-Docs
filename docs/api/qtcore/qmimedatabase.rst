:orphan:

.. sip:class:: PyQt6.QtCore.QMimeDatabase
    :description: QtCore/QMimeDatabase-c.rst

    .. sip:enum:: PyQt6.QtCore.QMimeDatabase.MatchMode
        :description: QtCore/QMimeDatabase-MatchMode-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QMimeDatabase.MatchMode.MatchContent
            :description: QtCore/QMimeDatabase-MatchMode-MatchContent-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QMimeDatabase.MatchMode.MatchDefault
            :description: QtCore/QMimeDatabase-MatchMode-MatchDefault-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QMimeDatabase.MatchMode.MatchExtension
            :description: QtCore/QMimeDatabase-MatchMode-MatchExtension-v.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.__init__
        :description: QtCore/QMimeDatabase-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.allMimeTypes
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QMimeType`]
        :description: QtCore/QMimeDatabase-allMimeTypes-f-1.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.mimeTypeForData
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeType`
        :description: QtCore/QMimeDatabase-mimeTypeForData-f-2.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.mimeTypeForData
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeType`
        :description: QtCore/QMimeDatabase-mimeTypeForData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.mimeTypeForFile
        :args:
            Optional[str]
            mode: :sip:ref:`~PyQt6.QtCore.QMimeDatabase.MatchMode` = :sip:ref:`~PyQt6.QtCore.QMimeDatabase.MatchMode.MatchDefault`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeType`
        :description: QtCore/QMimeDatabase-mimeTypeForFile-f-2.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.mimeTypeForFile
        :args:
            :sip:ref:`~PyQt6.QtCore.QFileInfo`
            mode: :sip:ref:`~PyQt6.QtCore.QMimeDatabase.MatchMode` = :sip:ref:`~PyQt6.QtCore.QMimeDatabase.MatchMode.MatchDefault`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeType`
        :description: QtCore/QMimeDatabase-mimeTypeForFile-f-1.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.mimeTypeForFileNameAndData
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeType`
        :description: QtCore/QMimeDatabase-mimeTypeForFileNameAndData-f-2.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.mimeTypeForFileNameAndData
        :args:
            Optional[str]
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeType`
        :description: QtCore/QMimeDatabase-mimeTypeForFileNameAndData-f-3.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.mimeTypeForName
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeType`
        :description: QtCore/QMimeDatabase-mimeTypeForName-f-1.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.mimeTypeForUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeType`
        :description: QtCore/QMimeDatabase-mimeTypeForUrl-f.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.mimeTypesForFileName
        :args:
            Optional[str]
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QMimeType`]
        :description: QtCore/QMimeDatabase-mimeTypesForFileName-f.rst

    .. sip:method:: PyQt6.QtCore.QMimeDatabase.suffixForFileName
        :args:
            Optional[str]
        :returns:
            str
        :description: QtCore/QMimeDatabase-suffixForFileName-f-1.rst
