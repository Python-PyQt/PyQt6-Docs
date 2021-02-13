.. sip:enum-member-description::
    :status: todo
    :value: 51
    :digest: fd1425f1e965ba019c0d95d6618b4061

Key press in child, for overriding shortcut key handling (\ :sip:ref:`~PyQt6.QtGui.QKeyEvent`). When a shortcut is about to trigger, ``ShortcutOverride`` is sent to the active window. This allows clients (e.g. widgets) to signal that they will handle the shortcut themselves, by accepting the event. If the shortcut override is accepted, the event is delivered as a normal key press to the focus widget. Otherwise, it triggers the shortcut action, if one exists.
