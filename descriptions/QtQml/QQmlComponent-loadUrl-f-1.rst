.. sip:method-description::
    :status: todo
    :pysig: 9321c4398c39804f52f213053f7e400b
    :realsig: (const QUrl&,QQmlComponent::CompilationMode)
    :digest: e8b77443cf4e1ad2dfa365b76c8e577e

Load the :sip:ref:`~PyQt6.QtQml.QQmlComponent` from the provided *url*. If *mode* is :sip:ref:`~PyQt6.QtQml.QQmlComponent.CompilationMode.Asynchronous`, the component will be loaded and compiled asynchronously.

Ensure that the URL provided is full and correct, in particular, use :sip:ref:`~PyQt6.QtCore.QUrl.fromLocalFile` when loading a file from the local filesystem.

Relative paths will be resolved against :sip:ref:`~PyQt6.QtQml.QQmlEngine.baseUrl`, which is the current working directory unless specified.
