.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: f12784af08ec4f1c74f2bbd44769e70b

Returns the list of directories where the engine searches for native plugins for imported modules (referenced in the ``qmldir`` file).

By default, the list contains only ``.``, i.e. the engine searches in the directory of the ``qmldir`` file itself.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.addPluginPath`, :sip:ref:`~PyQt6.QtQml.QQmlEngine.setPluginPathList`.
