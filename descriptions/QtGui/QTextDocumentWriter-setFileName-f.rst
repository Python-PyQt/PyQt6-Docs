.. sip:method-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: 28b54aca5537d975b4da54aa470df042

Sets the name of the file to be written to *fileName*. Internally, :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter` will create a :sip:ref:`~PyQt6.QtCore.QFile` and open it in :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.WriteOnly` mode, and use this file when writing the document.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter.fileName`, :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter.setDevice`.
