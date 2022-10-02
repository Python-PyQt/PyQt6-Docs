.. sip:enum-description::
    :status: todo
    :digest: 42c84ec3fa50f6905263a593072f4fde

Specifies where URL interception is taking place.

Because QML loads qmldir files for locating types, there are two URLs involved in loading a QML type. The URL of the (possibly implicit) qmldir used for locating the type and the URL of the file which defines the type. Intercepting both leads to either complex URL replacement or double URL replacements for the same file.
