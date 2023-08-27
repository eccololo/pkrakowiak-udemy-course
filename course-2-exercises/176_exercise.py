posts = [
    {
        'text': 'Lorem ipsum dolor sit amet, consectetur elit.',
        'author': 'John',
        'likes': 52,
    },
    {
        'text': 'Nulla facilisi. Duis eu aliquam libero.',
        'author': 'Jane',
        'likes': 87,
    },
    {
        'text': 'Vestibulum at ipsum ac diam sollicitudin tempor.',
        'author': 'Bob',
        'likes': 113,
    },
    {
        'text': 'Curabitur lobortis luctus velit, et scelerisque eu.',
        'author': 'Alice',
        'likes': 78,
    },
    {
        'text': 'Suspendisse nec enim rutrum, vehicula lectus ut',
        'author': 'Mike',
        'likes': 99,
    },
]

# Enter your solution here

for post in posts:
    if post['likes'] >= 100:
        print(post['text'])
        break
else:
    print("No popular post found.")