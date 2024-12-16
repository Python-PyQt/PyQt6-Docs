:orphan:

.. sip:class:: PyQt6.QtGui.QUndoGroup
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QUndoGroup-c.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QUndoGroup-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.activeStack
        :returns:
            :sip:ref:`~PyQt6.QtGui.QUndoStack`
        :description: QtGui/QUndoGroup-activeStack-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.addStack
        :args:
            :sip:ref:`~PyQt6.QtGui.QUndoStack`
        :description: QtGui/QUndoGroup-addStack-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.canRedo
        :returns:
            bool
        :description: QtGui/QUndoGroup-canRedo-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.canUndo
        :returns:
            bool
        :description: QtGui/QUndoGroup-canUndo-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.createRedoAction
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            prefix: Optional[str] = ''
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtGui/QUndoGroup-createRedoAction-f-1.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.createUndoAction
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            prefix: Optional[str] = ''
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtGui/QUndoGroup-createUndoAction-f-1.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.isClean
        :returns:
            bool
        :description: QtGui/QUndoGroup-isClean-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.redo
        :description: QtGui/QUndoGroup-redo-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.redoText
        :returns:
            str
        :description: QtGui/QUndoGroup-redoText-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.removeStack
        :args:
            :sip:ref:`~PyQt6.QtGui.QUndoStack`
        :description: QtGui/QUndoGroup-removeStack-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.setActiveStack
        :args:
            :sip:ref:`~PyQt6.QtGui.QUndoStack`
        :description: QtGui/QUndoGroup-setActiveStack-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.stacks
        :returns:
            list[:sip:ref:`~PyQt6.QtGui.QUndoStack`]
        :description: QtGui/QUndoGroup-stacks-f-1.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.undo
        :description: QtGui/QUndoGroup-undo-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoGroup.undoText
        :returns:
            str
        :description: QtGui/QUndoGroup-undoText-f.rst

    .. sip:signal:: PyQt6.QtGui.QUndoGroup.activeStackChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QUndoStack`
        :description: QtGui/QUndoGroup-activeStackChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QUndoGroup.canRedoChanged
        :args:
            bool
        :description: QtGui/QUndoGroup-canRedoChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QUndoGroup.canUndoChanged
        :args:
            bool
        :description: QtGui/QUndoGroup-canUndoChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QUndoGroup.cleanChanged
        :args:
            bool
        :description: QtGui/QUndoGroup-cleanChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QUndoGroup.indexChanged
        :args:
            int
        :description: QtGui/QUndoGroup-indexChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QUndoGroup.redoTextChanged
        :args:
            Optional[str]
        :description: QtGui/QUndoGroup-redoTextChanged-s-1.rst

    .. sip:signal:: PyQt6.QtGui.QUndoGroup.undoTextChanged
        :args:
            Optional[str]
        :description: QtGui/QUndoGroup-undoTextChanged-s-1.rst
