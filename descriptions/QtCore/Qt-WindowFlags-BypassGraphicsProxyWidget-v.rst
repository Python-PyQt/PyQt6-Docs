.. sip:enum-member-description::
    :status: todo
    :value: 0x20000000
    :realname: Qt::WindowType::BypassGraphicsProxyWidget
    :digest: d80b4ef2605c399cbc4612cd7f097494

Prevents the window and its children from automatically embedding themselves into a QGraphicsProxyWidget if the parent widget is already embedded. You can set this flag if you want your widget to always be a toplevel widget on the desktop, regardless of whether the parent widget is embedded in a scene or not.
