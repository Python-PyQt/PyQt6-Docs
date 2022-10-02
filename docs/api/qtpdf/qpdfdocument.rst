:orphan:

.. sip:class:: PyQt6.QtPdf.QPdfDocument
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtPdf/QPdfDocument-c.rst

    .. sip:enum:: PyQt6.QtPdf.QPdfDocument.Error
        :description: QtPdf/QPdfDocument-Error-e.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Error.DataNotYetAvailable
            :description: QtPdf/QPdfDocument-Error-DataNotYetAvailable-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Error.FileNotFound
            :description: QtPdf/QPdfDocument-Error-FileNotFound-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Error.IncorrectPassword
            :description: QtPdf/QPdfDocument-Error-IncorrectPassword-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Error.InvalidFileFormat
            :description: QtPdf/QPdfDocument-Error-InvalidFileFormat-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Error.None_
            :description: QtPdf/QPdfDocument-Error-None_-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Error.Unknown
            :description: QtPdf/QPdfDocument-Error-Unknown-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Error.UnsupportedSecurityScheme
            :description: QtPdf/QPdfDocument-Error-UnsupportedSecurityScheme-v.rst

    .. sip:enum:: PyQt6.QtPdf.QPdfDocument.MetaDataField
        :description: QtPdf/QPdfDocument-MetaDataField-e.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.MetaDataField.Author
            :description: QtPdf/QPdfDocument-MetaDataField-Author-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.MetaDataField.CreationDate
            :description: QtPdf/QPdfDocument-MetaDataField-CreationDate-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.MetaDataField.Creator
            :description: QtPdf/QPdfDocument-MetaDataField-Creator-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.MetaDataField.Keywords
            :description: QtPdf/QPdfDocument-MetaDataField-Keywords-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.MetaDataField.ModificationDate
            :description: QtPdf/QPdfDocument-MetaDataField-ModificationDate-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.MetaDataField.Producer
            :description: QtPdf/QPdfDocument-MetaDataField-Producer-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.MetaDataField.Subject
            :description: QtPdf/QPdfDocument-MetaDataField-Subject-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.MetaDataField.Title
            :description: QtPdf/QPdfDocument-MetaDataField-Title-v.rst

    .. sip:enum:: PyQt6.QtPdf.QPdfDocument.PageModelRole
        :description: QtPdf/QPdfDocument-PageModelRole-e.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.PageModelRole.Label
            :description: QtPdf/QPdfDocument-PageModelRole-Label-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.PageModelRole.PointSize
            :description: QtPdf/QPdfDocument-PageModelRole-PointSize-v.rst

    .. sip:enum:: PyQt6.QtPdf.QPdfDocument.Status
        :description: QtPdf/QPdfDocument-Status-e.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Status.Error
            :description: QtPdf/QPdfDocument-Status-Error-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Status.Loading
            :description: QtPdf/QPdfDocument-Status-Loading-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Status.Null
            :description: QtPdf/QPdfDocument-Status-Null-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Status.Ready
            :description: QtPdf/QPdfDocument-Status-Ready-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfDocument.Status.Unloading
            :description: QtPdf/QPdfDocument-Status-Unloading-v.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtPdf/QPdfDocument-__init__-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.close
        :description: QtPdf/QPdfDocument-close-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.error
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument.Error`
        :description: QtPdf/QPdfDocument-error-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.getAllText
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfSelection`
        :description: QtPdf/QPdfDocument-getAllText-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.getSelection
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfSelection`
        :description: QtPdf/QPdfDocument-getSelection-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.getSelectionAtIndex
        :args:
            int
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfSelection`
        :description: QtPdf/QPdfDocument-getSelectionAtIndex-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.load
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument.Error`
        :description: QtPdf/QPdfDocument-load-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.load
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtPdf/QPdfDocument-load-f-1.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.metaData
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument.MetaDataField`
        :returns:
            Any
        :description: QtPdf/QPdfDocument-metaData-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.pageCount
        :returns:
            int
        :description: QtPdf/QPdfDocument-pageCount-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.pageLabel
        :args:
            int
        :returns:
            str
        :description: QtPdf/QPdfDocument-pageLabel-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.pageModel
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractListModel`
        :description: QtPdf/QPdfDocument-pageModel-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.pagePointSize
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :description: QtPdf/QPdfDocument-pagePointSize-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.password
        :returns:
            str
        :description: QtPdf/QPdfDocument-password-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.render
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QSize`
            options: :sip:ref:`~PyQt6.QtPdf.QPdfDocumentRenderOptions` = QPdfDocumentRenderOptions()
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtPdf/QPdfDocument-render-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.setPassword
        :args:
            str
        :description: QtPdf/QPdfDocument-setPassword-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfDocument.status
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument.Status`
        :description: QtPdf/QPdfDocument-status-f.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfDocument.pageCountChanged
        :args:
            int
        :description: QtPdf/QPdfDocument-pageCountChanged-s.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfDocument.pageModelChanged
        :description: QtPdf/QPdfDocument-pageModelChanged-s.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfDocument.passwordChanged
        :description: QtPdf/QPdfDocument-passwordChanged-s.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfDocument.statusChanged
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument.Status`
        :description: QtPdf/QPdfDocument-statusChanged-s.rst
