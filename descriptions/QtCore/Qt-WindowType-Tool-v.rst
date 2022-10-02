.. sip:enum-member-description::
    :status: todo
    :value: Popup | Dialog
    :digest: 4c6466cfa754f55a40de48497829cace

Indicates that the widget is a tool window. A tool window is often a small window with a smaller than usual title bar and decoration, typically used for collections of tool buttons. If there is a parent, the tool window will always be kept on top of it. If there isn't a parent, you may consider using Qt::WindowStaysOnTopHint as well. If the window system supports it, a tool window can be decorated with a somewhat lighter frame. It can also be combined with Qt::FramelessWindowHint. On macOS, tool windows correspond to the `NSPanel <https://developer.apple.com/documentation/appkit/nspanel>`_ class of windows. This means that the window lives on a level above normal windows making it impossible to put a normal window on top of it. By default, tool windows will disappear when the application is inactive. This can be controlled by the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_MacAlwaysShowToolWindow` attribute.
