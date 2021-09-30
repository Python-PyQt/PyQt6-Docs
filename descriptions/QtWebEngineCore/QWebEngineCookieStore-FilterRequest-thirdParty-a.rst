.. sip:attribute-description::
    :status: todo
    :digest: 19c74fda43dc1e24c69d211e095f952c

This variable holds Whether this is considered a third-party access..

This is calculated by comparing FilterRequest::origin and FilterRequest::firstPartyUrl and checking if they share a common origin that is not a top-domain (like .com or .co.uk), or a known hosting site with independently owned subdomains.

.. seealso:: firstPartyUrl, origin.
