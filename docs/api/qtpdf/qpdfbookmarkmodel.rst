:orphan:

.. sip:class:: PyQt6.QtPdf.QPdfBookmarkModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
    :description: QtPdf/QPdfBookmarkModel-c.rst

    .. sip:enum:: PyQt6.QtPdf.QPdfBookmarkModel.Role
        :description: QtPdf/QPdfBookmarkModel-Role-e.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfBookmarkModel.Role.Level
            :description: QtPdf/QPdfBookmarkModel-Role-Level-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfBookmarkModel.Role.Location
            :description: QtPdf/QPdfBookmarkModel-Role-Location-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfBookmarkModel.Role.Page
            :description: QtPdf/QPdfBookmarkModel-Role-Page-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfBookmarkModel.Role.Title
            :description: QtPdf/QPdfBookmarkModel-Role-Title-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfBookmarkModel.Role.Zoom
            :description: QtPdf/QPdfBookmarkModel-Role-Zoom-v.rst

    .. sip:method:: PyQt6.QtPdf.QPdfBookmarkModel.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtPdf/QPdfBookmarkModel-__init__-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfBookmarkModel.columnCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtPdf/QPdfBookmarkModel-columnCount-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfBookmarkModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            Any
        :description: QtPdf/QPdfBookmarkModel-data-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfBookmarkModel.document
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdf/QPdfBookmarkModel-document-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfBookmarkModel.index
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtPdf/QPdfBookmarkModel-index-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfBookmarkModel.parent
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtPdf/QPdfBookmarkModel-parent-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfBookmarkModel.roleNames
        :returns:
            Dict[int, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtPdf/QPdfBookmarkModel-roleNames-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfBookmarkModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtPdf/QPdfBookmarkModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfBookmarkModel.setDocument
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdf/QPdfBookmarkModel-setDocument-f.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfBookmarkModel.documentChanged
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdf/QPdfBookmarkModel-documentChanged-s.rst
