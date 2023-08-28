articles = [
    {
        'title': 'Artykuł 1',
        'tags': ['Python', 'baz danych'],
    },
    {
        'title': 'Artykuł 2',
        'tags': ['Python', 'web dev', 'frontend'],
    },
    {
        'title': 'Artykuł 3',
        'tags': ['AI', 'data science'],
    },
]

# Enter your solution here
unique_tags = {tags for article in articles for tags in article['tags']}
print(unique_tags)