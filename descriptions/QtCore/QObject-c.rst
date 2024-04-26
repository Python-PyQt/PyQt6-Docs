.. sip:class-description::
    :status: todo
    :brief: The base class of all Qt objects
    :digest: 9c5cab9e21f33e8e787304ee2fe39768

The :sip:ref:`~PyQt6.QtCore.QObject` class is the base class of all Qt objects.

:sip:ref:`~PyQt6.QtCore.QObject` is the heart of the Qt `Object Model <https://doc.qt.io/qt-6/object.html>`_. The central feature in this model is a very powerful mechanism for seamless object communication called `signals and slots <https://doc.qt.io/qt-6/signalsandslots.html>`_. You can connect a signal to a slot with connect() and destroy the connection with :sip:ref:`~PyQt6.QtCore.QObject.disconnect`. To avoid never ending notification loops you can temporarily block signals with :sip:ref:`~PyQt6.QtCore.QObject.blockSignals`. The protected functions :sip:ref:`~PyQt6.QtCore.QObject.connectNotify` and :sip:ref:`~PyQt6.QtCore.QObject.disconnectNotify` make it possible to track connections.

QObjects organize themselves in `object trees <https://doc.qt.io/qt-6/objecttrees.html>`_. When you create a :sip:ref:`~PyQt6.QtCore.QObject` with another object as parent, the object will automatically add itself to the parent's :sip:ref:`~PyQt6.QtCore.QObject.children` list. The parent takes ownership of the object; i.e., it will automatically delete its children in its destructor. You can look for an object by name and optionally type using :sip:ref:`~PyQt6.QtCore.QObject.findChild` or :sip:ref:`~PyQt6.QtCore.QObject.findChildren`.

Every object has an :sip:ref:`~PyQt6.QtCore.QObject.objectName` and its class name can be found via the corresponding :sip:ref:`~PyQt6.QtCore.QObject.metaObject` (see :sip:ref:`~PyQt6.QtCore.QMetaObject.className`). You can determine whether the object's class inherits another class in the :sip:ref:`~PyQt6.QtCore.QObject` inheritance hierarchy by using the :sip:ref:`~PyQt6.QtCore.QObject.inherits` function.

When an object is deleted, it emits a :sip:ref:`~PyQt6.QtCore.QObject.destroyed` signal. You can catch this signal to avoid dangling references to QObjects.

QObjects can receive events through :sip:ref:`~PyQt6.QtCore.QObject.event` and filter the events of other objects. See :sip:ref:`~PyQt6.QtCore.QObject.installEventFilter` and :sip:ref:`~PyQt6.QtCore.QObject.eventFilter` for details. A convenience handler, :sip:ref:`~PyQt6.QtCore.QObject.childEvent`, can be reimplemented to catch child events.

Last but not least, :sip:ref:`~PyQt6.QtCore.QObject` provides the basic timer support in Qt; see :sip:ref:`~PyQt6.QtCore.QTimer` for high-level support for timers.

Notice that the Q_OBJECT macro is mandatory for any object that implements signals, slots or properties. You also need to run the Meta Object Compiler on the source file. We strongly recommend the use of this macro in all subclasses of :sip:ref:`~PyQt6.QtCore.QObject` regardless of whether or not they actually use signals, slots and properties, since failure to do so may lead certain functions to exhibit strange behavior.

All Qt widgets inherit :sip:ref:`~PyQt6.QtCore.QObject`. The convenience function :sip:ref:`~PyQt6.QtCore.QObject.isWidgetType` returns whether an object is actually a widget. It is much faster than qobject_cast<\ :sip:ref:`~PyQt6.QtWidgets.QWidget` \*>(\ *obj*) or *obj*->\ :sip:ref:`~PyQt6.QtCore.QObject.inherits`\ ("\ :sip:ref:`~PyQt6.QtWidgets.QWidget`").

Some :sip:ref:`~PyQt6.QtCore.QObject` functions, e.g. :sip:ref:`~PyQt6.QtCore.QObject.children`, return a QObjectList. QObjectList is a typedef for QList<\ :sip:ref:`~PyQt6.QtCore.QObject` \*>.

.. _qobject-thread-affinity:

Thread Affinity
---------------

A :sip:ref:`~PyQt6.QtCore.QObject` instance is said to have a *thread affinity*, or that it *lives* in a certain thread. When a :sip:ref:`~PyQt6.QtCore.QObject` receives a :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection` or a `posted event <https://doc.qt.io/qt-6/eventsandfilters.html#sending-events>`_, the slot or event handler will run in the thread that the object lives in.

**Note:** If a :sip:ref:`~PyQt6.QtCore.QObject` has no thread affinity (that is, if :sip:ref:`~PyQt6.QtCore.QObject.thread` returns zero), or if it lives in a thread that has no running event loop, then it cannot receive queued signals or posted events.

By default, a :sip:ref:`~PyQt6.QtCore.QObject` lives in the thread in which it is created. An object's thread affinity can be queried using :sip:ref:`~PyQt6.QtCore.QObject.thread` and changed using :sip:ref:`~PyQt6.QtCore.QObject.moveToThread`.

All QObjects must live in the same thread as their parent. Consequently:

* :sip:ref:`~PyQt6.QtCore.QObject.setParent` will fail if the two QObjects involved live in different threads.

* When a :sip:ref:`~PyQt6.QtCore.QObject` is moved to another thread, all its children will be automatically moved too.

* :sip:ref:`~PyQt6.QtCore.QObject.moveToThread` will fail if the :sip:ref:`~PyQt6.QtCore.QObject` has a parent.

* If QObjects are created within :sip:ref:`~PyQt6.QtCore.QThread.run`, they cannot become children of the :sip:ref:`~PyQt6.QtCore.QThread` object because the :sip:ref:`~PyQt6.QtCore.QThread` does not live in the thread that calls :sip:ref:`~PyQt6.QtCore.QThread.run`.

**Note:** A :sip:ref:`~PyQt6.QtCore.QObject`'s member variables *do not* automatically become its children. The parent-child relationship must be set by either passing a pointer to the child's :sip:ref:`~PyQt6.QtCore.QObject`, or by calling :sip:ref:`~PyQt6.QtCore.QObject.setParent`. Without this step, the object's member variables will remain in the old thread when :sip:ref:`~PyQt6.QtCore.QObject.moveToThread` is called.

.. _qobject-no-copy-constructor:

.. _qobject-no-copy-constructor-or-assignment-operator:

No Copy Constructor or Assignment Operator
------------------------------------------

:sip:ref:`~PyQt6.QtCore.QObject` has neither a copy constructor nor an assignment operator. This is by design. Actually, they are declared, but in a ``private`` section with the macro Q_DISABLE_COPY(). In fact, all Qt classes derived from :sip:ref:`~PyQt6.QtCore.QObject` (direct or indirect) use this macro to declare their copy constructor and assignment operator to be private. The reasoning is found in the discussion on `Identity vs Value <https://doc.qt.io/qt-6/object.html#identity-vs-value>`_ on the Qt `Object Model <https://doc.qt.io/qt-6/object.html>`_ page.

The main consequence is that you should use pointers to :sip:ref:`~PyQt6.QtCore.QObject` (or to your :sip:ref:`~PyQt6.QtCore.QObject` subclass) where you might otherwise be tempted to use your :sip:ref:`~PyQt6.QtCore.QObject` subclass as a value. For example, without a copy constructor, you can't use a subclass of :sip:ref:`~PyQt6.QtCore.QObject` as the value to be stored in one of the container classes. You must store pointers.

.. _qobject-auto-connection:

Auto-Connection
---------------

Qt's meta-object system provides a mechanism to automatically connect signals and slots between :sip:ref:`~PyQt6.QtCore.QObject` subclasses and their children. As long as objects are defined with suitable object names, and slots follow a simple naming convention, this connection can be performed at run-time by the :sip:ref:`~PyQt6.QtCore.QMetaObject.connectSlotsByName` function.

uic generates code that invokes this function to enable auto-connection to be performed between widgets on forms created with *Qt Designer*. More information about using auto-connection with *Qt Designer* is given in the `Using a Designer UI File in Your Application <https://doc.qt.io/qt-6/designer-using-a-ui-file.html>`_ section of the *Qt Designer* manual.

.. _qobject-dynamic-properties:

Dynamic Properties
------------------

Dynamic properties can be added to and removed from :sip:ref:`~PyQt6.QtCore.QObject` instances at run-time. Dynamic properties do not need to be declared at compile-time, yet they provide the same advantages as static properties and are manipulated using the same API - using :sip:ref:`~PyQt6.QtCore.QObject.property` to read them and :sip:ref:`~PyQt6.QtCore.QObject.setProperty` to write them.

Dynamic properties are supported by `Qt Designer <https://doc.qt.io/qt-6/designer-widget-mode.html#the-property-editor>`_, and both standard Qt widgets and user-created forms can be given dynamic properties.

.. _qobject-internationalization-i18n:

Internationalization (I18n)
---------------------------

All :sip:ref:`~PyQt6.QtCore.QObject` subclasses support Qt's translation features, making it possible to translate an application's user interface into different languages.

To make user-visible text translatable, it must be wrapped in calls to the :sip:ref:`~PyQt6.QtCore.QObject.tr` function. This is explained in detail in the Writing Source Code for Translation document.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject`, QPointer, :sip:ref:`~PyQt6.QtCore.QObjectCleanupHandler`, Q_DISABLE_COPY(), `Object Trees & Ownership <https://doc.qt.io/qt-6/objecttrees.html>`_.
