.. sip:method-description::
    :status: todo
    :pysig: 1afe59e58c16db6bcfee93505f94567b
    :realsig: ()
    :digest: 82a5e19a49b597d1cc629b992fe703d1

Returns a pointer to a shared :sip:ref:`~PyQt6.QtCore.QRandomGenerator` that always uses the facilities provided by the operating system to generate random numbers. The system facilities are considered to be cryptographically safe on at least the following operating systems: Apple OSes (Darwin), BSDs, Linux, Windows. That may also be the case on other operating systems.

They are also possibly backed by a true hardware random number generator. For that reason, the :sip:ref:`~PyQt6.QtCore.QRandomGenerator` returned by this function should not be used for bulk data generation. Instead, use it to seed :sip:ref:`~PyQt6.QtCore.QRandomGenerator` or a random engine from the <random> header.

The object returned by this function is thread-safe and may be used in any thread without locks. It may also be copied and the resulting :sip:ref:`~PyQt6.QtCore.QRandomGenerator` will also access the operating system facilities, but they will not generate the same sequence.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRandomGenerator.securelySeeded`, :sip:ref:`~PyQt6.QtCore.QRandomGenerator.global_`.
