.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: ()
    :digest: 3124c81ab4d673086d52f2e1fd34b8c3

Generates one random qreal in the canonical range [0, 1) (that is, inclusive of zero and exclusive of 1).

This function is equivalent to:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qrandom.py
    :lines: 111-112

The same may also be obtained by using `
                             <http://en.cppreference.com/w/cpp/numeric/random/uniform_real_distribution>`_ with parameters 0 and 1.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generate`, :sip:ref:`~PyQt6.QtCore.QRandomGenerator.generate64`, :sip:ref:`~PyQt6.QtCore.QRandomGenerator.bounded`.
