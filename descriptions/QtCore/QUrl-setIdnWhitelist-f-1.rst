.. sip:method-description::
    :status: todo
    :pysig: e086f7c3dd1fce31f5eda08ab7ea2590
    :realsig: (const QStringList&)
    :digest: cc88940c4178f1b42670305d661d4499

Sets the whitelist of Top-Level Domains (TLDs) that are allowed to have non-ASCII characters in domains to the value of *list*.

Note that if you call this function, you need to do so *before* you start any threads that might access :sip:ref:`~PyQt6.QtCore.QUrl.idnWhitelist`.

Qt comes with a default list that contains the Internet top-level domains that have published support for Internationalized Domain Names (IDNs) and rules to guarantee that no deception can happen between similarly-looking characters (such as the Latin lowercase letter ``'a'`` and the Cyrillic equivalent, which in most fonts are visually identical).

This list is periodically maintained, as registrars publish new rules.

This function is provided for those who need to manipulate the list, in order to add or remove a TLD. It is not recommended to change its value for purposes other than testing, as it may expose users to security risks.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.idnWhitelist`.
