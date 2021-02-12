.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: ()
    :digest: bc62423e3b791638e09ed64b228577d6

Reads the entire content of the stream, and returns it as a QString. Avoid this function when working on large files, as it will consume a significant amount of memory.

Calling :sip:ref:`~PyQt6.QtCore.QTextStream.readLine` is better if you do not know how much data is available.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream.readLine`.
