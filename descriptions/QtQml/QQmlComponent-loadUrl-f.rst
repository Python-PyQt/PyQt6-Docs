.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: d7f69e0d12f4400895ef383a474185bc

Load the :sip:ref:`~PyQt6.QtQml.QQmlComponent` from the provided *url*.

Ensure that the URL provided is full and correct, in particular, use :sip:ref:`~PyQt6.QtCore.QUrl.fromLocalFile` when loading a file from the local filesystem.

Relative paths will be resolved against :sip:ref:`~PyQt6.QtQml.QQmlEngine.baseUrl`, which is the current working directory unless specified.
