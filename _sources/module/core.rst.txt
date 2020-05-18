****
Core
****

.. automodule:: httpsuite.core

----

Request
*******

.. autoclass:: httpsuite.core.Request

  .. autoproperty:: httpsuite.core.Request.method

  .. autoproperty:: httpsuite.core.Request.target

  .. autoproperty:: httpsuite.core.Request.protocol

  .. autoproperty:: httpsuite.core.Request.headers

  .. autoproperty:: httpsuite.core.Request.body

  .. attribute:: raw

    Bytes representation of the ``Request``.

    .. note::
      ``.raw`` will return the bytes representation of the ``Request`` with
      ``\r\n`` escape. Intended to be use for communicating.

    Example:

    .. code-block:: python

      r = Request(
          method="GET",
          target="/get",
          protocol="HTTP/1.1",
          headers={"Host": "httpbin.org", "Connection": "close", "Accept": "*/*"},
          body=None,
      )

      print(r.raw)

    .. code-block::

        b'GET /get HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\nAccept: */*\r\n\r\n'

  .. autofunction:: httpsuite.core.Request.__str__

----

Response
********

.. autoclass:: httpsuite.core.Response

  .. autoproperty:: httpsuite.core.Response.protocol

  .. autoproperty:: httpsuite.core.Response.status

  .. autoproperty:: httpsuite.core.Response.status_msg

  .. autoproperty:: httpsuite.core.Response.headers

  .. autoproperty:: httpsuite.core.Response.body

  .. attribute:: raw

    Bytes representation of the ``Response``.

    .. note::
      ``.raw`` will return the bytes representation of the ``Response`` with
      ``\r\n`` escape. Intended to be use for communicating.

    Example:

    .. code-block:: python

      r = Response(
          protocol="HTTP/1.1",
          status=200,
          status_msg="OK",
          headers={"Host": "httpbin.org", "Connection": "close", "Accept": "*/*"},
          body=None,
      )

      print(r.raw)

    .. code-block::

        b'HTTP/1.1 200 OK\r\nHost: httpbin.org\r\nConnection: close\r\nAccept: */*\r\n\r\n'

  .. autofunction:: httpsuite.core.Response.__str__

----

Message
*******

.. autoclass:: httpsuite.core.Message
