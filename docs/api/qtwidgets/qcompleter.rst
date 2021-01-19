:orphan:

.. sip:class:: PyQt6.QtWidgets.QCompleter
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWidgets/QCompleter-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QCompleter.CompletionMode
        :description: QtWidgets/QCompleter-CompletionMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCompleter.CompletionMode.InlineCompletion
            :description: QtWidgets/QCompleter-CompletionMode-InlineCompletion-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCompleter.CompletionMode.PopupCompletion
            :description: QtWidgets/QCompleter-CompletionMode-PopupCompletion-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCompleter.CompletionMode.UnfilteredPopupCompletion
            :description: QtWidgets/QCompleter-CompletionMode-UnfilteredPopupCompletion-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QCompleter.ModelSorting
        :description: QtWidgets/QCompleter-ModelSorting-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCompleter.ModelSorting.CaseInsensitivelySortedModel
            :description: QtWidgets/QCompleter-ModelSorting-CaseInsensitivelySortedModel-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCompleter.ModelSorting.CaseSensitivelySortedModel
            :description: QtWidgets/QCompleter-ModelSorting-CaseSensitivelySortedModel-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCompleter.ModelSorting.UnsortedModel
            :description: QtWidgets/QCompleter-ModelSorting-UnsortedModel-v.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QCompleter-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QCompleter-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.__init__
        :args:
            Iterable[str]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QCompleter-__init__-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.caseSensitivity
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity`
        :description: QtWidgets/QCompleter-caseSensitivity-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.complete
        :args:
            rect: :sip:ref:`~PyQt6.QtCore.QRect` = QRect()
        :description: QtWidgets/QCompleter-complete-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.completionColumn
        :returns:
            int
        :description: QtWidgets/QCompleter-completionColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.completionCount
        :returns:
            int
        :description: QtWidgets/QCompleter-completionCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.completionMode
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QCompleter.CompletionMode`
        :description: QtWidgets/QCompleter-completionMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.completionModel
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtWidgets/QCompleter-completionModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.completionPrefix
        :returns:
            str
        :description: QtWidgets/QCompleter-completionPrefix-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.completionRole
        :returns:
            int
        :description: QtWidgets/QCompleter-completionRole-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.currentCompletion
        :returns:
            str
        :description: QtWidgets/QCompleter-currentCompletion-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.currentIndex
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QCompleter-currentIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.currentRow
        :returns:
            int
        :description: QtWidgets/QCompleter-currentRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QCompleter-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.eventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QCompleter-eventFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.filterMode
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.MatchFlags`
        :description: QtWidgets/QCompleter-filterMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.maxVisibleItems
        :returns:
            int
        :description: QtWidgets/QCompleter-maxVisibleItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.model
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtWidgets/QCompleter-model-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.modelSorting
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QCompleter.ModelSorting`
        :description: QtWidgets/QCompleter-modelSorting-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.pathFromIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            str
        :description: QtWidgets/QCompleter-pathFromIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.popup
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
        :description: QtWidgets/QCompleter-popup-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setCaseSensitivity
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity`
        :description: QtWidgets/QCompleter-setCaseSensitivity-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setCompletionColumn
        :args:
            int
        :description: QtWidgets/QCompleter-setCompletionColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setCompletionMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QCompleter.CompletionMode`
        :description: QtWidgets/QCompleter-setCompletionMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setCompletionPrefix
        :args:
            str
        :description: QtWidgets/QCompleter-setCompletionPrefix-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setCompletionRole
        :args:
            int
        :description: QtWidgets/QCompleter-setCompletionRole-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setCurrentRow
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QCompleter-setCurrentRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setFilterMode
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.MatchFlags`
        :description: QtWidgets/QCompleter-setFilterMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setMaxVisibleItems
        :args:
            int
        :description: QtWidgets/QCompleter-setMaxVisibleItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtWidgets/QCompleter-setModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setModelSorting
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QCompleter.ModelSorting`
        :description: QtWidgets/QCompleter-setModelSorting-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setPopup
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
        :description: QtWidgets/QCompleter-setPopup-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QCompleter-setWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.setWrapAround
        :args:
            bool
        :description: QtWidgets/QCompleter-setWrapAround-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.splitPath
        :args:
            str
        :returns:
            List[str]
        :description: QtWidgets/QCompleter-splitPath-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.widget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QCompleter-widget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCompleter.wrapAround
        :returns:
            bool
        :description: QtWidgets/QCompleter-wrapAround-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QCompleter.activated
        :args:
            str
        :description: QtWidgets/QCompleter-activated-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QCompleter.activated
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QCompleter-activated-s-1.rst

    .. sip:signal:: PyQt6.QtWidgets.QCompleter.highlighted
        :args:
            str
        :description: QtWidgets/QCompleter-highlighted-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QCompleter.highlighted
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QCompleter-highlighted-s-1.rst
