.. sip:class-description::
    :status: todo
    :brief: A class for applying a QFileSelector to QML file loading
    :digest: a0f30a20cc4138b99ff44064d6058286

A class for applying a :sip:ref:`~PyQt6.QtCore.QFileSelector` to QML file loading.

:sip:ref:`~PyQt6.QtQml.QQmlFileSelector` will automatically apply a :sip:ref:`~PyQt6.QtCore.QFileSelector` to qml file and asset paths.

It is used as follows:

::

    QQmlEngine engine;
    QQmlFileSelector* selector = new QQmlFileSelector(&engine);

Then you can swap out files like so:

::

    main.qml
    Component.qml
    asset.png
    +unix/Component.qml
    +mac/asset.png

In this example, main.qml will normally use Component.qml for the Component type. However on a unix platform, the unix selector will be present and the +unix/Component.qml version will be used instead. Note that this acts like swapping out Component.qml with +unix/Component.qml, so when using Component.qml you should not need to alter any paths based on which version was selected.

For example, to pass the "asset.png" file path around you would refer to it just as "asset.png" in all of main.qml, Component.qml, and +linux/Component.qml. It will be replaced with +mac/asset.png on Mac platforms in all cases.

For a list of available selectors, see ``QFileSelector``.

Your platform may also provide additional selectors for you to use. As specified by :sip:ref:`~PyQt6.QtCore.QFileSelector`, directories used for selection must start with a '+' character, so you will not accidentally trigger this feature unless you have directories with such names inside your project.

If a new :sip:ref:`~PyQt6.QtQml.QQmlFileSelector` is set on the engine, the old one will be replaced. Use QQmlFileSelector::get() to query or use the existing instance.
