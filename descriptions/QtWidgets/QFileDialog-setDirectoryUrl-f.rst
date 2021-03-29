.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: bf90afe0c3677ab49ff9b3cc83c54cb2

Sets the file dialog's current *directory* url.

**Note:** The non-native :sip:ref:`~PyQt6.QtWidgets.QFileDialog` supports only local files.

**Note:** On Windows, it is possible to pass URLs representing one of the *virtual folders*, such as "Computer" or "Network". This is done by passing a :sip:ref:`~PyQt6.QtCore.QUrl` using the scheme ``clsid`` followed by the CLSID value with the curly braces removed. For example the URL ``clsid:374DE290-123F-4565-9164-39C4925E467B`` denotes the download location. For a complete list of possible values, see the MSDN documentation on `KNOWNFOLDERID <https://msdn.microsoft.com/en-us/library/windows/desktop/dd378457.aspx>`_. This feature was added in Qt 5.5.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.directoryUrl`, :sip:ref:`~PyQt6.QtCore.QUuid`.
