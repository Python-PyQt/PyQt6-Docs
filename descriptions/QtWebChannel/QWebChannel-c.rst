.. sip:class-description::
    :status: todo
    :brief: Exposes QObjects to remote HTML clients
    :digest: 29b5dba37c9b4e894d867bf9b1577a36

Exposes QObjects to remote HTML clients.

The :sip:ref:`~PyQt6.QtWebChannel.QWebChannel` fills the gap between C++ applications and HTML/JavaScript applications. By publishing a :sip:ref:`~PyQt6.QtCore.QObject` derived object to a :sip:ref:`~PyQt6.QtWebChannel.QWebChannel` and using the `qwebchannel.js <https://doc.qt.io/qt-6/qtwebchannel-javascript.html>`_ on the HTML side, one can transparently access properties and public slots and methods of the :sip:ref:`~PyQt6.QtCore.QObject`. No manual message passing and serialization of data is required, property updates and signal emission on the C++ side get automatically transmitted to the potentially remotely running HTML clients. On the client side, a JavaScript object will be created for any published C++ :sip:ref:`~PyQt6.QtCore.QObject`. It mirrors the C++ object's API and thus is intuitively useable.

:sip:ref:`~PyQt6.QtWebChannel.QWebChannel` transparently supports QFuture. When a client calls a method that returns a QFuture, :sip:ref:`~PyQt6.QtWebChannel.QWebChannel` will send a response with the QFuture result only after the QFuture has finished.

Custom conversion of types to and from JSON is supported by defining converters with QMetaType::registerConverter() to and from :sip:ref:`~PyQt6.QtCore.QJsonValue`. Note that custom converters from :sip:ref:`~PyQt6.QtCore.QJsonValue` to a concrete type must fail if the :sip:ref:`~PyQt6.QtCore.QJsonValue` does not match the expected format. Otherwise :sip:ref:`~PyQt6.QtWebChannel.QWebChannel` cannot fall back to its default conversion mechanisms. Custom converters are also available on `the JavaScript side <https://doc.qt.io/qt-6/qtwebchannel-javascript.html>`_.

The C++ :sip:ref:`~PyQt6.QtWebChannel.QWebChannel` API makes it possible to talk to any HTML client, which could run on a local or even remote machine. The only limitation is that the HTML client supports the JavaScript features used by ``qwebchannel.js``. As such, one can interact with basically any modern HTML browser or standalone JavaScript runtime, such as node.js.

There also exists a declarative `WebChannel API <https://doc.qt.io/qt-6/qtwebchannel-qmlmodule.html>`_.

.. seealso:: `Qt WebChannel Standalone Example <https://doc.qt.io/qt-6/qtwebchannel-standalone-example.html>`_, `JavaScript API <https://doc.qt.io/qt-6/qtwebchannel-javascript.html>`_, QMetaType::registerConverter().
