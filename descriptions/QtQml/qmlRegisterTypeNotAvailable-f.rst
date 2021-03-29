.. sip:method-description::
    :status: todo
    :pysig: 5d0922dd69855ff0db399a5dda490578
    :realsig: (const char*,int,int,const char*,const QString&)
    :digest: 98351ddcecc071d936373dd69b790369

This function registers a type in the QML system with the name *qmlName*, in the type namespace imported from *uri* having the version number composed from *versionMajor* and *versionMinor*, but any attempt to instantiate the type will produce the given error *message*.

Normally, the types exported by a plugin should be fixed. However, if a C++ type is not available, you should at least "reserve" the QML type name, and give the user of the unavailable type a meaningful error message.

Returns the QML type id.

Example:

::

    #ifdef NO_GAMES_ALLOWED
    qmlRegisterTypeNotAvailable("MinehuntCore", 0, 1, "Game", "Get back to work, slacker!");
    #else
    qmlRegisterType<MinehuntGame>("MinehuntCore", 0, 1, "Game");
    #endif

This will cause any QML which imports the "MinehuntCore" type namespace and attempts to use the type to produce an error message:

::

    fun.qml: Get back to work, slacker!
       Game {
       ^

Without this, a generic "Game is not a type" message would be given.

.. seealso:: QML_UNAVAILABLE, :sip:ref:`~PyQt6.QtQml.qmlRegisterUncreatableType`, `Choosing the Correct Integration Method Between C++ and QML <https://doc.qt.io/qt-6/qtqml-cppintegration-overview.html#choosing-the-correct-integration-method-between-c-and-qml>`_.
