.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 2c6521bc3e70e7e4ac68aad34bd686c4

Clears all singletons the engine owns.

This function drops all singleton instances, deleting any QObjects owned by the engine among them. This is useful to make sure that no QML-created objects are left before calling :sip:ref:`~PyQt6.QtQml.QQmlEngine.clearComponentCache`.

QML properties holding :sip:ref:`~PyQt6.QtCore.QObject`-based singleton instances become null if the engine owns the singleton or retain their value if the engine doesn't own it. The singletons are not automatically re-created by accessing existing QML-created objects. Only when new components are instantiated, the singletons are re-created.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.clearComponentCache`.
