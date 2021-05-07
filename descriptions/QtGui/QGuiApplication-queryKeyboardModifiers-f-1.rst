.. sip:method-description::
    :status: todo
    :pysig: 03e4d442d9642f898f386cc81094eb19
    :realsig: ()
    :digest: 13decde1992e6b6accc62b85710e16c7

Queries and returns the state of the modifier keys on the keyboard. Unlike :sip:ref:`~PyQt6.QtGui.QGuiApplication.keyboardModifiers`, this method returns the actual keys held on the input device at the time of calling the method.

It does not rely on the keypress events having been received by this process, which makes it possible to check the modifiers while moving a window, for instance. Note that in most cases, you should use :sip:ref:`~PyQt6.QtGui.QGuiApplication.keyboardModifiers`, which is faster and more accurate since it contains the state of the modifiers as they were when the currently processed event was received.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.keyboardModifiers`.
