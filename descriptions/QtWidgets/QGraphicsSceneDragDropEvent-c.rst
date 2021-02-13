.. sip:class-description::
    :status: todo
    :brief: Events for drag and drop in the graphics view framework
    :digest: 7c3a1b883d84f0881680aad9df98ee63

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent` class provides events for drag and drop in the graphics view framework.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsView` inherits the drag and drop functionality provided by `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_. When it receives a drag and drop event, it translates it to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent`.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent` stores events of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.GraphicsSceneDragEnter`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.GraphicsSceneDragLeave`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.GraphicsSceneDragMove`, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.GraphicsSceneDrop`.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent` contains the position of the mouse cursor in both item, scene, and screen coordinates; this can be retrieved with :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent.pos`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent.scenePos`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent.screenPos`.

The scene sends the event to the first :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` under the mouse cursor that accepts drops; a graphics item is set to accept drops with :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setAcceptDrops`.
