.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: 41261cd87482cf45ed649940711a5244

Converts this :sip:ref:`~PyQt6.QtCore.QProcessEnvironment` object into a list of strings, one for each environment variable that is set. The environment variable's name and its value are separated by an equal character ('=').

The QStringList contents returned by this function are suitable for presentation. Use with the  function is not recommended due to potential encoding problems under Unix, and worse performance.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.systemEnvironment`, :sip:ref:`~PyQt6.QtCore.QProcess.systemEnvironment`, :sip:ref:`~PyQt6.QtCore.QProcess.setProcessEnvironment`.
