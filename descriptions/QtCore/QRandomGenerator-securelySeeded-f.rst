.. sip:method-description::
    :status: todo
    :pysig: 1afe59e58c16db6bcfee93505f94567b
    :realsig: ()
    :digest: 8bd1b486c46cced2c18590812ceee215

Returns a new :sip:ref:`~PyQt6.QtCore.QRandomGenerator` object that was securely seeded with :sip:ref:`~PyQt6.QtCore.QRandomGenerator.system`. This function will obtain the ideal seed size for the algorithm that :sip:ref:`~PyQt6.QtCore.QRandomGenerator` uses and is therefore the recommended way for creating a new :sip:ref:`~PyQt6.QtCore.QRandomGenerator` object that will be kept for some time.

Given the amount of data required to securely seed the deterministic engine, this function is somewhat expensive and should not be used for short-term uses of :sip:ref:`~PyQt6.QtCore.QRandomGenerator` (using it to generate fewer than 2600 bytes of random data is effectively a waste of resources). If the use doesn't require that much data, consider using :sip:ref:`~PyQt6.QtCore.QRandomGenerator.global_` and not storing a :sip:ref:`~PyQt6.QtCore.QRandomGenerator` object instead.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRandomGenerator.global_`, :sip:ref:`~PyQt6.QtCore.QRandomGenerator.system`.
