.. sip:class-description::
    :status: todo
    :brief: Instances drive the progress of QQmlIncubators
    :digest: 3893f4837c71b010ae6f3af7dd408564

:sip:ref:`~PyQt6.QtQml.QQmlIncubationController` instances drive the progress of QQmlIncubators.

In order to behave asynchronously and not introduce stutters or freezes in an application, the process of creating objects a QQmlIncubators must be driven only during the application's idle time. :sip:ref:`~PyQt6.QtQml.QQmlIncubationController` allows the application to control exactly when, how often and for how long this processing occurs.

A :sip:ref:`~PyQt6.QtQml.QQmlIncubationController` derived instance should be created and set on a :sip:ref:`~PyQt6.QtQml.QQmlEngine` by calling the :sip:ref:`~PyQt6.QtQml.QQmlEngine.setIncubationController` method. Processing is then controlled by calling the :sip:ref:`~PyQt6.QtQml.QQmlIncubationController.incubateFor` or QQmlIncubationController::incubateWhile() methods as dictated by the application's requirements.

For example, this is an example of a incubation controller that will incubate for a maximum of 5 milliseconds out of every 16 milliseconds.

::

    class PeriodicIncubationController : public QObject,
                                         public QQmlIncubationController
    {
    public:
        PeriodicIncubationController() {
            startTimer(16);
        }

    protected:
        void timerEvent(QTimerEvent *) override {
            incubateFor(5);
        }
    };

Although the previous example would work, it is not optimal. Real world incubation controllers should try and maximize the amount of idle time they consume - rather than a static amount like 5 milliseconds - while not disturbing the application.
