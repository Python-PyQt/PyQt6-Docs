:orphan:

.. sip:class:: PyQt6.QtPdf.QPdfPageNavigator
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtPdf/QPdfPageNavigator-c.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtPdf/QPdfPageNavigator-__init__-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.back
        :description: QtPdf/QPdfPageNavigator-back-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.backAvailable
        :returns:
            bool
        :description: QtPdf/QPdfPageNavigator-backAvailable-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.clear
        :description: QtPdf/QPdfPageNavigator-clear-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.currentLocation
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtPdf/QPdfPageNavigator-currentLocation-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.currentPage
        :returns:
            int
        :description: QtPdf/QPdfPageNavigator-currentPage-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.currentZoom
        :returns:
            float
        :description: QtPdf/QPdfPageNavigator-currentZoom-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.forward
        :description: QtPdf/QPdfPageNavigator-forward-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.forwardAvailable
        :returns:
            bool
        :description: QtPdf/QPdfPageNavigator-forwardAvailable-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.jump
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfLink`
        :description: QtPdf/QPdfPageNavigator-jump-f.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.jump
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QPointF`
            zoom: float = 0
        :description: QtPdf/QPdfPageNavigator-jump-f-1.rst

    .. sip:method:: PyQt6.QtPdf.QPdfPageNavigator.update
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QPointF`
            float
        :description: QtPdf/QPdfPageNavigator-update-f.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfPageNavigator.backAvailableChanged
        :args:
            bool
        :description: QtPdf/QPdfPageNavigator-backAvailableChanged-s.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfPageNavigator.currentLocationChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtPdf/QPdfPageNavigator-currentLocationChanged-s.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfPageNavigator.currentPageChanged
        :args:
            int
        :description: QtPdf/QPdfPageNavigator-currentPageChanged-s.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfPageNavigator.currentZoomChanged
        :args:
            float
        :description: QtPdf/QPdfPageNavigator-currentZoomChanged-s.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfPageNavigator.forwardAvailableChanged
        :args:
            bool
        :description: QtPdf/QPdfPageNavigator-forwardAvailableChanged-s.rst

    .. sip:signal:: PyQt6.QtPdf.QPdfPageNavigator.jumped
        :args:
            :sip:ref:`~PyQt6.QtPdf.QPdfLink`
        :description: QtPdf/QPdfPageNavigator-jumped-s.rst
