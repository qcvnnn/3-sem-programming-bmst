class LanguageConstruct:
    def __init__(self, construct_id, title, difficulty_level, language_ref):
        self.construct_id = construct_id
        self.title = title
        self.difficulty_level = difficulty_level
        self.language_ref = language_ref

class ProgLanguage:
    def __init__(self, language_id, language_name):
        self.language_id = language_id
        self.language_name = language_name

class LanguageConstructRelation:
    def __init__(self, lang_ref, construct_ref):
        self.lang_ref = lang_ref
        self.construct_ref = construct_ref

# Данные для тестирования
programming_languages_data = [
    ProgLanguage(10, "Python"),
    ProgLanguage(20, "JavaScript"),
    ProgLanguage(30, "Java"),
    ProgLanguage(40, "C#"),
    ProgLanguage(50, "Ruby")
]

syntax_constructs_data = [
    LanguageConstruct(100, "List Comprehension", 8, 10),
    LanguageConstruct(200, "Arrow Functions", 6, 20),
    LanguageConstruct(300, "Lambda Expressions", 7, 20),
    LanguageConstruct(400, "Decorators", 9, 10),
    LanguageConstruct(500, "Interfaces", 5, 30),
    LanguageConstruct(600, "Extension Methods", 6, 40),
    LanguageConstruct(700, "Blocks", 4, 50)
]

language_relations_data = [
    LanguageConstructRelation(10, 100),
    LanguageConstructRelation(20, 200),
    LanguageConstructRelation(20, 300),
    LanguageConstructRelation(10, 400),
    LanguageConstructRelation(30, 500),
    LanguageConstructRelation(40, 600),
    LanguageConstructRelation(50, 700),
    LanguageConstructRelation(30, 300),  # Java тоже имеет lambda
    LanguageConstructRelation(40, 200),  # C# имеет arrow functions
]

def execute_queries():
    # Формирование связи один-ко-многим
    one_to_many_relation = []
    for lang in programming_languages_data:
        for construct in syntax_constructs_data:
            if construct.language_ref == lang.language_id:
                one_to_many_relation.append({
                    'construct': construct.title,
                    'difficulty': construct.difficulty_level,
                    'language': lang.language_name
                })

    print("Запрос 1: Конструкции и языки (сортировка по языкам)")
    sorted_by_language = sorted(one_to_many_relation, key=lambda x: x['language'])
    for item in sorted_by_language:
        print(f"  {item['language']}: {item['construct']} - сложность {item['difficulty']}")

    print("\nЗапрос 2: Языки с суммарной сложностью конструкций")
    language_complexity_map = {}
    for item in one_to_many_relation:
        lang_name = item['language']
        if lang_name not in language_complexity_map:
            language_complexity_map[lang_name] = 0
        language_complexity_map[lang_name] += item['difficulty']

    sorted_by_complexity = sorted(language_complexity_map.items(),
                                 key=lambda x: x[1], reverse=True)
    for lang, total_complexity in sorted_by_complexity:
        print(f"  {lang}: {total_complexity}")

    print("\nЗапрос 3: Языки содержащие 'Java' и их конструкции")
    # Формирование связи многие-ко-многим
    many_to_many_relation = []
    for relation in language_relations_data:
        lang = next((l for l in programming_languages_data
                    if l.language_id == relation.lang_ref), None)
        construct = next((c for c in syntax_constructs_data
                         if c.construct_id == relation.construct_ref), None)
        if lang and construct:
            many_to_many_relation.append({
                'language': lang.language_name,
                'construct': construct.title,
                'difficulty': construct.difficulty_level
            })

    java_languages_constructs = {}
    for item in many_to_many_relation:
        if 'Java' in item['language']:
            if item['language'] not in java_languages_constructs:
                java_languages_constructs[item['language']] = []
            java_languages_constructs[item['language']].append(item['construct'])

    for lang, constructs in java_languages_constructs.items():
        print(f"  {lang}: {constructs}")

if __name__ == "__main__":
    execute_queries()
