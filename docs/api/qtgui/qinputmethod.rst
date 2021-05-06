:orphan:

.. sip:class:: PyQt6.QtGui.QInputMethod
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QInputMethod-c.rst

    .. sip:enum:: PyQt6.QtGui.QInputMethod.Action
        :description: QtGui/QInputMethod-Action-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputMethod.Action.Click
            :description: QtGui/QInputMethod-Action-Click-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputMethod.Action.ContextMenu
            :description: QtGui/QInputMethod-Action-ContextMenu-v.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.anchorRectangle
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QInputMethod-anchorRectangle-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.commit
        :description: QtGui/QInputMethod-commit-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.cursorRectangle
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QInputMethod-cursorRectangle-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.hide
        :description: QtGui/QInputMethod-hide-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.inputDirection
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.LayoutDirection`
        :description: QtGui/QInputMethod-inputDirection-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.inputItemClipRectangle
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QInputMethod-inputItemClipRectangle-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.inputItemRectangle
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QInputMethod-inputItemRectangle-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.inputItemTransform
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QInputMethod-inputItemTransform-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.invokeAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QInputMethod.Action`
            int
        :description: QtGui/QInputMethod-invokeAction-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.isAnimating
        :returns:
            bool
        :description: QtGui/QInputMethod-isAnimating-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.isVisible
        :returns:
            bool
        :description: QtGui/QInputMethod-isVisible-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.keyboardRectangle
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QInputMethod-keyboardRectangle-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.locale
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtGui/QInputMethod-locale-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.queryFocusObject
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery`
            Any
        :returns:
            Any
        :static:
        :description: QtGui/QInputMethod-queryFocusObject-f-1.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.reset
        :description: QtGui/QInputMethod-reset-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.setInputItemRectangle
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QInputMethod-setInputItemRectangle-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.setInputItemTransform
        :args:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QInputMethod-setInputItemTransform-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.setVisible
        :args:
            bool
        :description: QtGui/QInputMethod-setVisible-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.show
        :description: QtGui/QInputMethod-show-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethod.update
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery`
        :description: QtGui/QInputMethod-update-f-1.rst

    .. sip:signal:: PyQt6.QtGui.QInputMethod.anchorRectangleChanged
        :description: QtGui/QInputMethod-anchorRectangleChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QInputMethod.animatingChanged
        :description: QtGui/QInputMethod-animatingChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QInputMethod.cursorRectangleChanged
        :description: QtGui/QInputMethod-cursorRectangleChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QInputMethod.inputDirectionChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.LayoutDirection`
        :description: QtGui/QInputMethod-inputDirectionChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QInputMethod.inputItemClipRectangleChanged
        :description: QtGui/QInputMethod-inputItemClipRectangleChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QInputMethod.keyboardRectangleChanged
        :description: QtGui/QInputMethod-keyboardRectangleChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QInputMethod.localeChanged
        :description: QtGui/QInputMethod-localeChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QInputMethod.visibleChanged
        :description: QtGui/QInputMethod-visibleChanged-s.rst
