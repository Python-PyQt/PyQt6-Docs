:orphan:

.. sip:class:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtDesigner/QDesignerFormWindowManagerInterface-c.rst

    .. sip:enum:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action
        :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-e.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.AdjustSizeAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-AdjustSizeAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.BreakLayoutAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-BreakLayoutAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.CopyAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-CopyAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.CutAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-CutAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.DefaultPreviewAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-DefaultPreviewAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.DeleteAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-DeleteAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.FormLayoutAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-FormLayoutAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.FormWindowSettingsDialogAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-FormWindowSettingsDialogAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.GridLayoutAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-GridLayoutAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.HorizontalLayoutAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-HorizontalLayoutAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.LowerAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-LowerAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.PasteAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-PasteAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.RaiseAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-RaiseAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.RedoAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-RedoAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.SelectAllAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-SelectAllAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.SimplifyLayoutAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-SimplifyLayoutAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.SplitHorizontalAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-SplitHorizontalAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.SplitVerticalAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-SplitVerticalAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.UndoAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-UndoAction-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action.VerticalLayoutAction
            :description: QtDesigner/QDesignerFormWindowManagerInterface-Action-VerticalLayoutAction-v.rst

    .. sip:enum:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.ActionGroup
        :description: QtDesigner/QDesignerFormWindowManagerInterface-ActionGroup-e.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.ActionGroup.StyledPreviewActionGroup
            :description: QtDesigner/QDesignerFormWindowManagerInterface-ActionGroup-StyledPreviewActionGroup-v.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtDesigner/QDesignerFormWindowManagerInterface-__init__-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.action
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.Action`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-action-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.actionFormLayout
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-actionFormLayout-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.actionGroup
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.ActionGroup`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QActionGroup`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-actionGroup-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.actionSimplifyLayout
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-actionSimplifyLayout-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.activeFormWindow
        :returns:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-activeFormWindow-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.addFormWindow
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-addFormWindow-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.closeAllPreviews
        :description: QtDesigner/QDesignerFormWindowManagerInterface-closeAllPreviews-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.core
        :returns:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-core-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.createFormWindow
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags` = Qt.WindowFlags()
        :returns:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-createFormWindow-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.formWindow
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-formWindow-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.formWindowCount
        :returns:
            int
        :description: QtDesigner/QDesignerFormWindowManagerInterface-formWindowCount-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.removeFormWindow
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-removeFormWindow-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.setActiveFormWindow
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-setActiveFormWindow-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.showPluginDialog
        :description: QtDesigner/QDesignerFormWindowManagerInterface-showPluginDialog-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.showPreview
        :description: QtDesigner/QDesignerFormWindowManagerInterface-showPreview-f.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.activeFormWindowChanged
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-activeFormWindowChanged-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.formWindowAdded
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-formWindowAdded-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.formWindowRemoved
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-formWindowRemoved-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.formWindowSettingsChanged
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :description: QtDesigner/QDesignerFormWindowManagerInterface-formWindowSettingsChanged-s.rst
