.. sip:method-description::
    :status: todo
    :pysig: 2ef5c79e866b6b22f075b2fb433a909f
    :realsig: (QProcessEnvironment::Initialization)
    :digest: b2a2d6ba2e790dbb4e48c18c91833be0

Creates an object that when set on :sip:ref:`~PyQt6.QtCore.QProcess` will cause it to be executed with environment variables inherited from its parent process.

**Note:** The created object does not store any environment variables by itself, it just indicates to :sip:ref:`~PyQt6.QtCore.QProcess` to arrange for inheriting the environment at the time when the new process is started. Adding any environment variables to the created object will disable inheritance of the environment and result in an environment containing only the added environment variables.

If a modified version of the parent environment is wanted, start with the return value of ``systemEnvironment()`` and modify that (but note that changes to the parent process's environment after that is created won't be reflected in the modified environment).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.inheritsFromParent`, :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.systemEnvironment`.
