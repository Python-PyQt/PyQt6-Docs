:orphan:

.. sip:class:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface
    :description: QtDesigner/QDesignerFormWindowCursorInterface-c.rst

    .. sip:enum:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveMode
        :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveMode-e.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveMode.KeepAnchor
            :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveMode-KeepAnchor-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveMode.MoveAnchor
            :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveMode-MoveAnchor-v.rst

    .. sip:enum:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation
        :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveOperation-e.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation.Down
            :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveOperation-Down-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation.End
            :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveOperation-End-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation.Left
            :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveOperation-Left-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation.Next
            :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveOperation-Next-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation.NoMove
            :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveOperation-NoMove-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation.Prev
            :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveOperation-Prev-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation.Right
            :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveOperation-Right-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation.Start
            :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveOperation-Start-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation.Up
            :description: QtDesigner/QDesignerFormWindowCursorInterface-MoveOperation-Up-v.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.__init__
        :description: QtDesigner/QDesignerFormWindowCursorInterface-__init__-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.current
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowCursorInterface-current-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.formWindow
        :returns:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :description: QtDesigner/QDesignerFormWindowCursorInterface-formWindow-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.hasSelection
        :returns:
            bool
        :description: QtDesigner/QDesignerFormWindowCursorInterface-hasSelection-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.isWidgetSelected
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            bool
        :description: QtDesigner/QDesignerFormWindowCursorInterface-isWidgetSelected-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.movePosition
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation`
            mode: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveMode` = :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveMode.MoveAnchor`
        :returns:
            bool
        :description: QtDesigner/QDesignerFormWindowCursorInterface-movePosition-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.position
        :returns:
            int
        :description: QtDesigner/QDesignerFormWindowCursorInterface-position-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.resetWidgetProperty
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            Optional[str]
        :description: QtDesigner/QDesignerFormWindowCursorInterface-resetWidgetProperty-f-1.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.selectedWidget
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowCursorInterface-selectedWidget-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.selectedWidgetCount
        :returns:
            int
        :description: QtDesigner/QDesignerFormWindowCursorInterface-selectedWidgetCount-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.setPosition
        :args:
            int
            mode: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveMode` = :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveMode.MoveAnchor`
        :description: QtDesigner/QDesignerFormWindowCursorInterface-setPosition-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.setProperty
        :args:
            Optional[str]
            Any
        :description: QtDesigner/QDesignerFormWindowCursorInterface-setProperty-f-1.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.setWidgetProperty
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            Optional[str]
            Any
        :description: QtDesigner/QDesignerFormWindowCursorInterface-setWidgetProperty-f-1.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.widget
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowCursorInterface-widget-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.widgetCount
        :returns:
            int
        :description: QtDesigner/QDesignerFormWindowCursorInterface-widgetCount-f.rst
