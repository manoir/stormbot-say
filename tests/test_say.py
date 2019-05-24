from unittest import TestCase, mock
import asyncio



from stormbot_say import Say

def _run(coro):
    asyncio.get_event_loop().run_until_complete(coro)

class TestSayCommand(TestCase):
    def test_argparser(self):
        # Given
        mock_arg_parse = mock.Mock()

        # When
        Say.argparser(mock_arg_parse)

        # Then
        mock_arg_parse.add_argument.assert_called()

    def test_cmdparser(self):
        # Given
        mock_bot = mock.Mock()
        mock_args = mock.Mock()
        mock_arg_parse = mock.Mock()
        plugin = Say(mock_bot, mock_args)

        # When
        plugin.cmdparser(mock_arg_parse)

        # Then
        mock_arg_parse.add_parser.assert_called()

    def test_run(self):
        # Given
        mock_bot = mock.Mock()
        mock_args = mock.Mock()
        mock_parser = mock.Mock()
        mock_parsed_args = mock.Mock()
        mock_peer = mock.Mock()
        plugin = Say(mock_bot, mock_args)
        msg = "Message to say"

        # When
        _run(plugin.run(msg, mock_parser, mock_parsed_args, mock_peer))

        # Then
        #mock_arg_parse.add_parser.assert_called()
