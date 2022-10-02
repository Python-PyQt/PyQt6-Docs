:orphan:

.. sip:class:: PyQt6.QtPdf.QPdfPageRenderer
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtPdf/QPdfPageRenderer-c.rst

    .. sip:enum:: PyQt6.QtPdf.QPdfPageRenderer.RenderMode
        :description: QtPdf/QPdfPageRenderer-RenderMode-e.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfPageRenderer.RenderMode.MultiThreaded
            :description: QtPdf/QPdfPageRenderer-RenderMode-MultiThreaded-v.rst

        .. sip:enum-member:: PyQt6.QtPdf.QPdfPageRenderer.RenderMode.SingleThreaded
            :description: QtPdf/QPdfPageRenderer-RenderMode-SingleThreaded-v.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageRenderer.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtPdf/QPdfPageRenderer-__init__-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageRenderer.document
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdf/QPdfPageRenderer-document-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageRenderer.renderMode
        :returns:
            :sip:ref:`~PyQt6.QtPdf.QPdfPageRenderer.RenderMode`
        :description: QtPdf/QPdfPageRenderer-renderMode-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageRenderer.requestPage
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QSize`
            options: :sip:ref:`~PyQt6.QtPdf.QPdfDocumentRenderOptions` = QPdfDocumentRenderOptions()
        :returns:
            int
        :description: QtPdf/QPdfPageRenderer-requestPage-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageRenderer.setDocument
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdf/QPdfPageRenderer-setDocument-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageRenderer.setRenderMode
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfPageRenderer.RenderMode`
        :description: QtPdf/QPdfPageRenderer-setRenderMode-f.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfPageRenderer.documentChanged
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfDocument`
        :description: QtPdf/QPdfPageRenderer-documentChanged-s.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfPageRenderer.renderModeChanged
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfPageRenderer.RenderMode`
        :description: QtPdf/QPdfPageRenderer-renderModeChanged-s.rst
