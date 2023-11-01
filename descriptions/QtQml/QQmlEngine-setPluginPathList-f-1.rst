.. sip:method-description::
    :status: todo
    :pysig: 2e1e4fde32fc7292dbe8e18ea768734a
    :realsig: (const QStringList&)
    :digest: 6454032d66caaa81dcfb666f2b081805

Sets the list of directories where the engine searches for native plugins for imported modules (referenced in the ``qmldir`` file) to *paths*.

By default, the list contains only ``.``, i.e. the engine searches in the directory of the ``qmldir`` file itself.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.pluginPathList`, :sip:ref:`~PyQt6.QtQml.QQmlEngine.addPluginPath`.
