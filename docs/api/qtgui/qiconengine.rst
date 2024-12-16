:orphan:

.. sip:class:: PyQt6.QtGui.QIconEngine
    :description: QtGui/QIconEngine-c.rst

    .. sip:enum:: PyQt6.QtGui.QIconEngine.IconEngineHook
        :description: QtGui/QIconEngine-IconEngineHook-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QIconEngine.IconEngineHook.IsNullHook
            :description: QtGui/QIconEngine-IconEngineHook-IsNullHook-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QIconEngine.IconEngineHook.ScaledPixmapHook
            :description: QtGui/QIconEngine-IconEngineHook-ScaledPixmapHook-v.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.__init__
        :description: QtGui/QIconEngine-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QIconEngine`
        :description: QtGui/QIconEngine-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.actualSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
            :sip:ref:`~PyQt6.QtGui.QIcon.Mode`
            :sip:ref:`~PyQt6.QtGui.QIcon.State`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtGui/QIconEngine-actualSize-f.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.addFile
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QSize`
            :sip:ref:`~PyQt6.QtGui.QIcon.Mode`
            :sip:ref:`~PyQt6.QtGui.QIcon.State`
        :description: QtGui/QIconEngine-addFile-f-1.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.addPixmap
        :args:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
            :sip:ref:`~PyQt6.QtGui.QIcon.Mode`
            :sip:ref:`~PyQt6.QtGui.QIcon.State`
        :description: QtGui/QIconEngine-addPixmap-f.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.availableSizes
        :args:
            mode: :sip:ref:`~PyQt6.QtGui.QIcon.Mode` = :sip:ref:`~PyQt6.QtGui.QIcon.Mode.Normal`
            state: :sip:ref:`~PyQt6.QtGui.QIcon.State` = :sip:ref:`~PyQt6.QtGui.QIcon.State.Off`
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QSize`]
        :description: QtGui/QIconEngine-availableSizes-f-1.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.clone
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIconEngine`
        :description: QtGui/QIconEngine-clone-f.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.iconName
        :returns:
            str
        :description: QtGui/QIconEngine-iconName-f.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.isNull
        :returns:
            bool
        :description: QtGui/QIconEngine-isNull-f.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.key
        :returns:
            str
        :description: QtGui/QIconEngine-key-f.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.paint
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtGui.QIcon.Mode`
            :sip:ref:`~PyQt6.QtGui.QIcon.State`
        :description: QtGui/QIconEngine-paint-f.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.pixmap
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
            :sip:ref:`~PyQt6.QtGui.QIcon.Mode`
            :sip:ref:`~PyQt6.QtGui.QIcon.State`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QIconEngine-pixmap-f.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.read
        :args:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :returns:
            bool
        :description: QtGui/QIconEngine-read-f.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.scaledPixmap
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
            :sip:ref:`~PyQt6.QtGui.QIcon.Mode`
            :sip:ref:`~PyQt6.QtGui.QIcon.State`
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QIconEngine-scaledPixmap-f.rst

    .. sip:method:: PyQt6.QtGui.QIconEngine.write
        :args:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :returns:
            bool
        :description: QtGui/QIconEngine-write-f.rst
