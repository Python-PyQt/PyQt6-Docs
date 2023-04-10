.. sip:method-description::
    :status: todo
    :pysig: 14cfca2ae20c9a1cdd63b7e4750587c1
    :realsig: () const
    :digest: 6a2dfc3fd63d83929b69cab2a710be64

Returns the environment that :sip:ref:`~PyQt6.QtCore.QProcess` will pass to its child process. If no environment has been set using :sip:ref:`~PyQt6.QtCore.QProcess.setProcessEnvironment`, this method returns an object indicating the environment will be inherited from the parent.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.setProcessEnvironment`, :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.inheritsFromParent`, :ref:`qprocess-environment-variables`.
