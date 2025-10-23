.. sip:method-description::
    :status: todo
    :pysig: 883579c2ad1a92ea9bbe04c13915d560
    :realsig: (qint64,qint64)
    :digest: a01fc44af3e64852f37b5e2a8d866533

Generates one random 64-bit quantity in the range between *lowest* (inclusive) and *highest* (exclusive), both of which may be negative, but *highest* must be greater than *lowest*.

Note that this function cannot be used to obtain values in the full 64-bit range of ``qint64``. Instead, use :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generate64` and cast to qint64.

**Note:** This function is implemented as a loop, which depends on the random value obtained. On the long run, on average it should loop just under 2 times, but if the random generator is defective, this function may take considerably longer to execute.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generate`, :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generate64`, :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generateDouble`.
