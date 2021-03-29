.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: fab6786bccff71bbd6ede75907d37485

Clears all stored type registrations, such as those produced with :sip:ref:`~PyQt6.QtQml.qmlRegisterType`.

Do not call this function while a :sip:ref:`~PyQt6.QtQml.QQmlEngine` exists or behavior will be undefined. Any existing QQmlEngines must be deleted before calling this function. This function only affects the application global cache. Delete the :sip:ref:`~PyQt6.QtQml.QQmlEngine` to clear all cached data relating to that engine.
