:orphan:

.. sip:class:: PyQt6.QtGui.QIcon
    :description: QtGui/QIcon-c.rst

    .. sip:enum:: PyQt6.QtGui.QIcon.Mode
        :description: QtGui/QIcon-Mode-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QIcon.Mode.Active
            :description: QtGui/QIcon-Mode-Active-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QIcon.Mode.Disabled
            :description: QtGui/QIcon-Mode-Disabled-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QIcon.Mode.Normal
            :description: QtGui/QIcon-Mode-Normal-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QIcon.Mode.Selected
            :description: QtGui/QIcon-Mode-Selected-v.rst

    .. sip:enum:: PyQt6.QtGui.QIcon.State
        :description: QtGui/QIcon-State-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QIcon.State.Off
            :description: QtGui/QIcon-State-Off-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QIcon.State.On
            :description: QtGui/QIcon-State-On-v.rst

    .. sip:method:: PyQt6.QtGui.QIcon.__init__
        :description: QtGui/QIcon-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QIcon-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QIcon.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtGui/QIcon-__init__-f-2.rst

    .. sip:method:: PyQt6.QtGui.QIcon.__init__
        :args:
            str
        :description: QtGui/QIcon-__init__-f-3.rst

    .. sip:method:: PyQt6.QtGui.QIcon.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QIconEngine`
        :description: QtGui/QIcon-__init__-f-4.rst

    .. sip:method:: PyQt6.QtGui.QIcon.__init__
        :args:
            Any
        :description: QtGui/QIcon-__init__-f-5.rst

    .. sip:method:: PyQt6.QtGui.QIcon.actualSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
            mode: :sip:ref:`~PyQt6.QtGui.QIcon.Mode` = :sip:ref:`~PyQt6.QtGui.QIcon.Mode.Normal`
            state: :sip:ref:`~PyQt6.QtGui.QIcon.State` = :sip:ref:`~PyQt6.QtGui.QIcon.State.Off`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtGui/QIcon-actualSize-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.addFile
        :args:
            str
            size: :sip:ref:`~PyQt6.QtCore.QSize` = QSize()
            mode: :sip:ref:`~PyQt6.QtGui.QIcon.Mode` = :sip:ref:`~PyQt6.QtGui.QIcon.Mode.Normal`
            state: :sip:ref:`~PyQt6.QtGui.QIcon.State` = :sip:ref:`~PyQt6.QtGui.QIcon.State.Off`
        :description: QtGui/QIcon-addFile-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.addPixmap
        :args:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
            mode: :sip:ref:`~PyQt6.QtGui.QIcon.Mode` = :sip:ref:`~PyQt6.QtGui.QIcon.Mode.Normal`
            state: :sip:ref:`~PyQt6.QtGui.QIcon.State` = :sip:ref:`~PyQt6.QtGui.QIcon.State.Off`
        :description: QtGui/QIcon-addPixmap-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.availableSizes
        :args:
            mode: :sip:ref:`~PyQt6.QtGui.QIcon.Mode` = :sip:ref:`~PyQt6.QtGui.QIcon.Mode.Normal`
            state: :sip:ref:`~PyQt6.QtGui.QIcon.State` = :sip:ref:`~PyQt6.QtGui.QIcon.State.Off`
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QSize`]
        :description: QtGui/QIcon-availableSizes-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.cacheKey
        :returns:
            int
        :description: QtGui/QIcon-cacheKey-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.fallbackSearchPaths
        :returns:
            List[str]
        :static:
        :description: QtGui/QIcon-fallbackSearchPaths-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.fallbackThemeName
        :returns:
            str
        :static:
        :description: QtGui/QIcon-fallbackThemeName-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.fromTheme
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :static:
        :description: QtGui/QIcon-fromTheme-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.fromTheme
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :static:
        :description: QtGui/QIcon-fromTheme-f-1.rst

    .. sip:method:: PyQt6.QtGui.QIcon.hasThemeIcon
        :args:
            str
        :returns:
            bool
        :static:
        :description: QtGui/QIcon-hasThemeIcon-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.isDetached
        :returns:
            bool
        :description: QtGui/QIcon-isDetached-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.isMask
        :returns:
            bool
        :description: QtGui/QIcon-isMask-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.isNull
        :returns:
            bool
        :description: QtGui/QIcon-isNull-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.name
        :returns:
            str
        :description: QtGui/QIcon-name-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.paint
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            alignment: :sip:ref:`~PyQt6.QtCore.Qt.Alignment` = :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignCenter`
            mode: :sip:ref:`~PyQt6.QtGui.QIcon.Mode` = :sip:ref:`~PyQt6.QtGui.QIcon.Mode.Normal`
            state: :sip:ref:`~PyQt6.QtGui.QIcon.State` = :sip:ref:`~PyQt6.QtGui.QIcon.State.Off`
        :description: QtGui/QIcon-paint-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.paint
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            int
            int
            int
            int
            alignment: :sip:ref:`~PyQt6.QtCore.Qt.Alignment` = :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignCenter`
            mode: :sip:ref:`~PyQt6.QtGui.QIcon.Mode` = :sip:ref:`~PyQt6.QtGui.QIcon.Mode.Normal`
            state: :sip:ref:`~PyQt6.QtGui.QIcon.State` = :sip:ref:`~PyQt6.QtGui.QIcon.State.Off`
        :description: QtGui/QIcon-paint-f-1.rst

    .. sip:method:: PyQt6.QtGui.QIcon.pixmap
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
            mode: :sip:ref:`~PyQt6.QtGui.QIcon.Mode` = :sip:ref:`~PyQt6.QtGui.QIcon.Mode.Normal`
            state: :sip:ref:`~PyQt6.QtGui.QIcon.State` = :sip:ref:`~PyQt6.QtGui.QIcon.State.Off`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QIcon-pixmap-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.pixmap
        :args:
            int
            mode: :sip:ref:`~PyQt6.QtGui.QIcon.Mode` = :sip:ref:`~PyQt6.QtGui.QIcon.Mode.Normal`
            state: :sip:ref:`~PyQt6.QtGui.QIcon.State` = :sip:ref:`~PyQt6.QtGui.QIcon.State.Off`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QIcon-pixmap-f-1.rst

    .. sip:method:: PyQt6.QtGui.QIcon.pixmap
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
            float
            mode: :sip:ref:`~PyQt6.QtGui.QIcon.Mode` = :sip:ref:`~PyQt6.QtGui.QIcon.Mode.Normal`
            state: :sip:ref:`~PyQt6.QtGui.QIcon.State` = :sip:ref:`~PyQt6.QtGui.QIcon.State.Off`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QIcon-pixmap-f-2.rst

    .. sip:method:: PyQt6.QtGui.QIcon.pixmap
        :args:
            int
            int
            mode: :sip:ref:`~PyQt6.QtGui.QIcon.Mode` = :sip:ref:`~PyQt6.QtGui.QIcon.Mode.Normal`
            state: :sip:ref:`~PyQt6.QtGui.QIcon.State` = :sip:ref:`~PyQt6.QtGui.QIcon.State.Off`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QIcon-pixmap-f-3.rst

    .. sip:method:: PyQt6.QtGui.QIcon.setFallbackSearchPaths
        :args:
            Iterable[str]
        :static:
        :description: QtGui/QIcon-setFallbackSearchPaths-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.setFallbackThemeName
        :args:
            str
        :static:
        :description: QtGui/QIcon-setFallbackThemeName-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.setIsMask
        :args:
            bool
        :description: QtGui/QIcon-setIsMask-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.setThemeName
        :args:
            str
        :static:
        :description: QtGui/QIcon-setThemeName-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.setThemeSearchPaths
        :args:
            Iterable[str]
        :static:
        :description: QtGui/QIcon-setThemeSearchPaths-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.swap
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtGui/QIcon-swap-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.themeName
        :returns:
            str
        :static:
        :description: QtGui/QIcon-themeName-f.rst

    .. sip:method:: PyQt6.QtGui.QIcon.themeSearchPaths
        :returns:
            List[str]
        :static:
        :description: QtGui/QIcon-themeSearchPaths-f.rst
