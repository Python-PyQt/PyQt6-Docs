:orphan:

.. sip:class:: PyQt6.QtCore.QLibrary
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QLibrary-c.rst

    .. sip:enum:: PyQt6.QtCore.QLibrary.LoadHints
        :description: QtCore/QLibrary-LoadHints-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QLibrary.LoadHints.DeepBindHint
            :description: QtCore/QLibrary-LoadHints-DeepBindHint-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QLibrary.LoadHints.ExportExternalSymbolsHint
            :description: QtCore/QLibrary-LoadHints-ExportExternalSymbolsHint-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QLibrary.LoadHints.LoadArchiveMemberHint
            :description: QtCore/QLibrary-LoadHints-LoadArchiveMemberHint-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QLibrary.LoadHints.PreventUnloadHint
            :description: QtCore/QLibrary-LoadHints-PreventUnloadHint-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QLibrary.LoadHints.ResolveAllSymbolsHint
            :description: QtCore/QLibrary-LoadHints-ResolveAllSymbolsHint-v.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QLibrary-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.__init__
        :args:
            str
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QLibrary-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.__init__
        :args:
            str
            int
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QLibrary-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.__init__
        :args:
            str
            str
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QLibrary-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.errorString
        :returns:
            str
        :description: QtCore/QLibrary-errorString-f.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.fileName
        :returns:
            str
        :description: QtCore/QLibrary-fileName-f.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.isLibrary
        :args:
            str
        :returns:
            bool
        :static:
        :description: QtCore/QLibrary-isLibrary-f.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.isLoaded
        :returns:
            bool
        :description: QtCore/QLibrary-isLoaded-f.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.load
        :returns:
            bool
        :description: QtCore/QLibrary-load-f.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.loadHints
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLibrary.LoadHints`
        :description: QtCore/QLibrary-loadHints-f.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.resolve
        :args:
            str
        :returns:
            sip.voidptr
        :description: QtCore/QLibrary-resolve-f.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.resolve
        :args:
            str
            str
        :returns:
            sip.voidptr
        :static:
        :description: QtCore/QLibrary-resolve-f-1.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.resolve
        :args:
            str
            int
            str
        :returns:
            sip.voidptr
        :static:
        :description: QtCore/QLibrary-resolve-f-2.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.resolve
        :args:
            str
            str
            str
        :returns:
            sip.voidptr
        :static:
        :description: QtCore/QLibrary-resolve-f-3.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.setFileName
        :args:
            str
        :description: QtCore/QLibrary-setFileName-f.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.setFileNameAndVersion
        :args:
            str
            int
        :description: QtCore/QLibrary-setFileNameAndVersion-f.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.setFileNameAndVersion
        :args:
            str
            str
        :description: QtCore/QLibrary-setFileNameAndVersion-f-1.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.setLoadHints
        :args:
            :sip:ref:`~PyQt6.QtCore.QLibrary.LoadHints`
        :description: QtCore/QLibrary-setLoadHints-f.rst

    .. sip:method:: PyQt6.QtCore.QLibrary.unload
        :returns:
            bool
        :description: QtCore/QLibrary-unload-f.rst
