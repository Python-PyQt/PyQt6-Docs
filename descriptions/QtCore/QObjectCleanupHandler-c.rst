.. sip:class-description::
    :status: todo
    :brief: Watches the lifetime of multiple QObjects
    :digest: 0584a6dd0bff27eef0f9cb91faf84d03

The :sip:ref:`~PyQt6.QtCore.QObjectCleanupHandler` class watches the lifetime of multiple QObjects.

A :sip:ref:`~PyQt6.QtCore.QObjectCleanupHandler` is useful whenever you need to know when a number of :sip:ref:`~PyQt6.QtCore.QObject`\ s that are owned by someone else have been deleted. This is important, for example, when referencing memory in an application that has been allocated in a shared library.

To keep track of some :sip:ref:`~PyQt6.QtCore.QObject`\ s, create a :sip:ref:`~PyQt6.QtCore.QObjectCleanupHandler`, and :sip:ref:`~PyQt6.QtCore.QObjectCleanupHandler.add` the objects you are interested in. If you are no longer interested in tracking a particular object, use :sip:ref:`~PyQt6.QtCore.QObjectCleanupHandler.remove` to remove it from the cleanup handler. If an object being tracked by the cleanup handler gets deleted by someone else it will automatically be removed from the cleanup handler. You can delete all the objects in the cleanup handler with :sip:ref:`~PyQt6.QtCore.QObjectCleanupHandler.clear`, or by destroying the cleanup handler. :sip:ref:`~PyQt6.QtCore.QObjectCleanupHandler.isEmpty` returns ``true`` if the :sip:ref:`~PyQt6.QtCore.QObjectCleanupHandler` has no objects to keep track of.

.. seealso:: QPointer.
