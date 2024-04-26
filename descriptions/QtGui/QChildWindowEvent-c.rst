.. sip:class-description::
    :status: todo
    :brief: Contains event parameters for child window changes
    :digest: 080b87fcbe49c1ee0a7c9d0214aea39b

The :sip:ref:`~PyQt6.QtGui.QChildWindowEvent` class contains event parameters for child window changes.

Child window events are sent to windows when children are added or removed.

In both cases you can only rely on the child being a :sip:ref:`~PyQt6.QtGui.QWindow` — not any subclass thereof. This is because in the :sip:ref:`~PyQt6.QtCore.QEvent.Type.ChildWindowAdded` case the subclass is not yet fully constructed, and in the :sip:ref:`~PyQt6.QtCore.QEvent.Type.ChildWindowRemoved` case it might have already been destructed.
