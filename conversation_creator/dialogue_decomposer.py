from typing import List, Tuple, Dict

ActorName = str


class DialogueDecomposer:
    @staticmethod
    def split_into_roles(actors: List[ActorName], dialogue: str) -> List[Tuple[ActorName, str]]:
        actors_tags_indexes: List[int] = DialogueDecomposer.__get_actors_tags_indexes(actors, dialogue)
        actors_sections: List[str] = DialogueDecomposer.__get_actors_sections(actors_tags_indexes, dialogue)
        roles: List[Tuple[ActorName, str]] = DialogueDecomposer.__get_roles(actors_sections)

        return roles

    @staticmethod
    def __get_actors_tags_indexes(actors: List[ActorName], dialogue: str) -> List[int]:
        actors_tags: List[str] = DialogueDecomposer.__get_actors_tags(actors)
        tags_indexes: List[int] = []
        i: int = 0

        while i < len(dialogue):
            closes_indexes: Dict[str, int] = {tag: dialogue.find(tag, i) for tag in actors_tags}
            closes_indexes = dict(filter(lambda elem: elem[1] >= 0, closes_indexes.items()))

            if not closes_indexes:
                break

            closest_tag = min(closes_indexes, key=closes_indexes.get)
            closest_index = closes_indexes[closest_tag]
            tags_indexes.append(closest_index)
            i = closest_index + len(closest_tag)

        return tags_indexes

    @staticmethod
    def __get_actors_tags(actors: List[ActorName]) -> List[str]:
        return [f'[{actor}]' for actor in actors]

    @staticmethod
    def __get_actors_sections(actors_tags_indexes: List[int], dialogue: str) -> List[str]:
        sections: List[str] = []

        for i in range(len(actors_tags_indexes) - 1):
            sections.append(dialogue[actors_tags_indexes[i]:actors_tags_indexes[i + 1]])

        sections.append(dialogue[actors_tags_indexes[-1]:])

        return sections

    @staticmethod
    def __get_roles(actors_sections: List[str]) -> List[Tuple[ActorName, str]]:
        roles: List[Tuple[ActorName, str]] = []

        for section in actors_sections:
            actor_name: ActorName = section[1:section.index(']')]
            text: str = section[section.index(']') + 2:]
            roles.append((actor_name, text.strip()))

        return roles
