:orphan:

.. sip:class:: PyQt6.QtPrintSupport.QPrintPreviewWidget
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtPrintSupport/QPrintPreviewWidget-c.rst

    .. sip:enum:: PyQt6.QtPrintSupport.QPrintPreviewWidget.ViewMode
        :description: QtPrintSupport/QPrintPreviewWidget-ViewMode-e.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QPrintPreviewWidget.ViewMode.AllPagesView
            :description: QtPrintSupport/QPrintPreviewWidget-ViewMode-AllPagesView-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QPrintPreviewWidget.ViewMode.FacingPagesView
            :description: QtPrintSupport/QPrintPreviewWidget-ViewMode-FacingPagesView-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QPrintPreviewWidget.ViewMode.SinglePageView
            :description: QtPrintSupport/QPrintPreviewWidget-ViewMode-SinglePageView-v.rst

    .. sip:enum:: PyQt6.QtPrintSupport.QPrintPreviewWidget.ZoomMode
        :description: QtPrintSupport/QPrintPreviewWidget-ZoomMode-e.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QPrintPreviewWidget.ZoomMode.CustomZoom
            :description: QtPrintSupport/QPrintPreviewWidget-ZoomMode-CustomZoom-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QPrintPreviewWidget.ZoomMode.FitInView
            :description: QtPrintSupport/QPrintPreviewWidget-ZoomMode-FitInView-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QPrintPreviewWidget.ZoomMode.FitToWidth
            :description: QtPrintSupport/QPrintPreviewWidget-ZoomMode-FitToWidth-v.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :description: QtPrintSupport/QPrintPreviewWidget-__init__-f-2.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.__init__
        :args:
            :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :description: QtPrintSupport/QPrintPreviewWidget-__init__-f-3.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.currentPage
        :returns:
            int
        :description: QtPrintSupport/QPrintPreviewWidget-currentPage-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.fitInView
        :description: QtPrintSupport/QPrintPreviewWidget-fitInView-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.fitToWidth
        :description: QtPrintSupport/QPrintPreviewWidget-fitToWidth-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.orientation
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Orientation`
        :description: QtPrintSupport/QPrintPreviewWidget-orientation-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.pageCount
        :returns:
            int
        :description: QtPrintSupport/QPrintPreviewWidget-pageCount-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.print
        :description: QtPrintSupport/QPrintPreviewWidget-print-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.setAllPagesViewMode
        :description: QtPrintSupport/QPrintPreviewWidget-setAllPagesViewMode-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.setCurrentPage
        :args:
            int
        :description: QtPrintSupport/QPrintPreviewWidget-setCurrentPage-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.setFacingPagesViewMode
        :description: QtPrintSupport/QPrintPreviewWidget-setFacingPagesViewMode-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.setLandscapeOrientation
        :description: QtPrintSupport/QPrintPreviewWidget-setLandscapeOrientation-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.setOrientation
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Orientation`
        :description: QtPrintSupport/QPrintPreviewWidget-setOrientation-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.setPortraitOrientation
        :description: QtPrintSupport/QPrintPreviewWidget-setPortraitOrientation-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.setSinglePageViewMode
        :description: QtPrintSupport/QPrintPreviewWidget-setSinglePageViewMode-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.setViewMode
        :args:
            :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget.ViewMode`
        :description: QtPrintSupport/QPrintPreviewWidget-setViewMode-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.setVisible
        :args:
            bool
        :description: QtPrintSupport/QPrintPreviewWidget-setVisible-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.setZoomFactor
        :args:
            float
        :description: QtPrintSupport/QPrintPreviewWidget-setZoomFactor-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.setZoomMode
        :args:
            :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget.ZoomMode`
        :description: QtPrintSupport/QPrintPreviewWidget-setZoomMode-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.updatePreview
        :description: QtPrintSupport/QPrintPreviewWidget-updatePreview-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.viewMode
        :returns:
            :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget.ViewMode`
        :description: QtPrintSupport/QPrintPreviewWidget-viewMode-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.zoomFactor
        :returns:
            float
        :description: QtPrintSupport/QPrintPreviewWidget-zoomFactor-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.zoomIn
        :args:
            factor: float = 1.1
        :description: QtPrintSupport/QPrintPreviewWidget-zoomIn-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.zoomMode
        :returns:
            :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget.ZoomMode`
        :description: QtPrintSupport/QPrintPreviewWidget-zoomMode-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QPrintPreviewWidget.zoomOut
        :args:
            factor: float = 1.1
        :description: QtPrintSupport/QPrintPreviewWidget-zoomOut-f.rst

    .. sip:signal:: PyQt6.QtPrintSupport.QPrintPreviewWidget.paintRequested
        :args:
            :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`
        :description: QtPrintSupport/QPrintPreviewWidget-paintRequested-s.rst

    .. sip:signal:: PyQt6.QtPrintSupport.QPrintPreviewWidget.previewChanged
        :description: QtPrintSupport/QPrintPreviewWidget-previewChanged-s.rst
