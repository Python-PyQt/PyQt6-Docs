:orphan:

.. sip:class:: PyQt6.QtPdfWidgets.QPdfView
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea`
    :description: QtPdfWidgets/QPdfView-c.rst

    .. sip:enum:: PyQt6.QtPdfWidgets.QPdfView.PageMode
        :description: QtPdfWidgets/QPdfView-PageMode-e.rst

        .. sip:enum-member:: PyQt6.QtPdfWidgets.QPdfView.PageMode.MultiPage
            :description: QtPdfWidgets/QPdfView-PageMode-MultiPage-v.rst

        .. sip:enum-member:: PyQt6.QtPdfWidgets.QPdfView.PageMode.SinglePage
            :description: QtPdfWidgets/QPdfView-PageMode-SinglePage-v.rst

    .. sip:enum:: PyQt6.QtPdfWidgets.QPdfView.ZoomMode
        :description: QtPdfWidgets/QPdfView-ZoomMode-e.rst

        .. sip:enum-member:: PyQt6.QtPdfWidgets.QPdfView.ZoomMode.Custom
            :description: QtPdfWidgets/QPdfView-ZoomMode-Custom-v.rst

        .. sip:enum-member:: PyQt6.QtPdfWidgets.QPdfView.ZoomMode.FitInView
            :description: QtPdfWidgets/QPdfView-ZoomMode-FitInView-v.rst

        .. sip:enum-member:: PyQt6.QtPdfWidgets.QPdfView.ZoomMode.FitToWidth
            :description: QtPdfWidgets/QPdfView-ZoomMode-FitToWidth-v.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.__init__
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtPdfWidgets/QPdfView-__init__-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.currentSearchResultIndex
        :returns:
            int
        :description: QtPdfWidgets/QPdfView-currentSearchResultIndex-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.document
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdfWidgets/QPdfView-document-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.documentMargins
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtPdfWidgets/QPdfView-documentMargins-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtPdfWidgets/QPdfView-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtPdfWidgets/QPdfView-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtPdfWidgets/QPdfView-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.pageMode
        :returns:
            :sip:ref:`~PyQt6.QtPdfWidgets.QPdfView.PageMode`
        :description: QtPdfWidgets/QPdfView-pageMode-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.pageNavigator
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator`
        :description: QtPdfWidgets/QPdfView-pageNavigator-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.pageSpacing
        :returns:
            int
        :description: QtPdfWidgets/QPdfView-pageSpacing-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtPdfWidgets/QPdfView-paintEvent-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtPdfWidgets/QPdfView-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.scrollContentsBy
        :args:
            int
            int
        :description: QtPdfWidgets/QPdfView-scrollContentsBy-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.searchModel
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfSearchModel`
        :description: QtPdfWidgets/QPdfView-searchModel-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.setCurrentSearchResultIndex
        :args:
            int
        :description: QtPdfWidgets/QPdfView-setCurrentSearchResultIndex-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.setDocument
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdfWidgets/QPdfView-setDocument-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.setDocumentMargins
        :args:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtPdfWidgets/QPdfView-setDocumentMargins-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.setPageMode
        :args:
            :sip:ref:`~PyQt6.QtPdfWidgets.QPdfView.PageMode`
        :description: QtPdfWidgets/QPdfView-setPageMode-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.setPageSpacing
        :args:
            int
        :description: QtPdfWidgets/QPdfView-setPageSpacing-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.setSearchModel
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfSearchModel`
        :description: QtPdfWidgets/QPdfView-setSearchModel-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.setZoomFactor
        :args:
            float
        :description: QtPdfWidgets/QPdfView-setZoomFactor-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.setZoomMode
        :args:
            :sip:ref:`~PyQt6.QtPdfWidgets.QPdfView.ZoomMode`
        :description: QtPdfWidgets/QPdfView-setZoomMode-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.zoomFactor
        :returns:
            float
        :description: QtPdfWidgets/QPdfView-zoomFactor-f.rst

    .. sip:method:: PyQt6.QtPdfWidgets.QPdfView.zoomMode
        :returns:
            :sip:ref:`~PyQt6.QtPdfWidgets.QPdfView.ZoomMode`
        :description: QtPdfWidgets/QPdfView-zoomMode-f.rst

    .. sip:signal:: PyQt6.QtPdfWidgets.QPdfView.currentSearchResultIndexChanged
        :args:
            int
        :description: QtPdfWidgets/QPdfView-currentSearchResultIndexChanged-s.rst

    .. sip:signal:: PyQt6.QtPdfWidgets.QPdfView.documentChanged
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdfWidgets/QPdfView-documentChanged-s.rst

    .. sip:signal:: PyQt6.QtPdfWidgets.QPdfView.documentMarginsChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtPdfWidgets/QPdfView-documentMarginsChanged-s.rst

    .. sip:signal:: PyQt6.QtPdfWidgets.QPdfView.pageModeChanged
        :args:
            :sip:ref:`~PyQt6.QtPdfWidgets.QPdfView.PageMode`
        :description: QtPdfWidgets/QPdfView-pageModeChanged-s.rst

    .. sip:signal:: PyQt6.QtPdfWidgets.QPdfView.pageSpacingChanged
        :args:
            int
        :description: QtPdfWidgets/QPdfView-pageSpacingChanged-s.rst

    .. sip:signal:: PyQt6.QtPdfWidgets.QPdfView.searchModelChanged
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfSearchModel`
        :description: QtPdfWidgets/QPdfView-searchModelChanged-s.rst

    .. sip:signal:: PyQt6.QtPdfWidgets.QPdfView.zoomFactorChanged
        :args:
            float
        :description: QtPdfWidgets/QPdfView-zoomFactorChanged-s.rst

    .. sip:signal:: PyQt6.QtPdfWidgets.QPdfView.zoomModeChanged
        :args:
            :sip:ref:`~PyQt6.QtPdfWidgets.QPdfView.ZoomMode`
        :description: QtPdfWidgets/QPdfView-zoomModeChanged-s.rst
