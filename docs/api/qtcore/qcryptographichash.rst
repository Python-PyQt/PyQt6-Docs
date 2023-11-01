:orphan:

.. sip:class:: PyQt6.QtCore.QCryptographicHash
    :description: QtCore/QCryptographicHash-c.rst

    .. sip:enum:: PyQt6.QtCore.QCryptographicHash.Algorithm
        :description: QtCore/QCryptographicHash-Algorithm-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Blake2b_160
            :description: QtCore/QCryptographicHash-Algorithm-Blake2b_160-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Blake2b_256
            :description: QtCore/QCryptographicHash-Algorithm-Blake2b_256-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Blake2b_384
            :description: QtCore/QCryptographicHash-Algorithm-Blake2b_384-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Blake2b_512
            :description: QtCore/QCryptographicHash-Algorithm-Blake2b_512-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Blake2s_128
            :description: QtCore/QCryptographicHash-Algorithm-Blake2s_128-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Blake2s_160
            :description: QtCore/QCryptographicHash-Algorithm-Blake2s_160-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Blake2s_224
            :description: QtCore/QCryptographicHash-Algorithm-Blake2s_224-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Blake2s_256
            :description: QtCore/QCryptographicHash-Algorithm-Blake2s_256-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Keccak_224
            :description: QtCore/QCryptographicHash-Algorithm-Keccak_224-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Keccak_256
            :description: QtCore/QCryptographicHash-Algorithm-Keccak_256-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Keccak_384
            :description: QtCore/QCryptographicHash-Algorithm-Keccak_384-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Keccak_512
            :description: QtCore/QCryptographicHash-Algorithm-Keccak_512-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Md4
            :description: QtCore/QCryptographicHash-Algorithm-Md4-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Md5
            :description: QtCore/QCryptographicHash-Algorithm-Md5-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Sha1
            :description: QtCore/QCryptographicHash-Algorithm-Sha1-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Sha224
            :description: QtCore/QCryptographicHash-Algorithm-Sha224-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Sha256
            :description: QtCore/QCryptographicHash-Algorithm-Sha256-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Sha384
            :description: QtCore/QCryptographicHash-Algorithm-Sha384-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Sha3_224
            :description: QtCore/QCryptographicHash-Algorithm-Sha3_224-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Sha3_256
            :description: QtCore/QCryptographicHash-Algorithm-Sha3_256-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Sha3_384
            :description: QtCore/QCryptographicHash-Algorithm-Sha3_384-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Sha3_512
            :description: QtCore/QCryptographicHash-Algorithm-Sha3_512-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCryptographicHash.Algorithm.Sha512
            :description: QtCore/QCryptographicHash-Algorithm-Sha512-v.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QCryptographicHash.Algorithm`
        :description: QtCore/QCryptographicHash-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.addData
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtCore/QCryptographicHash-addData-f-3.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.addData
        :args:
            bytes
        :description: QtCore/QCryptographicHash-addData-f.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.addData
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :returns:
            bool
        :description: QtCore/QCryptographicHash-addData-f-2.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.algorithm
        :returns:
            :sip:ref:`~PyQt6.QtCore.QCryptographicHash.Algorithm`
        :description: QtCore/QCryptographicHash-algorithm-f.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.hash
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            :sip:ref:`~PyQt6.QtCore.QCryptographicHash.Algorithm`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QCryptographicHash-hash-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.hashLength
        :args:
            :sip:ref:`~PyQt6.QtCore.QCryptographicHash.Algorithm`
        :returns:
            int
        :static:
        :description: QtCore/QCryptographicHash-hashLength-f.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.reset
        :description: QtCore/QCryptographicHash-reset-f.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.result
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QCryptographicHash-result-f.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.resultView
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QCryptographicHash-resultView-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.supportsAlgorithm
        :args:
            :sip:ref:`~PyQt6.QtCore.QCryptographicHash.Algorithm`
        :returns:
            bool
        :static:
        :description: QtCore/QCryptographicHash-supportsAlgorithm-f.rst

    .. sip:method:: PyQt6.QtCore.QCryptographicHash.swap
        :args:
            :sip:ref:`~PyQt6.QtCore.QCryptographicHash`
        :description: QtCore/QCryptographicHash-swap-f.rst
