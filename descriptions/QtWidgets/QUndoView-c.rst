.. sip:class-description::
    :status: todo
    :brief: Displays the contents of a QUndoStack
    :digest: 7ce75db85f3ac5805625ce9ccec56490

The :sip:ref:`~PyQt6.QtWidgets.QUndoView` class displays the contents of a :sip:ref:`~PyQt6.QtGui.QUndoStack`.

:sip:ref:`~PyQt6.QtWidgets.QUndoView` is a :sip:ref:`~PyQt6.QtWidgets.QListView` which displays the list of commands pushed on an undo stack. The most recently executed command is always selected. Selecting a different command results in a call to :sip:ref:`~PyQt6.QtGui.QUndoStack.setIndex`, rolling the state of the document backwards or forward to the new command.

The stack can be set explicitly with :sip:ref:`~PyQt6.QtWidgets.QUndoView.setStack`. Alternatively, a :sip:ref:`~PyQt6.QtGui.QUndoGroup` object can be set with :sip:ref:`~PyQt6.QtWidgets.QUndoView.setGroup`. The view will then update itself automatically whenever the active stack of the group changes.

.. image:: ../../../images/qundoview.png
