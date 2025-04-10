.. sip:class-description::
    :status: todo
    :brief: RAII convenience class for balanced QPainter::save() and QPainter::restore() calls
    :digest: a2dac5a4c4fb246171475129f856bdd1

The :sip:ref:`~PyQt6.QtGui.QPainterStateGuard` is a RAII convenience class for balanced :sip:ref:`~PyQt6.QtGui.QPainter.save` and :sip:ref:`~PyQt6.QtGui.QPainter.restore` calls.

:sip:ref:`~PyQt6.QtGui.QPainterStateGuard` should be used everywhere as a replacement for :sip:ref:`~PyQt6.QtGui.QPainter.save` to make sure that the corresponding :sip:ref:`~PyQt6.QtGui.QPainter.restore` is called upon finishing of the painting routine to avoid unbalanced calls between those two functions.

Example with :sip:ref:`~PyQt6.QtGui.QPainter.save`/\ :sip:ref:`~PyQt6.QtGui.QPainter.restore`:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainterstateguard.py
    :lines: 26-38

Example with :sip:ref:`~PyQt6.QtGui.QPainterStateGuard`:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainterstateguard.py
    :lines: 42-53

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter`.
