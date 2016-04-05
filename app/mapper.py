def character_to_dict(character):
    return {
        'id': character.id,
        'thumbnail': character.thumbnail,
        'name': character.name,
        'description': character.description,
        'number_of_comics': character.number_of_comics,
        'number_of_stories': character.number_of_stories,
        'number_of_series': character.number_of_series
        # 'comics': list(map(comic_to_dict, character.comics))
    }

def comic_to_dict(comic):
    return {
        'id': comic.id,
        'thumbnail': comic.thumbnail,
        'title': comic.title,
        'issue_num': comic.issue_num,
        'description': comic.description,
        'page_count': comic.page_count,
        'number_of_creators': comic.number_of_creators,
        'number_of_characters': comic.number_of_characters,
        'number_of_stories': comic.number_of_stories
        # 'characters': list(map(character_to_dict, comic.characters)),
        # 'creators': list(map(creator_to_dict, comic.creators))
    }

def creator_to_dict(creator):
    return {
        'id': creator.id,
        'thumbnail': creator.thumbnail,
        'first_name': creator.first_name,
        'last_name': creator.last_name,
        'number_of_comics': creator.number_of_comics,
        'number_of_stories': creator.number_of_stories,
        'number_of_series': creator.number_of_series
        # 'comics': list(map(comic_to_dict, creator.comics))
    }
