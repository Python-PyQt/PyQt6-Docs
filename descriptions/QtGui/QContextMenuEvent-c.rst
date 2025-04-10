.. sip:class-description::
    :status: todo
    :brief: Contains parameters that describe a context menu event
    :digest: a7205a72e16c5170fe28d0411d0541b7

The :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` class contains parameters that describe a context menu event.

A context menu event is sent when a user performs an action that should open a contextual menu:

* clicking the right mouse button

* pressing a dedicated keyboard menu key (if the keyboard has one, such as the menu key on standard 104-key PC keyboards)

* pressing some other keyboard shortcut (such as "Ctrl+Return" by default on macOS 15 and newer)

The expected context menu should contain :sip:ref:`~PyQt6.QtGui.QAction` that are relevant to some content within the application (the "context"). In Qt, the context is at least the particular :sip:ref:`~PyQt6.QtWidgets.QWidget` or Qt Quick `Item <https://doc.qt.io/qt-6/qml-qtquick-item.html>`_ that receives the :sip:ref:`~PyQt6.QtGui.QContextMenuEvent`. If there is a selection, that should probably be treated as the context. The context can be further refined using :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.pos` to pinpoint the content within the widget, item or selection.

Widgets can override :sip:ref:`~PyQt6.QtWidgets.QWidget.contextMenuEvent` to handle this event. Many widgets already do that, and have useful context menus by default. Some widgets have a function such as :sip:ref:`~PyQt6.QtWidgets.QLineEdit.createStandardContextMenu` to populate the default set of actions into a :sip:ref:`~PyQt6.QtWidgets.QMenu`, which can be customized further in your subclass and then shown.

In Qt Quick, the event can be handled via the ContextMenu attached property. Some QtQuick.Controls Controls already provide context menus by default.

Unlike most synthetic events (such as a :sip:ref:`~PyQt6.QtGui.QMouseEvent` that is sent only after a :sip:ref:`~PyQt6.QtGui.QTouchEvent` or :sip:ref:`~PyQt6.QtGui.QTabletEvent` was not accepted), :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` is sent regardless of whether the original mouse or key event was already handled and :sip:ref:`~PyQt6.QtCore.QEvent.isAccepted`. This is to accommodate the Windows UI pattern of selecting some kind of items (icons, drawing elements, or cells in an Item View) using the right mouse button (clicking or dragging), and then getting a context menu as soon as you release the right mouse button. (The actions on the menu are meant to apply to the selection.) Therefore, on Windows the :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` is sent on mouse release; while on other platforms, it's sent on press. Qt follows the :sip:ref:`~PyQt6.QtGui.QStyleHints.contextMenuTrigger` by default.

There are also some Qt Quick Controls such as Pane that accept mouse events, and nevertheless receive a :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` after a mouse press or click.

If you prefer to support the press-drag-release UI pattern to open a context menu on press, and drag over a menu item to select it on release, you will need to do that by handling :sip:ref:`~PyQt6.QtGui.QMouseEvent` directly (by overriding :sip:ref:`~PyQt6.QtWidgets.QWidget.mousePressEvent` in :sip:ref:`~PyQt6.QtWidgets.QWidget` subclasses, or using `TapHandler <https://doc.qt.io/qt-6/qml-qtquick-taphandler.html>`_ to open a Menu in Qt Quick); and then the :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` will be redundant when the :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.reason` is ``Mouse``. You should ignore() the event in that case; but you should still ensure that the widget, custom control or application can respond to a :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` that :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.reason` the platform-specific keyboard shortcut.

When a :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` is ignored, Qt attempts to deliver it to other widgets and/or Items under the :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.pos` (which is usually translated from the cursor position).
