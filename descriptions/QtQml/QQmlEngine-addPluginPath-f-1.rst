.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 1bfc0a2690b9a20f5efc786836cb7b54

Adds *path* as a directory where the engine searches for native plugins for imported modules (referenced in the ``qmldir`` file).

By default, the list contains only ``.``, i.e. the engine searches in the directory of the ``qmldir`` file itself.

The newly added *path* will be first in the :sip:ref:`~PyQt6.QtQml.QQmlEngine.pluginPathList`.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.setPluginPathList`.
