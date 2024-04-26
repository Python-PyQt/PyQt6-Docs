.. sip:class-description::
    :status: todo
    :brief: Allows QML objects to be created asynchronously
    :digest: 2b8caff2e22e9aa94910b4e635904946

The :sip:ref:`~PyQt6.QtQml.QQmlIncubator` class allows QML objects to be created asynchronously.

Creating QML objects - like delegates in a view, or a new page in an application - can take a noticeable amount of time, especially on resource constrained mobile devices. When an application uses :sip:ref:`~PyQt6.QtQml.QQmlComponent.create` directly, the QML object instance is created synchronously which, depending on the complexity of the object, can cause noticeable pauses or stutters in the application.

The use of :sip:ref:`~PyQt6.QtQml.QQmlIncubator` gives more control over the creation of a QML object, including allowing it to be created asynchronously using application idle time. The following example shows a simple use of :sip:ref:`~PyQt6.QtQml.QQmlIncubator`.

::

    // Initialize the incubator
    QQmlIncubator incubator;
    component->create(incubator);

Let the incubator run for a while (normally by returning control to the event loop), then poll it. There are a number of ways to get back to the incubator later. You may want to connect to one of the signals sent by :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, or you may want to run a :sip:ref:`~PyQt6.QtCore.QTimer` especially for that. You may also need the object for some specific purpose and poll the incubator when that purpose arises.

::

    // Poll the incubator
    if (incubator.isReady()) {
        QObject *object = incubator.object();
        // Use created object
    }

Asynchronous incubators are controlled by a :sip:ref:`~PyQt6.QtQml.QQmlIncubationController` that is set on the :sip:ref:`~PyQt6.QtQml.QQmlEngine`, which lets the engine know when the application is idle and incubating objects should be processed. If an incubation controller is not set on the :sip:ref:`~PyQt6.QtQml.QQmlEngine`, :sip:ref:`~PyQt6.QtQml.QQmlIncubator` creates objects synchronously regardless of the specified :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode.IncubationMode`. By default, no incubation controller is set. However, :sip:ref:`~PyQt6.QtQuick.QQuickView`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow` and :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` all set incubation controllers on their respective :sip:ref:`~PyQt6.QtQml.QQmlEngine`\ s. These incubation controllers space out incubations across multiple frames while the view is being rendered.

:sip:ref:`~PyQt6.QtQml.QQmlIncubator` supports three incubation modes:

* Synchronous The creation occurs synchronously. That is, once the :sip:ref:`~PyQt6.QtQml.QQmlComponent.create` call returns, the incubator will already be in either the Error or Ready state. A synchronous incubator has no real advantage compared to using the synchronous creation methods on :sip:ref:`~PyQt6.QtQml.QQmlComponent` directly, but it may simplify an application's implementation to use the same API for both synchronous and asynchronous creations.

* Asynchronous (default) The creation occurs asynchronously, assuming a QQmlIncubatorController is set on the :sip:ref:`~PyQt6.QtQml.QQmlEngine`.

  The incubator will remain in the Loading state until either the creation is complete or an error occurs. The :sip:ref:`~PyQt6.QtQml.QQmlIncubator.statusChanged` callback can be used to be notified of status changes.

  Applications should use the Asynchronous incubation mode to create objects that are not needed immediately. For example, the `ListView <https://doc.qt.io/qt-6/qml-qtquick-listview.html>`_ type uses Asynchronous incubation to create objects that are slightly off screen while the list is being scrolled. If, during asynchronous creation, the object is needed immediately the :sip:ref:`~PyQt6.QtQml.QQmlIncubator.forceCompletion` method can be called to complete the creation process synchronously.

* :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode.AsynchronousIfNested` The creation will occur asynchronously if part of a nested asynchronous creation, or synchronously if not.

  In most scenarios where a QML component wants the appearance of a synchronous instantiation, it should use this mode.

  This mode is best explained with an example. When the `ListView <https://doc.qt.io/qt-6/qml-qtquick-listview.html>`_ type is first created, it needs to populate itself with an initial set of delegates to show. If the `ListView <https://doc.qt.io/qt-6/qml-qtquick-listview.html>`_ was 400 pixels high, and each delegate was 100 pixels high, it would need to create four initial delegate instances. If the `ListView <https://doc.qt.io/qt-6/qml-qtquick-listview.html>`_ used the Asynchronous incubation mode, the `ListView <https://doc.qt.io/qt-6/qml-qtquick-listview.html>`_ would always be created empty and then, sometime later, the four initial items would appear.

  Conversely, if the `ListView <https://doc.qt.io/qt-6/qml-qtquick-listview.html>`_ was to use the Synchronous incubation mode it would behave correctly but it may introduce stutters into the application. As QML would have to stop and instantiate the `ListView <https://doc.qt.io/qt-6/qml-qtquick-listview.html>`_'s delegates synchronously, if the `ListView <https://doc.qt.io/qt-6/qml-qtquick-listview.html>`_ was part of a QML component that was being instantiated asynchronously this would undo much of the benefit of asynchronous instantiation.

  The :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode.AsynchronousIfNested` mode reconciles this problem. By using :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode.AsynchronousIfNested`, the `ListView <https://doc.qt.io/qt-6/qml-qtquick-listview.html>`_ delegates are instantiated asynchronously if the `ListView <https://doc.qt.io/qt-6/qml-qtquick-listview.html>`_ itself is already part of an asynchronous instantiation, and synchronously otherwise. In the case of a nested asynchronous instantiation, the outer asynchronous instantiation will not complete until after all the nested instantiations have also completed. This ensures that by the time the outer asynchronous instantitation completes, inner items like `ListView <https://doc.qt.io/qt-6/qml-qtquick-listview.html>`_ have already completed loading their initial delegates.

  It is almost always incorrect to use the Synchronous incubation mode - elements or components that want the appearance of synchronous instantiation, but without the downsides of introducing freezes or stutters into the application, should use the :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode.AsynchronousIfNested` incubation mode.
