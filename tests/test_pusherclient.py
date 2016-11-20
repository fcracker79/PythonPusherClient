import json
import time
from unittest import TestCase

try:
    from unittest import mock
except ImportError:
    # noinspection PyUnresolvedReferences
    import mock


import pusherclient
from tests import pusherserver


class TestPusherClient(TestCase):
    _PORT = 9000
    _MAX_ELAPSED_TIME_SECS = 10

    def test(self):
        server = pusherserver.Pusher(pusherserver.PusherTestServerProtocol, port=self._PORT)

        def _stop_test():
            print('Stop timer')
            client.disconnect()
            server.stop(fromThread=True)

        stop_test = mock.Mock()
        stop_test.side_effect = _stop_test

        success_mock = mock.Mock()

        def _test_channel_callback(data):
            print("Client: %s" % data)

            data = json.loads(data)

            if 'message' in data:
                if data['message'] == "test":
                    # Test successful
                    success_mock()
                    server.stop()
                    client.disconnect()

        test_channel_callback = mock.Mock()
        test_channel_callback.side_effect = _test_channel_callback

        def _connect_handler(_):
            channel = client.subscribe("test_channel")
            channel.bind('test_event', test_channel_callback)

        connect_handler = mock.Mock()
        connect_handler.side_effect = _connect_handler

        # Set up our client and attempt to connect to the server
        appkey = 'appkey'
        pusherclient.Pusher.host = "127.0.0.1"
        client = pusherclient.Pusher(appkey, port=self._PORT, secure=False, reconnect_interval=1)

        print(client._build_url("mykey", False, port=self._PORT))
        client.connection.bind('pusher:connection_established', connect_handler)
        client.connect()

        # Sleep a bit before starting the server - this will cause the clients
        # initial connect to fail, forcing it to use the retry mechanism
        time.sleep(2)

        start = time.time()
        # Start our pusher server on localhost
        server.run()

        if not success_mock.call_count or time.time() - start > self._MAX_ELAPSED_TIME_SECS:
            self.fail('Successful callback not called')
