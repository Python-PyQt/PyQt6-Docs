.. sip:method-description::
    :status: todo
    :pysig: a16fc74df0b4b43d65e125206b1c2796
    :realsig: (const QColorSpace&)
    :digest: 207f17c5321c41e750ee5c19c299d0c2

Sets the output device profile to *profile*.

**Note:** PDF/X-4 requires all the color specifications in the document to match the same colorspace of *profile*. It is the application's responsibility to ensure this is the case.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPdfOutputIntent.outputProfile`, :sip:ref:`~PyQt6.QtGui.QColorSpace.fromIccProfile`, :sip:ref:`~PyQt6.QtGui.QPdfWriter.setColorModel`.
