:orphan:

.. sip:class:: PyQt6.QtGui.QUndoStack
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QUndoStack-c.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QUndoStack-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.beginMacro
        :args:
            str
        :description: QtGui/QUndoStack-beginMacro-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.canRedo
        :returns:
            bool
        :description: QtGui/QUndoStack-canRedo-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.canUndo
        :returns:
            bool
        :description: QtGui/QUndoStack-canUndo-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.cleanIndex
        :returns:
            int
        :description: QtGui/QUndoStack-cleanIndex-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.clear
        :description: QtGui/QUndoStack-clear-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.command
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QUndoCommand`
        :description: QtGui/QUndoStack-command-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.count
        :returns:
            int
        :description: QtGui/QUndoStack-count-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.createRedoAction
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            prefix: str = ''
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtGui/QUndoStack-createRedoAction-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.createUndoAction
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            prefix: str = ''
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtGui/QUndoStack-createUndoAction-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.endMacro
        :description: QtGui/QUndoStack-endMacro-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.index
        :returns:
            int
        :description: QtGui/QUndoStack-index-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.isActive
        :returns:
            bool
        :description: QtGui/QUndoStack-isActive-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.isClean
        :returns:
            bool
        :description: QtGui/QUndoStack-isClean-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.__len__
        :returns:
            int
        :description: QtGui/QUndoStack-__len__-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.push
        :args:
            :sip:ref:`~PyQt6.QtGui.QUndoCommand`
        :description: QtGui/QUndoStack-push-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.redo
        :description: QtGui/QUndoStack-redo-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.redoText
        :returns:
            str
        :description: QtGui/QUndoStack-redoText-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.resetClean
        :description: QtGui/QUndoStack-resetClean-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.setActive
        :args:
            active: bool = True
        :description: QtGui/QUndoStack-setActive-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.setClean
        :description: QtGui/QUndoStack-setClean-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.setIndex
        :args:
            int
        :description: QtGui/QUndoStack-setIndex-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.setUndoLimit
        :args:
            int
        :description: QtGui/QUndoStack-setUndoLimit-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.text
        :args:
            int
        :returns:
            str
        :description: QtGui/QUndoStack-text-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.undo
        :description: QtGui/QUndoStack-undo-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.undoLimit
        :returns:
            int
        :description: QtGui/QUndoStack-undoLimit-f.rst

    .. sip:method:: PyQt6.QtGui.QUndoStack.undoText
        :returns:
            str
        :description: QtGui/QUndoStack-undoText-f.rst

    .. sip:signal:: PyQt6.QtGui.QUndoStack.canRedoChanged
        :args:
            bool
        :description: QtGui/QUndoStack-canRedoChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QUndoStack.canUndoChanged
        :args:
            bool
        :description: QtGui/QUndoStack-canUndoChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QUndoStack.cleanChanged
        :args:
            bool
        :description: QtGui/QUndoStack-cleanChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QUndoStack.indexChanged
        :args:
            int
        :description: QtGui/QUndoStack-indexChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QUndoStack.redoTextChanged
        :args:
            str
        :description: QtGui/QUndoStack-redoTextChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QUndoStack.undoTextChanged
        :args:
            str
        :description: QtGui/QUndoStack-undoTextChanged-s.rst
