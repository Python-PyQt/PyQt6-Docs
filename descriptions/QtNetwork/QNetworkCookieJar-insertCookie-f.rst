.. sip:method-description::
    :status: todo
    :pysig: c48ed56091f0b4413fabf5fa338fcaef
    :realsig: (const QNetworkCookie&)
    :digest: 1c325a6e31119aa7af04769ba4fef700

Adds *cookie* to this cookie jar.

Returns ``true`` if *cookie* was added, false otherwise.

If a cookie with the same identifier already exists in the cookie jar, it will be overridden.
