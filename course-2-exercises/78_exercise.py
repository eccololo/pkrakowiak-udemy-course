daily_menu = {
    'burger',
    'fries',
    'hot dog',
    'chicken sandwich',
    'pasta with seafood',
}
fixed_vegetarian_options = {
    'fries',
    'onion rings',
    'pasta with seafood',
    'feta salad',
}

# Enter your solution here

vegetarian_menu = daily_menu.intersection(fixed_vegetarian_options)
print(vegetarian_menu)