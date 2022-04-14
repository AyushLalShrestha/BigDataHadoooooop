
data = [
    {"id": 55, "name": "Ram", "city": "kathmandu"},
    {"id": 66, "name": "Hari", "city": "lalitpur"},
    {"id": 77, "name": "Sita", "city": " kathmandu"},
    {"id": 70, "name": "Rama", "city": "Kathmandu "},
    {"id": 88, "name": "Geeta", "city": "pokhara"},
    {"id": 99, "name": "Shyam", "city": " pokhara "},
    {"id": 95, "name": "Parbati", "city": "bhaktapur"}
]

def format_data(data):
    # write your code here
    pass

result = format_data(data)
print(result)

# Expected
# {
#   "kathmandu": ["Ram", "Sita", "Rama"],
#   "lalitpur": ["Hari"],
#   "pokhara": ["Geeta", "Shyam"],
#   "bhaktapur": ["Parbati"]
# }
