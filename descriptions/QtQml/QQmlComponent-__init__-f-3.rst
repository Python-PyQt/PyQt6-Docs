.. sip:method-description::
    :status: todo
    :pysig: 6735334d5d4bd717a03fb5d0596d6eec
    :realsig: (QQmlEngine*,const QUrl&,QObject*)
    :digest: 95da80644a510d7b0897ad954e7d55a6

Create a :sip:ref:`~PyQt6.QtQml.QQmlComponent` from the given *url* and give it the specified *parent* and *engine*.

Ensure that the URL provided is full and correct, in particular, use :sip:ref:`~PyQt6.QtCore.QUrl.fromLocalFile` when loading a file from the local filesystem.

Relative paths will be resolved against :sip:ref:`~PyQt6.QtQml.QQmlEngine.baseUrl`, which is the current working directory unless specified.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.loadUrl`.
