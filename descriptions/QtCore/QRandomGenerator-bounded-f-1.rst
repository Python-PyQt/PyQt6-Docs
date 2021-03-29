.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qint64)
    :digest: 9afff146cff0da5206c466395941a0b7

This is an overloaded function.

Generates one random 64-bit quantity in the range between 0 (inclusive) and *highest* (exclusive). *highest* must be positive.

Note that this function cannot be used to obtain values in the full 64-bit range of ``qint64``. Instead, use :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generate64` and cast to qint64 or instead use the unsigned version of this function.

**Note:** This function is implemented as a loop, which depends on the random value obtained. On the long run, on average it should loop just under 2 times, but if the random generator is defective, this function may take considerably longer to execute.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generate`, :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generate64`, :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generateDouble`.
