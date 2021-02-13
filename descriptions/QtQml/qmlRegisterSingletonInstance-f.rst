.. sip:method-description::
    :status: todo
    :pysig: 1071d7a5200197d917c07c65ac597f15
    :realsig: (const char*,int,int,const char*,QObject*)
    :digest: 902b28debcb3f47d6bfe3378a29783e5

This function is used to register a singleton object *cppObject*, with a particular *uri* and *typeName*. Its version is a combination of *versionMajor* and *versionMinor*.

Installing a singleton type into a URI allows you to provide arbitrary functionality (methods and properties) to QML code without requiring individual instances of the type to be instantiated by the client.

Use this function to register an object of the given type T as a singleton type.

A :sip:ref:`~PyQt6.QtCore.QObject` singleton type may be referenced via the type name with which it was registered; in turn this type name may be used as the target in a `Connections <https://doc.qt.io/qt-6/qml-qtqml-connections.html>`_ type, or like any other type ID. However, there's one exception: a :sip:ref:`~PyQt6.QtCore.QObject` singleton type property can't be aliased because the singleton type name does not identify an object within the same component as any other item.

**Note:** *cppObject* must outlive the QML engine in which it is used. Moreover, cppObject must have the same thread affinity as the engine. If you want separate singleton instances for multiple engines, you need to use :sip:ref:`~PyQt6.QtQml.qmlRegisterSingletonType`. See Threads and QObjects for more information about thread safety.

Usage:

::

    // First, define your QObject which provides the functionality.
    class SingletonTypeExample : public QObject
    {
        Q_OBJECT
        Q_PROPERTY(int someProperty READ someProperty WRITE setSomeProperty NOTIFY somePropertyChanged)

    public:
        explicit SingletonTypeExample(QObject* parent = nullptr) : QObject(parent) {}

        Q_INVOKABLE int doSomething()
        {
            setSomeProperty(5);
            return m_someProperty;
        }

        int someProperty() const { return m_someProperty; }
        void setSomeProperty(int val) {
            if (m_someProperty != val) {
                m_someProperty = val;
                emit somePropertyChanged(val);
            }
        }

    signals:
        void somePropertyChanged(int newValue);

    private:
        int m_someProperty = 0;
    };

::

    // Second, create an instance of the object

    // allocate example before the engine to ensure that it outlives it
    QScopedPointer<SingletonTypeExample> example(new SingletonTypeExample);
    QQmlEngine engine;

    // Third, register the singleton type provider with QML by calling this
    // function in an initialization function.
    qmlRegisterSingletonInstance("Qt.example.qobjectSingleton", 1, 0, "MyApi", example.get());

In order to use the registered singleton type in QML, you must import the URI with the corresponding version.

.. seealso:: QML_SINGLETON, :sip:ref:`~PyQt6.QtQml.qmlRegisterSingletonType`.
