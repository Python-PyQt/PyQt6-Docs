.. sip:method-description::
    :status: todo
    :pysig: f0ef12c7ed86a8b8d56773ff098fc427
    :realsig: (const QString&, int, int)
    :digest: e056d83bccaa2974b374dc54b76e5f3e

Sets the commit string to *commitString*.

The commit string is the text that should get added to (or replace parts of) the text of the editor widget. It usually is a result of the input operations and has to be inserted to the widgets text directly before the preedit string.

If the commit string should replace parts of the text in the editor, *replaceLength* specifies the number of characters to be replaced. *replaceFrom* specifies the position at which characters are to be replaced relative from the start of the preedit string.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.commitString`, :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.replacementStart`, :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.replacementLength`.
