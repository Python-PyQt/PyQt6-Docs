.. sip:class-description::
    :status: todo
    :brief: Enables logging of OpenGL debugging messages
    :digest: 29caa2bdacdcf38795e3a019c833375d

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger` enables logging of OpenGL debugging messages.

.. _qopengldebuglogger-introduction:

Introduction
------------

OpenGL programming can be very error prone. Most of the time, a single failing call to OpenGL can cause an entire portion of an application to stop working, with nothing being drawn on the screen.

The only way to be sure that no errors are being returned from the OpenGL implementation is checking with ``glGetError`` after each and every API call. Moreover, OpenGL errors stack up, therefore glGetError should always be used in a loop like this:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_opengl_qopengldebug.py
    :lines: 74-80

If you try to clear the error stack, make sure not just keep going until GL_NO_ERROR is returned but also break on GL_CONTEXT_LOST as that error value will keep repeating.

There are also many other information we are interested in (as application developers), for instance performance issues, or warnings about using deprecated APIs. Those kind of messages are not reported through the ordinary OpenGL error reporting mechanisms.

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger` aims at addressing these issues by providing access to the *OpenGL debug log*. If your OpenGL implementation supports it (by exposing the ``GL_KHR_debug`` extension), messages from the OpenGL server will be either logged in an internal OpenGL log, or passed in "real-time" to listeners as they're generated from OpenGL.

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger` supports both these modes of operation. Refer to the following sections to find out the differences between them.

.. _qopengldebuglogger-creating-an-opengl-debug-context:

Creating an OpenGL Debug Context
--------------------------------

For efficiency reasons, OpenGL implementations are allowed not to create any debug output at all, unless the OpenGL context is a debug context. In order to create a debug context from Qt, you must set the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.FormatOptions.DebugContext` format option on the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` used to create the `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ object:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_opengl_qopengldebug.py
    :lines: 85-94

Note that requesting a 3.2 OpenGL Core Profile is just for the example's purposes; this class is not tied to any specific OpenGL or OpenGL ES version, as it relies on the availability of the ``GL_KHR_debug`` extension (see below).

.. _qopengldebuglogger-creating-and-initializing-a-qopengldebuglogger:

Creating and Initializing a QOpenGLDebugLogger
----------------------------------------------

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger` is a simple :sip:ref:`~PyQt6.QtCore.QObject`-derived class. Just like all :sip:ref:`~PyQt6.QtCore.QObject` subclasses, you create an instance (and optionally specify a parent object), and like the other OpenGL functions in Qt you *must* initialize it before usage by calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.initialize` whilst there is a current OpenGL context:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_opengl_qopengldebug.py
    :lines: 102-105

Note that the ``GL_KHR_debug`` extension *must* be available in the context in order to access the messages logged by OpenGL. You can check the presence of this extension by calling:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_opengl_qopengldebug.py
    :lines: 110-110

where ``ctx`` is a valid `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_. If the extension is not available, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.initialize` will return false.

.. _qopengldebuglogger-reading-the-internal-opengl-debug-log:

Reading the Internal OpenGL Debug Log
-------------------------------------

OpenGL implementations keep an internal log of debug messages. Messages stored in this log can be retrieved by using the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.loggedMessages` function:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_opengl_qopengldebug.py
    :lines: 115-117

The internal log has a limited size; when it fills up, older messages will get discarded to make room for the new incoming messages. When you call :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.loggedMessages`, the internal log will be emptied as well.

If you want to be sure not to lose any debug message, you must use real-time logging instead of calling this function. However, debug messages might still be generated in the timespan between context creation and activation of real-time logging (or, in general, when the real-time logging is disabled).

.. _qopengldebuglogger-real-time-logging-of-messages:

Real-time logging of messages
-----------------------------

It is also possible to receive a stream of debug messages from the OpenGL server *as they are generated* by the implementation. In order to do so, you need to connect a suitable slot to the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.messageLogged` signal, and start logging by calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.startLogging`:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_opengl_qopengldebug.py
    :lines: 122-123

Similarly, logging can be disabled at any time by calling the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.stopLogging` function.

Real-time logging can be either asynchronous or synchronous, depending on the parameter passed to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.startLogging`. When logging in asynchronous mode (the default, as it has a very small overhead), the OpenGL implementation can generate messages at any time, and/or in an order which is different from the order of the OpenGL commands which caused those messages to be logged. The messages could also be generated from a thread that it's different from the thread the context is currently bound to. This is because OpenGL implementations are usually highly threaded and asynchronous, and therefore no warranties are made about the relative order and the timings of the debug messages.

On the other hand, logging in synchronous mode has a high overhead, but the OpenGL implementation guarantees that all the messages caused by a certain command are received in order, before the command returns, and from the same thread the OpenGL context is bound to.

This means that when logging in synchronous mode you will be able to run your OpenGL application in a debugger, put a breakpoint on a slot connected to the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.messageLogged` signal, and see in the backtrace the exact call that caused the logged message. This can be extremely useful to debug an OpenGL problem. Note that if OpenGL rendering is happening in another thread, you must force the signal/slot connection type to :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.DirectConnection` in order to be able to see the actual backtrace.

Refer to the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.LoggingMode.LoggingMode` enum documentation for more information about logging modes.

**Note:** When real-time logging is enabled, debug messages will *not* be inserted in the internal OpenGL debug log any more; messages already present in the internal log will not be deleted, nor they will be emitted through the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.messageLogged` signal. Since some messages might be generated before real-time logging is started (and therefore be kept in the internal OpenGL log), it is important to always check if it contains any message after calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.startLogging`.

.. _qopengldebuglogger-inserting-messages-in-the-debug-log:

Inserting Messages in the Debug Log
-----------------------------------

It is possible for applications and libraries to insert custom messages in the debug log, for instance for marking a group of related OpenGL commands and therefore being then able to identify eventual messages coming from them.

In order to do so, you can create a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage` object by calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.createApplicationMessage` or :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.createThirdPartyMessage`, and then inserting it into the log by calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.logMessage`:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_opengl_qopengldebug.py
    :lines: 128-131

Note that OpenGL implementations have a vendor-specific limit to the length of the messages that can be inserted in the debug log. You can retrieve this length by calling the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.maximumMessageLength` method; messages longer than the limit will automatically get truncated.

.. _qopengldebuglogger-controlling-the-debug-output:

Controlling the Debug Output
----------------------------

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage` is also able to apply filters to the debug messages, and therefore limit the amount of messages logged. You can enable or disable logging of messages by calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.enableMessages` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.disableMessages` respectively. By default, all messages are logged.

It is possible to enable or disable messages by selecting them by:

* source, type and severity (and including all ids in the selection);

* id, source and type (and including all severities in the selection).

Note that the "enabled" status for a given message is a property of the (id, source, type, severity) tuple; the message attributes *do not* form a hierarchy of any kind. You should be careful about the order of the calls to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.enableMessages` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.disableMessages`, as it will change which messages will are enabled / disabled.

It's not possible to filter by the message text itself; applications have to do that on their own (in slots connected to the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.messageLogged` signal, or after fetching the messages in the internal debug log through :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.loggedMessages`).

In order to simplify the management of the enabled / disabled statuses, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage` also supports the concept of ``debug groups``. A debug group contains the group of enabled / disabled configurations of debug messages. Moreover, debug groups are organized in a stack: it is possible to push and pop groups by calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.pushGroup` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.popGroup` respectively. (When an OpenGL context is created, there is already a group in the stack).

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.enableMessages` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.disableMessages` functions will modify the configuration in the current debug group, that is, the one at the top of the debug groups stack.

When a new group is pushed onto the debug groups stack, it will inherit the configuration of the group that was previously on the top of the stack. Vice versa, popping a debug group will restore the configuration of the debug group that becomes the new top.

Pushing (respectively popping) debug groups will also automatically generate a debug message of type :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.GroupPushType` (respectively :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.GroupPopType`).

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage`.
