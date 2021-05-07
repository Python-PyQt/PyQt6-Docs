.. sip:class-description::
    :status: todo
    :brief: Represents a value on the JavaScript heap belonging to a QJSEngine
    :digest: 86990625a3e9ceede21e030a728a9fca

:sip:ref:`~PyQt6.QtQml.QJSManagedValue` represents a value on the JavaScript heap belonging to a :sip:ref:`~PyQt6.QtQml.QJSEngine`.

The :sip:ref:`~PyQt6.QtQml.QJSManagedValue` class allows interaction with JavaScript values in most ways you can interact with them from JavaScript itself. You can get and set properties and prototypes, and you can access arrays. Additionally, you can transform the value into the Qt counterparts of JavaScript objects. For example, a Url object may be transformed into a :sip:ref:`~PyQt6.QtCore.QUrl`.

A :sip:ref:`~PyQt6.QtQml.QJSManagedValue` is always bound to a particular :sip:ref:`~PyQt6.QtQml.QJSEngine`. You cannot use it independently. This means that you cannot have a :sip:ref:`~PyQt6.QtQml.QJSManagedValue` from one engine be a property or a proptotype of a :sip:ref:`~PyQt6.QtQml.QJSManagedValue` from a different engine.

In contrast to :sip:ref:`~PyQt6.QtQml.QJSValue`, almost all values held by :sip:ref:`~PyQt6.QtQml.QJSManagedValue` live on the JavaScript heap. There is no inline or unmanaged storage. Therefore, you can get the prototype of a primitive value, and you can get the ``length`` property of a string.

Only default-constructed or moved-from QJSManagedValues do not hold a value on the JavaScript heap. They represent ``undefined``, which doesn't have any properties or prototypes.

Also in contrast to :sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSManagedValue` does not catch any JavaScript exceptions. If an operation on a :sip:ref:`~PyQt6.QtQml.QJSManagedValue` causes an error, it will generally return an ``undefined`` value and :sip:ref:`~PyQt6.QtQml.QJSEngine.hasError` will return ``true`` afterwards. You can then catch the exception using :sip:ref:`~PyQt6.QtQml.QJSEngine.catchError`, or pass it up the stack, at your own discretion.

**Note:** As the reference to the value on the JavaScript heap has to be freed on destruction, you cannot move a :sip:ref:`~PyQt6.QtQml.QJSManagedValue` to a different thread. The destruction would take place in the new thread, which would create a race condition with the garbage collector on the original thread. This also means that you cannot hold a :sip:ref:`~PyQt6.QtQml.QJSManagedValue` beyond the lifespan of its engine.

The recommended way of working with a :sip:ref:`~PyQt6.QtQml.QJSManagedValue` is creating it on the stack, possibly by moving a :sip:ref:`~PyQt6.QtQml.QJSValue` and adding an engine, then performing the necessary operations on it, and finally moving it back into a :sip:ref:`~PyQt6.QtQml.QJSValue` for storage. Moving between :sip:ref:`~PyQt6.QtQml.QJSManagedValue` and :sip:ref:`~PyQt6.QtQml.QJSValue` is fast.
