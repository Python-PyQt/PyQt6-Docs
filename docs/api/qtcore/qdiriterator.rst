:orphan:

.. sip:class:: PyQt6.QtCore.QDirIterator
    :description: QtCore/QDirIterator-c.rst

    .. sip:enum:: PyQt6.QtCore.QDirIterator.IteratorFlag
        :description: QtCore/QDirIterator-IteratorFlag-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QDirIterator.IteratorFlag.FollowSymlinks
            :description: QtCore/QDirIterator-IteratorFlag-FollowSymlinks-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags
            :description: QtCore/QDirIterator-IteratorFlag-NoIteratorFlags-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDirIterator.IteratorFlag.Subdirectories
            :description: QtCore/QDirIterator-IteratorFlag-Subdirectories-v.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir`
            flags: :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlag` = :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags`
        :description: QtCore/QDirIterator-__init__-f-4.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.__init__
        :args:
            str
            flags: :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlag` = :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags`
        :description: QtCore/QDirIterator-__init__-f-5.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.__init__
        :args:
            str
            :sip:ref:`~PyQt6.QtCore.QDir.Filter`
            flags: :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlag` = :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags`
        :description: QtCore/QDirIterator-__init__-f-6.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.__init__
        :args:
            str
            Iterable[str]
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filter` = :sip:ref:`~PyQt6.QtCore.QDir.Filter.NoFilter`
            flags: :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlag` = :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags`
        :description: QtCore/QDirIterator-__init__-f-7.rst

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

    .. sip:method:: PyQt6.QtCore.QDirIterator.nextFileInfo
        :returns:
            :sip:ref:`~PyQt6.QtCore.QFileInfo`
        :description: QtCore/QDirIterator-nextFileInfo-f.rst

    .. sip:method:: PyQt6.QtCore.QDirIterator.path
        :returns:
            str
        :description: QtCore/QDirIterator-path-f.rst
