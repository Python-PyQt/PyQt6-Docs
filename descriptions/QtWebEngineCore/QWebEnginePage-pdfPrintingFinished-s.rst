.. sip:signal-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&,bool)
    :digest: 3290f7a8e6dc580f4b581afc85638ba6

This signal is emitted when printing the web page into a PDF file has finished. *filePath* will contain the path the file was requested to be created at, and *success* will be ``true`` if the file was successfully created and ``false`` otherwise.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.printToPdf`.
