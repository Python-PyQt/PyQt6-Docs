.. sip:method-description::
    :status: todo
    :pysig: 8a6f025d8c5b11da8ad12739d643a9e4
    :realsig: (QQmlEngine*,const QUrl&,QQmlComponent::CompilationMode,QObject*)
    :digest: 118aab60cf5324eb1cbb0c3b051f93d4

Create a :sip:ref:`~PyQt6.QtQml.QQmlComponent` from the given *url* and give it the specified *parent* and *engine*. If *mode* is :sip:ref:`~PyQt6.QtQml.QQmlComponent.CompilationMode.Asynchronous`, the component will be loaded and compiled asynchronously.

Ensure that the URL provided is full and correct, in particular, use :sip:ref:`~PyQt6.QtCore.QUrl.fromLocalFile` when loading a file from the local filesystem.

Relative paths will be resolved against :sip:ref:`~PyQt6.QtQml.QQmlEngine.baseUrl`, which is the current working directory unless specified.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.loadUrl`.
