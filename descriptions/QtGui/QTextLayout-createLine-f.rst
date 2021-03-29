.. sip:method-description::
    :status: todo
    :pysig: 40fc2cc59e3e0b4dcd88ad252df53677
    :realsig: ()
    :digest: d6827f29fd234152be3210edf1975802

Returns a new text line to be laid out if there is text to be inserted into the layout; otherwise returns an invalid text line.

The text layout creates a new line object that starts after the last line in the layout, or at the beginning if the layout is empty. The layout maintains an internal cursor, and each line is filled with text from the cursor position onwards when the :sip:ref:`~PyQt6.QtGui.QTextLine.setLineWidth` function is called.

Once :sip:ref:`~PyQt6.QtGui.QTextLine.setLineWidth` is called, a new line can be created and filled with text. Repeating this process will lay out the whole block of text contained in the :sip:ref:`~PyQt6.QtGui.QTextLayout`. If there is no text left to be inserted into the layout, the :sip:ref:`~PyQt6.QtGui.QTextLine` returned will not be valid (isValid() will return false).
