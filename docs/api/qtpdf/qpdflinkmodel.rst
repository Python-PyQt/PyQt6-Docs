:orphan:

.. sip:class:: PyQt6.QtPdf.QPdfLinkModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractListModel`
    :description: QtPdf/QPdfLinkModel-c.rst

    .. sip:enum:: PyQt6.QtPdf.QPdfLinkModel.Role
        :description: QtPdf/QPdfLinkModel-Role-e.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfLinkModel.Role.Link
            :description: QtPdf/QPdfLinkModel-Role-Link-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfLinkModel.Role.Location
            :description: QtPdf/QPdfLinkModel-Role-Location-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfLinkModel.Role.Page
            :description: QtPdf/QPdfLinkModel-Role-Page-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfLinkModel.Role.Rectangle
            :description: QtPdf/QPdfLinkModel-Role-Rectangle-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfLinkModel.Role.Url
            :description: QtPdf/QPdfLinkModel-Role-Url-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfLinkModel.Role.Zoom
            :description: QtPdf/QPdfLinkModel-Role-Zoom-v.rst

    .. sip:method:: PyQt6.QtPdf.QPdfLinkModel.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtPdf/QPdfLinkModel-__init__-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfLinkModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            Any
        :description: QtPdf/QPdfLinkModel-data-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfLinkModel.document
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdf/QPdfLinkModel-document-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfLinkModel.linkAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfLink`
        :description: QtPdf/QPdfLinkModel-linkAt-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfLinkModel.page
        :returns:
            int
        :description: QtPdf/QPdfLinkModel-page-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfLinkModel.roleNames
        :returns:
            Dict[int, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtPdf/QPdfLinkModel-roleNames-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfLinkModel.rowCount
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            int
        :description: QtPdf/QPdfLinkModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfLinkModel.setDocument
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdf/QPdfLinkModel-setDocument-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfLinkModel.setPage
        :args:
            int
        :description: QtPdf/QPdfLinkModel-setPage-f.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfLinkModel.documentChanged
        :description: QtPdf/QPdfLinkModel-documentChanged-s.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfLinkModel.pageChanged
        :args:
            int
        :description: QtPdf/QPdfLinkModel-pageChanged-s.rst
