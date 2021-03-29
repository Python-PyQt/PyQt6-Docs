.. sip:method-description::
    :status: todo
    :pysig: afa7c3fd1523b1723d243fa47b96baf1
    :realsig: (QTextBlockUserData*)
    :digest: a8dd72ca6828ddb90e54a0ffce3350fa

Attaches the given *data* object to the text block.

:sip:ref:`~PyQt6.QtGui.QTextBlockUserData` can be used to store custom settings. The ownership is passed to the underlying text document, i.e. the provided :sip:ref:`~PyQt6.QtGui.QTextBlockUserData` object will be deleted if the corresponding text block gets deleted. The user data object is not stored in the undo history, so it will not be available after undoing the deletion of a text block.

For example, if you write a programming editor in an IDE, you may want to let your user set breakpoints visually in your code for an integrated debugger. In a programming editor a line of text usually corresponds to one :sip:ref:`~PyQt6.QtGui.QTextBlock`. The :sip:ref:`~PyQt6.QtGui.QTextBlockUserData` interface allows the developer to store data for each :sip:ref:`~PyQt6.QtGui.QTextBlock`, like for example in which lines of the source code the user has a breakpoint set. Of course this could also be stored externally, but by storing it inside the :sip:ref:`~PyQt6.QtGui.QTextDocument`, it will for example be automatically deleted when the user deletes the associated line. It's really just a way to store custom information in the :sip:ref:`~PyQt6.QtGui.QTextDocument` without using custom properties in :sip:ref:`~PyQt6.QtGui.QTextFormat` which would affect the undo/redo stack.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextBlock.userData`.
