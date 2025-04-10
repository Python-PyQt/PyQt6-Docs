:orphan:

.. sip:class:: PyQt6.QtGui.QPdfWriter
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject` :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice`
    :description: QtGui/QPdfWriter-c.rst

    .. sip:enum:: PyQt6.QtGui.QPdfWriter.ColorModel
        :description: QtGui/QPdfWriter-ColorModel-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QPdfWriter.ColorModel.Auto
            :description: QtGui/QPdfWriter-ColorModel-Auto-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPdfWriter.ColorModel.CMYK
            :description: QtGui/QPdfWriter-ColorModel-CMYK-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPdfWriter.ColorModel.Grayscale
            :description: QtGui/QPdfWriter-ColorModel-Grayscale-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPdfWriter.ColorModel.RGB
            :description: QtGui/QPdfWriter-ColorModel-RGB-v.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.__init__
        :args:
            Optional[str]
        :description: QtGui/QPdfWriter-__init__-f-2.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtGui/QPdfWriter-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.addFileAttachment
        :args:
            Optional[str]
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            mimeType: Optional[str] = ''
        :description: QtGui/QPdfWriter-addFileAttachment-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.author
        :returns:
            str
        :description: QtGui/QPdfWriter-author-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.colorModel
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPdfWriter.ColorModel`
        :description: QtGui/QPdfWriter-colorModel-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.creator
        :returns:
            str
        :description: QtGui/QPdfWriter-creator-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.documentId
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUuid`
        :description: QtGui/QPdfWriter-documentId-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.documentXmpMetadata
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtGui/QPdfWriter-documentXmpMetadata-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.metric
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintDevice.PaintDeviceMetric`
        :returns:
            int
        :description: QtGui/QPdfWriter-metric-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.newPage
        :returns:
            bool
        :description: QtGui/QPdfWriter-newPage-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.outputIntent
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPdfOutputIntent`
        :description: QtGui/QPdfWriter-outputIntent-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.paintEngine
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPaintEngine`
        :description: QtGui/QPdfWriter-paintEngine-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.pdfVersion
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.PdfVersion`
        :description: QtGui/QPdfWriter-pdfVersion-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.resolution
        :returns:
            int
        :description: QtGui/QPdfWriter-resolution-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.setAuthor
        :args:
            Optional[str]
        :description: QtGui/QPdfWriter-setAuthor-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.setColorModel
        :args:
            :sip:ref:`~PyQt6.QtGui.QPdfWriter.ColorModel`
        :description: QtGui/QPdfWriter-setColorModel-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.setCreator
        :args:
            Optional[str]
        :description: QtGui/QPdfWriter-setCreator-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.setDocumentId
        :args:
            :sip:ref:`~PyQt6.QtCore.QUuid`
        :description: QtGui/QPdfWriter-setDocumentId-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.setDocumentXmpMetadata
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtGui/QPdfWriter-setDocumentXmpMetadata-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.setOutputIntent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPdfOutputIntent`
        :description: QtGui/QPdfWriter-setOutputIntent-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.setPdfVersion
        :args:
            :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.PdfVersion`
        :description: QtGui/QPdfWriter-setPdfVersion-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.setResolution
        :args:
            int
        :description: QtGui/QPdfWriter-setResolution-f.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.setTitle
        :args:
            Optional[str]
        :description: QtGui/QPdfWriter-setTitle-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPdfWriter.title
        :returns:
            str
        :description: QtGui/QPdfWriter-title-f.rst
