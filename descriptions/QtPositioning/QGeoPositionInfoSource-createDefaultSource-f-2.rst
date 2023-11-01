.. sip:method-description::
    :status: todo
    :pysig: e6855c051f6a6194ca551b0ccb843be2
    :realsig: (const QVariantMap&, QObject*)
    :digest: 9c0b741fdd041b13d6a8bb24ff631cdd

Creates and returns a position source with the given *parent* that reads from the system's default sources of location data, or the plugin with the highest available priority.

Returns ``nullptr`` if the system has no default position source, no valid plugins could be found or the user does not have the permission to access the current position.

This method passes *parameters* to the factory to configure the source.
