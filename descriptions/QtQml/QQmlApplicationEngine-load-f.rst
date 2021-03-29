.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: 7be85e4e2130a2a29df365f8e33e6162

Loads the root QML file located at *url*. The object tree defined by the file is created immediately for local file urls. Remote urls are loaded asynchronously, listen to the :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine.objectCreated` signal to determine when the object tree is ready.

If an error occurs, the :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine.objectCreated` signal is emitted with a null pointer as parameter and error messages are printed with :sip:ref:`~PyQt6.QtCore.qWarning`.
