.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: 6454032d66caaa81dcfb666f2b081805

Sets the list of directories where the engine searches for native plugins for imported modules (referenced in the ``qmldir`` file) to *paths*.

By default, the list contains only ``.``, i.e. the engine searches in the directory of the ``qmldir`` file itself.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.pluginPathList`, :sip:ref:`~PyQt6.QtQml.QQmlEngine.addPluginPath`.
