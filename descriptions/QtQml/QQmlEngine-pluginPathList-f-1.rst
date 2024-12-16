.. sip:method-description::
    :status: todo
    :pysig: 3c9a938a1e983dbe538fd869f2db5e67
    :realsig: () const
    :digest: f12784af08ec4f1c74f2bbd44769e70b

Returns the list of directories where the engine searches for native plugins for imported modules (referenced in the ``qmldir`` file).

By default, the list contains only ``.``, i.e. the engine searches in the directory of the ``qmldir`` file itself.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.addPluginPath`, :sip:ref:`~PyQt6.QtQml.QQmlEngine.setPluginPathList`.
