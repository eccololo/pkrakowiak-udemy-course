itinerary = {
    'destination': 'Paris, France',
    'duration': 7,
    'budget': 1500,
    'activities': [
        'Visit the Eiffel Tower',
        'Explore the Louvre',
        'Take a Seine River Cruise',
    ],
}

# Enter your solution here
itinerary["duration"] = 10
itinerary['activities'].append('Visit the Palace of Versailles')
itinerary["accommodation"] = "Hotel"

print(f"""Destination: {itinerary['destination']}
Duration: {itinerary['duration']}
Budget: {itinerary['budget']}
Number of activities: {len(itinerary['activities'])}""")