:orphan:

.. sip:class:: PyQt6.QtPdf.QPdfSearchModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractListModel`
    :description: QtPdf/QPdfSearchModel-c.rst

    .. sip:enum:: PyQt6.QtPdf.QPdfSearchModel.Role
        :description: QtPdf/QPdfSearchModel-Role-e.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfSearchModel.Role.ContextAfter
            :description: QtPdf/QPdfSearchModel-Role-ContextAfter-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfSearchModel.Role.ContextBefore
            :description: QtPdf/QPdfSearchModel-Role-ContextBefore-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfSearchModel.Role.IndexOnPage
            :description: QtPdf/QPdfSearchModel-Role-IndexOnPage-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfSearchModel.Role.Location
            :description: QtPdf/QPdfSearchModel-Role-Location-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfSearchModel.Role.Page
            :description: QtPdf/QPdfSearchModel-Role-Page-v.rst

    .. sip:method:: PyQt6.QtPdf.QPdfSearchModel.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtPdf/QPdfSearchModel-__init__-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfSearchModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            Any
        :description: QtPdf/QPdfSearchModel-data-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfSearchModel.document
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdf/QPdfSearchModel-document-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfSearchModel.resultAtIndex
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfLink`
        :description: QtPdf/QPdfSearchModel-resultAtIndex-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfSearchModel.resultsOnPage
        :args:
            int
        :returns:
            List[:sip:ref:`~PyQt6.QtPdf.QPdfLink`]
        :description: QtPdf/QPdfSearchModel-resultsOnPage-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfSearchModel.roleNames
        :returns:
            Dict[int, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtPdf/QPdfSearchModel-roleNames-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfSearchModel.rowCount
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            int
        :description: QtPdf/QPdfSearchModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfSearchModel.searchString
        :returns:
            str
        :description: QtPdf/QPdfSearchModel-searchString-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfSearchModel.setDocument
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdf/QPdfSearchModel-setDocument-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfSearchModel.setSearchString
        :args:
            str
        :description: QtPdf/QPdfSearchModel-setSearchString-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfSearchModel.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtPdf/QPdfSearchModel-timerEvent-f.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfSearchModel.documentChanged
        :description: QtPdf/QPdfSearchModel-documentChanged-s.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfSearchModel.searchStringChanged
        :description: QtPdf/QPdfSearchModel-searchStringChanged-s.rst
