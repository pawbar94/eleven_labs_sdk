import unittest
from typing import List, Tuple

from conversation_creator.dialogue_decomposer import DialogueDecomposer, ActorName


class TestDialogueDecomposer(unittest.TestCase):
    def test_split_into_roles_returns_proper_data_for_sections_split_with_newline(self):
        text = "[John] Hello, how are you?\n" \
               "[Mary] I'm fine, thanks. And you?\n" \
               "[John] I'm fine too because I've just got back from the trip in the mountains.\n" \
               "[Mary] Great, I'd love to go with you next time."
        expected_result: List[Tuple[ActorName, str]] = [
            ('John', "Hello, how are you?"),
            ('Mary', "I'm fine, thanks. And you?"),
            ('John', "I'm fine too because I've just got back from the trip in the mountains."),
            ('Mary', "Great, I'd love to go with you next time.")
        ]

        roles: List[Tuple[ActorName, str]] = DialogueDecomposer.split_into_roles(actors=['John', 'Mary'], dialogue=text)

        self.assertEqual(expected_result, roles)

    def test_split_into_roles_returns_proper_data_for_sections_with_multiple_newline_split(self):
        text = "[John] Hello, how are you?\n\n" \
               "[Mary] I'm fine, thanks. And you?\n\n" \
               "[John] I'm fine too because I've just got back from the trip in the mountains.\n\n" \
               "[Mary] Great, I'd love to go with you next time."
        expected_result: List[Tuple[ActorName, str]] = [
            ('John', "Hello, how are you?"),
            ('Mary', "I'm fine, thanks. And you?"),
            ('John', "I'm fine too because I've just got back from the trip in the mountains."),
            ('Mary', "Great, I'd love to go with you next time.")
        ]

        roles: List[Tuple[ActorName, str]] = DialogueDecomposer.split_into_roles(actors=['John', 'Mary'], dialogue=text)

        self.assertEqual(expected_result, roles)

    def test_split_into_roles_returns_proper_data_for_sections_with_no_newline_split(self):
        text = "[John] Hello, how are you?" \
               "[Mary] I'm fine, thanks. And you?" \
               "[John] I'm fine too because I've just got back from the trip in the mountains." \
               "[Mary] Great, I'd love to go with you next time."
        expected_result: List[Tuple[ActorName, str]] = [
            ('John', "Hello, how are you?"),
            ('Mary', "I'm fine, thanks. And you?"),
            ('John', "I'm fine too because I've just got back from the trip in the mountains."),
            ('Mary', "Great, I'd love to go with you next time.")
        ]

        roles: List[Tuple[ActorName, str]] = DialogueDecomposer.split_into_roles(actors=['John', 'Mary'], dialogue=text)

        self.assertEqual(expected_result, roles)
