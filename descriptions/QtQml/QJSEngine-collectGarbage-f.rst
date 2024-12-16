.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d70ab935279dd95eb62ce9714a2059b5

Runs the garbage collector.

The garbage collector will attempt to reclaim memory by locating and disposing of objects that are no longer reachable in the script environment.

Normally you don't need to call this function; the garbage collector will automatically be invoked when the :sip:ref:`~PyQt6.QtQml.QJSEngine` decides that it's wise to do so (i.e. when a certain number of new objects have been created). However, you can call this function to explicitly request that garbage collection should be performed as soon as possible.

.. seealso:: `Garbage Collection <https://doc.qt.io/qt-6/qtqml-javascript-memory.html#garbage-collection>`_, gc().
