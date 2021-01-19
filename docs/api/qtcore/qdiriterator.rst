:orphan:

.. sip:class:: PyQt6.QtCore.QDirIterator
    :description: QtCore/QDirIterator-c.rst

    .. sip:enum:: PyQt6.QtCore.QDirIterator.IteratorFlags
        :description: QtCore/QDirIterator-IteratorFlags-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QDirIterator.IteratorFlags.FollowSymlinks
            :description: QtCore/QDirIterator-IteratorFlags-FollowSymlinks-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDirIterator.IteratorFlags.NoIteratorFlags
            :description: QtCore/QDirIterator-IteratorFlags-NoIteratorFlags-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDirIterator.IteratorFlags.Subdirectories
            :description: QtCore/QDirIterator-IteratorFlags-Subdirectories-v.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir`
            flags: :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags` = :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags.NoIteratorFlags`
        :description: QtCore/QDirIterator-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.__init__
        :args:
            str
            flags: :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags` = :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags.NoIteratorFlags`
        :description: QtCore/QDirIterator-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.__init__
        :args:
            str
            :sip:ref:`~PyQt6.QtCore.QDir.Filters`
            flags: :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags` = :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags.NoIteratorFlags`
        :description: QtCore/QDirIterator-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.__init__
        :args:
            str
            Iterable[str]
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filters` = :sip:ref:`~PyQt6.QtCore.QDir.Filters.NoFilter`
            flags: :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags` = :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags.NoIteratorFlags`
        :description: QtCore/QDirIterator-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.fileInfo
        :returns:
            :sip:ref:`~PyQt6.QtCore.QFileInfo`
        :description: QtCore/QDirIterator-fileInfo-f.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.fileName
        :returns:
            str
        :description: QtCore/QDirIterator-fileName-f.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.filePath
        :returns:
            str
        :description: QtCore/QDirIterator-filePath-f.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.hasNext
        :returns:
            bool
        :description: QtCore/QDirIterator-hasNext-f.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.next
        :returns:
            str
        :description: QtCore/QDirIterator-next-f.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.path
        :returns:
            str
        :description: QtCore/QDirIterator-path-f.rst
